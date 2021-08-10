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
    company_name = models.CharField('Название вашей компании', max_length=50, blank=True)
    phone = models.CharField('Телефон', max_length=50, blank=True)
    email = models.EmailField('E-mail', max_length=50, blank=True)
    loading_date = models.DateField('Дата загрузки', blank=True)
    loading_place = models.CharField('Место загрузки', max_length=120, required=True)
    weight = models.FloatField('Общий вес (кг)', blank=True)
    cargo_name = models.CharField('Наименование груза', max_length=50, required=True)
    cc_place = models.CharField('Место растаможки', max_length=50, required=True)
    volume = models.FloatField('Объем')
    transport = models.CharField('Тип транспорта', max_length=150)
    unloading_place = models.CharField('Место выгрузки', max_length=150)
    cost = models.CharField('Стоимость груза', max_length=150, required=True)
    transport = models.CharField('Тип транспорта', max_length=150)
    message = models.TextField('Дополнительно', max_length=500, blank=True)

    class Meta:
        verbose_name = 'Запрос на перевозку'
        verbose_name_plural = 'Запросы на перевозку'

    def __str__(self):
        return f'{self.company_name} {self.phone}, {self.email}'
