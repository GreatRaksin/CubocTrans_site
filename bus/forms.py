from django import forms
from django.core.mail import send_mail as django_send_mail
from django.forms import ModelForm
from .models import Contact


class UserForm(ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'
        widgets = {
            'l_name': forms.TextInput(attrs={'placeholder': 'Имя',
                                             'class': 'form-control'}),
            'f_name': forms.TextInput(attrs={'placeholder': 'Фамилия',
                                             'class': 'form-control'}),
            'email': forms.TextInput(attrs={'placeholder': 'E-Mail',
                                            'class': 'form-control'}),
            'subject': forms.TextInput(attrs={'placeholder': 'Тема',
                                              'class': 'form-control'}),
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
