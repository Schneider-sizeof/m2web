import random
from django import forms
from django.core.signing import Signer, BadSignature
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from .models import WholesaleInquiry

signer = Signer(salt='wholesale_math_captcha')

class WholesaleInquiryForm(forms.ModelForm):
    website = forms.CharField(required=False, widget=forms.HiddenInput, label='')
    captcha_token = forms.CharField(widget=forms.HiddenInput, required=False)
    captcha_answer = forms.IntegerField(
        label='',
        widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': '?'})
    )

    class Meta:
        model = WholesaleInquiry
        fields = ['company_name', 'contact_person', 'email', 'phone', 'city', 'monthly_volume', 'hardware_types_needed', 'message']
        widgets = {
            'company_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': _('Ex: Atlas Logistique SARL')}),
            'contact_person': forms.TextInput(attrs={'class': 'form-control', 'placeholder': _('Nom du responsable')}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'contact@entreprise.ma'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '+212 6 XX XX XX XX'}),
            'city': forms.TextInput(attrs={'class': 'form-control', 'placeholder': _('Fès, Casablanca, Tanger...')}),
            'monthly_volume': forms.Select(attrs={'class': 'form-select'}),
            'hardware_types_needed': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': _('Ex: Traceurs OBD 4G, traceurs filaires avec relais coupure...')}),
            'message': forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'placeholder': _('Présentation de vos activités et besoins...')}),
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
