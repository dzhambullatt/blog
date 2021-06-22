from django.db import models
from django.urls import reverse


class News(models.Model):
    title = models.CharField('Название', max_length=150)
    content = models.TextField('Контент', blank=True)
    created_ad = models.DateTimeField('Дата регистрации', auto_now_add=True)
    updated_ad = models.DateTimeField('Дата обновления', auto_now=True)
    photo = models.ImageField('Фото', upload_to='photos/%Y/%m/%d/', blank=True)
    is_published = models.BooleanField('Опубликовано', default=True)
    category = models.ForeignKey('Category', on_delete=models.PROTECT, null=True, verbose_name='Категория')

    def get_absolute_url(self):
        return reverse('view_news', kwargs={"news_id": self.pk})

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
        ordering = ['-created_ad']


class Category(models.Model):
    title = models.CharField('Название', max_length=100, db_index=True)

    def get_absolute_url(self):
        return reverse('category', kwargs={"category_id": self.pk})

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Категорию'
        verbose_name_plural = 'Категории'
        ordering = ['title']
