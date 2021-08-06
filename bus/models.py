from django.db import models
from django.utils.safestring import mark_safe
import os


class Head(models.Model):
    title = models.CharField('Title страницы', max_length=120, blank=True,)
    title_on_image = models.CharField('Заголовок на главном фото', max_length=50, blank=True,)
    logo = models.CharField('Лого', max_length=30, blank=True,)
    image = models.FileField('Главное фото', blank=True)

    def image_preview(self):
        if self.image:
            return mark_safe('<img src="%s" style="width:100px; height:70px;" />' % self.image.url)
        else:
            return 'No Image Found'

    image_preview.short_description = 'Фото'

    class Meta:
        verbose_name = 'Верхняя часть с фото'
        verbose_name_plural = 'Верхняя часть с фото'

    def __str__(self):
        return self.logo


class Contact(models.Model):
    f_name = models.CharField('Имя', max_length=50, blank=True)
    l_name = models.CharField('Фамилия', max_length=50, blank=True)
    email = models.EmailField('Емейл', max_length=50, blank=True)
    subject = models.CharField('Тема', max_length=50, blank=True)
    message = models.TextField('Сообщение', max_length=500, blank=True)

    class Meta:
        verbose_name = 'Сообщение с сайта'
        verbose_name_plural = 'Сообщения с сайта'

    def __str__(self):
        return f'{self.l_name} {self.f_name}, {self.email}'
