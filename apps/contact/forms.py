import random
from django import forms
from django.core.signing import Signer, BadSignature
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from .models import ContactMessage

signer = Signer(salt='contact_math_captcha')

class ContactForm(forms.ModelForm):
    website = forms.CharField(required=False, widget=forms.HiddenInput, label='')
    captcha_token = forms.CharField(widget=forms.HiddenInput, required=False)
    captcha_answer = forms.IntegerField(
        label='',
        widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': '?'})
    )

    class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'phone', 'subject', 'message']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': _('Votre nom complet')}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'exemple@domaine.com'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '+212 6 XX XX XX XX'}),
            'subject': forms.TextInput(attrs={'class': 'form-control', 'placeholder': _('Objet de votre demande')}),
            'message': forms.Textarea(attrs={'class': 'form-control', 'rows': 5, 'placeholder': _('Détaillez votre projet...')}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        token = None
        if self.is_bound:
            token = self.data.get('captcha_token')
            if token:
                try:
                    val = signer.unsign(token)
                    a, b, expected = val.split(':')
                    self.captcha_question = f'{a} + {b} = ?'
                    self.expected_captcha = int(expected)
                except (BadSignature, ValueError):
                    token = None

        if not token:
            a = random.randint(2, 12)
            b = random.randint(2, 12)
            expected = a + b
            token = signer.sign(f'{a}:{b}:{expected}')
            self.captcha_question = f'{a} + {b} = ?'
            self.expected_captcha = expected
            self.initial['captcha_token'] = token

    def clean_website(self):
        website = self.cleaned_data.get('website')
        if website:
            raise ValidationError(_('Spam detected.'))
        return website

    def clean_captcha_answer(self):
        answer = self.cleaned_data.get('captcha_answer')
        token = self.data.get('captcha_token')
        if not token:
            raise ValidationError(_('Session de vérification expirée. Veuillez réessayer.'))
        try:
            val = signer.unsign(token)
            part1, part2, expected = val.split(':')
            if answer != int(expected):
                raise ValidationError(_('Réponse incorrecte. Veuillez réessayer.'))
        except (BadSignature, ValueError):
            raise ValidationError(_('Vérification invalide. Veuillez réessayer.'))
        return answer
