from django.db import models
from django.urls import reverse
from django.utils.text import slugify


class TimeStampedModel(models.Model):
    created_at = models.DateTimeField('Створено', auto_now_add=True)
    updated_at = models.DateTimeField('Оновлено', auto_now=True)

    class Meta:
        abstract = True


class Category(TimeStampedModel):
    name = models.CharField('Назва', max_length=120)
    slug = models.SlugField('Slug', max_length=140, unique=True, blank=True)
    description = models.TextField('Опис', blank=True)

    class Meta:
        verbose_name = 'Категорія'
        verbose_name_plural = 'Категорії'
        ordering = ['name']

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name, allow_unicode=True)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('shop:category', kwargs={'slug': self.slug})


class Brand(TimeStampedModel):
    name = models.CharField('Назва', max_length=120)
    slug = models.SlugField('Slug', max_length=140, unique=True, blank=True)
    description = models.TextField('Опис', blank=True)
    logo = models.ImageField('Логотип', upload_to='brands/', blank=True)

    class Meta:
        verbose_name = 'Бренд'
        verbose_name_plural = 'Бренди'
        ordering = ['name']

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name, allow_unicode=True)
        super().save(*args, **kwargs)


class Perfume(TimeStampedModel):
    name = models.CharField('Назва', max_length=200)
    slug = models.SlugField('Slug', max_length=220, unique=True, blank=True)
    brand = models.ForeignKey(
        Brand,
        on_delete=models.PROTECT,
        related_name='perfumes',
        verbose_name='Бренд',
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.PROTECT,
        related_name='perfumes',
        verbose_name='Категорія',
    )
    description = models.TextField('Опис', blank=True)
    product_type = models.CharField(
        'Тип продукту',
        max_length=80,
        default='Extrait de Parfum',
    )
    price = models.DecimalField('Ціна', max_digits=10, decimal_places=2)
    volume_ml = models.PositiveIntegerField('Обʼєм (мл)', default=50)
    image = models.ImageField('Зображення', upload_to='perfumes/', blank=True)
    is_available = models.BooleanField('В наявності', default=True)
    is_featured = models.BooleanField('На головній', default=False)

    class Meta:
        verbose_name = 'Парфум'
        verbose_name_plural = 'Парфуми'
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.brand.name} — {self.name}'

    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(f'{self.brand.name}-{self.name}', allow_unicode=True)
            self.slug = base_slug
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('shop:perfume_detail', kwargs={'slug': self.slug})
