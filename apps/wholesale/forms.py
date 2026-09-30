import random
from django import forms
from django.core.signing import Signer, BadSignature
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from .models import WholesaleInquiry, ResellerInquiry, PlatformInquiry

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


class ResellerInquiryForm(forms.ModelForm):
    website = forms.CharField(required=False, widget=forms.HiddenInput, label='')
    captcha_token = forms.CharField(widget=forms.HiddenInput, required=False)
    captcha_answer = forms.IntegerField(
        label='',
        widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': '?'})
    )

    class Meta:
        model = ResellerInquiry
        fields = [
            'company_name', 'contact_person', 'email', 'phone', 'city', 
            'activity_type', 'expected_volume', 'has_installed_before', 
            'interested_in_whitelabel', 'message'
        ]
        widgets = {
            'company_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': _('Ex: Auto Élec Express SARL')}),
            'contact_person': forms.TextInput(attrs={'class': 'form-control', 'placeholder': _('Nom & Prénom')}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'contact@atelier.ma'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '+212 6 XX XX XX XX'}),
            'city': forms.TextInput(attrs={'class': 'form-control', 'placeholder': _('Fès, Casablanca, Tanger, Marrakech...')}),
            'activity_type': forms.Select(attrs={'class': 'form-select'}),
            'expected_volume': forms.Select(attrs={'class': 'form-select'}),
            'has_installed_before': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'interested_in_whitelabel': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'message': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': _('Décrivez votre zone d\'intervention, votre équipement ou vos besoins spécifiques...')}),
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
            a = random.randint(2, 9)
            b = random.randint(1, 9)
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


class PlatformInquiryForm(forms.ModelForm):
    website = forms.CharField(required=False, widget=forms.HiddenInput, label='')
    captcha_token = forms.CharField(widget=forms.HiddenInput, required=False)
    captcha_answer = forms.IntegerField(
        label='',
        widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': '?'})
    )

    class Meta:
        model = PlatformInquiry
        fields = [
            'company_name', 'contact_name', 'email', 'phone', 'city', 
            'acquisition_mode', 'fleet_size', 'needs_reports', 
            'needs_fuel_sensor', 'message'
        ]
        widgets = {
            'company_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': _('Ex: Atlas Transport & Logistique')}),
            'contact_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': _('Nom du responsable flotte / DSI')}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'direction@societe.ma'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '+212 6 XX XX XX XX'}),
            'city': forms.TextInput(attrs={'class': 'form-control', 'placeholder': _('Fès, Casablanca, Tanger...')}),
            'acquisition_mode': forms.Select(attrs={'class': 'form-select'}),
            'fleet_size': forms.Select(attrs={'class': 'form-select'}),
            'needs_reports': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'needs_fuel_sensor': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'message': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': _('Précisez vos besoins : type de véhicules, besoin d\'API ERP, marque blanche, nombre d\'utilisateurs...')}),
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
            a = random.randint(1, 9)
            b = random.randint(2, 8)
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
