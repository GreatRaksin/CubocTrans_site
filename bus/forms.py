from django import forms
from django.core.mail import send_mail as django_send_mail
from django.forms import ModelForm
from .models import Contact


class UserForm(ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'
        widgets = {
            'company_name': forms.TextInput(attrs={'placeholder': 'My Company',
                                                   'class': 'form-control',
                                            'required': True},
                                            ),
            'phone': forms.TextInput(attrs={'placeholder': '+375 (29) 123 45 67',
                                            'class': 'form-control',
                                            'required': True}),
            'email': forms.TextInput(attrs={'placeholder': 'E-Mail',
                                            'class': 'form-control',
                                            'required': True}),
            'loading_date': forms.DateInput(attrs={'class': 'form-control'}),
            'loading_place': forms.TextInput(attrs={'placeholder': 'Germany, Leipzig',
                                                    'class': 'form-control',
                                            'required': True}),
            'weight': forms.NumberInput(attrs={'placeholder': '1200',
                                               'class': 'form-control'}),
            'cargo_name': forms.TextInput(attrs={'placeholder': 'Electronics',
                                                 'class': 'form-control',
                                            'required': True}),
            'cc_place': forms.TextInput(attrs={'placeholder': 'Russia, Moscow',
                                               'class': 'form-control'}),
            'volume': forms.NumberInput(attrs={'placeholder': 'm3',
                                               'class': 'form-control',
                                               'required': True}),
            'transport': forms.TextInput(attrs={'placeholder': 'Фура',
                                                'class': 'form-control',
                                            'required': True}),
            'unloading_place': forms.TextInput(attrs={'placeholder': 'Склад Ярцево',
                                                      'class': 'form-control',
                                            'required': True}),
            'cost': forms.NumberInput(attrs={'placeholder': 'Стоимость груза',
                                             'class': 'form-control',
                                             'required': True}),
            'message': forms.Textarea(attrs={'placeholder': 'Сообщение',
                                             'class': 'form-control'})
        }

    def send_mail(self):
        return django_send_mail('Сообщение с сайта bus-comfort.by',
                                str('Имя: ') + self.cleaned_data['f_name'] + '\n' + str('Фамилия: ') +
                                self.cleaned_data['l_name'] +
                                '\n' + str('Емейл: ') + self.cleaned_data['email'] + '\n' + str('Тема: ') +
                                self.cleaned_data['subject'] + '\n' + str('Сообщение: ') + self.cleaned_data['message'],
                                'no-reply@bus-comfort.by',
                                ['info@iko-studio.com'])
