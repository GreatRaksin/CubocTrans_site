from django import forms
from django.core.mail import send_mail as django_send_mail
from django.forms import ModelForm
from .models import Contact


class UserForm(ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'
        widgets = {
            'company_name': forms.TextInput(attrs={'placeholder': 'Название компании',
                                             'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'placeholder': 'Телефон',
                                             'class': 'form-control'}),
            'email': forms.TextInput(attrs={'placeholder': 'E-Mail',
                                            'class': 'form-control'}),
            'loading_date': forms.TextInput(attrs={'placeholder': 'Дата загрузки',
                                              'class': 'form-control'}),
            'loading_place': forms.TextInput(attrs={'placeholder': 'Место загрузки',
                                       'class': 'form-control'}),
            'weight': forms.TextInput(attrs={'placeholder': 'Общая масса (кг)',
                                       'class': 'form-control'}),
            'cargo_name': forms.TextInput(attrs={'placeholder': 'Наименование груза',
                                       'class': 'form-control'}),
            'cc_place': forms.TextInput(attrs={'placeholder': 'Место растаможки',
                                       'class': 'form-control'}),
            'volume': forms.TextInput(attrs={'placeholder': 'Объем',
                                       'class': 'form-control'}),
            'transport': forms.TextInput(attrs={'placeholder': 'Тип транспорта',
                                       'class': 'form-control'}),
            'unloading_place': forms.TextInput(attrs={'placeholder': 'Место выгрузки',
                                       'class': 'form-control'}),
            'cost': forms.TextInput(attrs={'placeholder': 'Стоимость груза',
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
