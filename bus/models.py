from django.db import models
from django.utils.safestring import mark_safe
from django.utils import timezone
import os
import datetime


class Head(models.Model):
    title = models.CharField('Title страницы', max_length=120, blank=True, default='AAA')
    title_on_image = models.CharField('Заголовок на главном фото', max_length=50, blank=True, default='FFF')
    logo = models.CharField('Лого', max_length=30, blank=True, default='КУБКОТРАНС')
    image = models.FileField('Главное фото', blank=True, default='static/images/blog_1.jpg')

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
    company_name = models.CharField('Название вашей компании', max_length=50, blank=True)
    phone = models.CharField('Телефон', max_length=50, blank=True)
    email = models.EmailField('E-mail', max_length=50, blank=True)
    loading_date = models.DateField('Дата загрузки', default=timezone.now())
    loading_place = models.CharField('Место загрузки', max_length=120, blank=True)
    weight = models.FloatField('Общий вес (кг)', blank=True, default=0.1)
    cargo_name = models.CharField('Наименование груза', max_length=50, default='Груз')
    cc_place = models.CharField('Место растаможки', max_length=50, blank=True)
    volume = models.FloatField('Объем', blank=True, default=0.1)
    transport = models.CharField('Тип транспорта', max_length=150, blank=True)
    unloading_place = models.CharField('Место выгрузки', max_length=150, blank=True)
    cost = models.CharField('Стоимость груза', max_length=150, blank=True)
    message = models.TextField('Дополнительно', max_length=500, blank=True)

    class Meta:
        verbose_name = 'Запрос на перевозку'
        verbose_name_plural = 'Запросы на перевозку'

    def __str__(self):
        return f'{self.company_name} {self.phone}, {self.email}'
