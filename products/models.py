from django.db import models
from django.utils.translation import gettext_lazy as _


class Category(models.Model):
    """Категория продукции (Пиво, Напитки, Снеки)"""
    name = models.CharField(_('Название'), max_length=100, unique=True)
    slug = models.SlugField(_('Слаг'), max_length=100, unique=True)
    description = models.TextField(_('Описание'), blank=True)
    order = models.PositiveIntegerField(_('Порядок'), default=0)

    class Meta:
        verbose_name = _('Категория')
        verbose_name_plural = _('Категории')
        ordering = ['order', 'name']

    def __str__(self):
        return self.name


class Brand(models.Model):
    """Бренд пива (Singha, Leo, Saigon и т.д.)"""
    name = models.CharField(_('Название бренда'), max_length=100, unique=True)
    slug = models.SlugField(_('Слаг'), max_length=100, unique=True)
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name='brands',
        verbose_name=_('Категория')
    )
    description = models.TextField(_('Описание бренда'), blank=True)
    history = models.TextField(_('Историческая справка'), blank=True)
    logo = models.ImageField(
        _('Логотип'), upload_to='brands/logos/', blank=True)
    background_image = models.ImageField(
        _('Фоновое изображение'),
        upload_to='brands/backgrounds/',
        blank=True
    )
    order = models.PositiveIntegerField(_('Порядок'), default=0)

    class Meta:
        verbose_name = _('Бренд')
        verbose_name_plural = _('Бренды')
        ordering = ['order', 'name']

    def __str__(self):
        return self.name


class Product(models.Model):
    """Конкретный продукт (например, Singha Lager 0.5L бутылка)"""
    name = models.CharField(_('Название продукта'), max_length=200)
    slug = models.SlugField(_('Слаг'), max_length=200, unique=True)
    brand = models.ForeignKey(
        Brand,
        on_delete=models.CASCADE,
        related_name='products',
        verbose_name=_('Бренд')
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name='products',
        verbose_name=_('Категория')
    )
    description = models.TextField(_('Описание'), blank=True)
    volume_ml = models.PositiveIntegerField(
        _('Объем (мл)'), null=True, blank=True)
    alcohol_percentage = models.DecimalField(
        _('Алкоголь %'),
        max_digits=4,
        decimal_places=2,
        null=True,
        blank=True
    )
    packaging = models.CharField(_('Упаковка'), max_length=50, blank=True)
    image = models.ImageField(
        _('Изображение'), upload_to='products/', blank=True)
    price = models.DecimalField(
        _('Цена (руб)'),
        max_digits=10,
        decimal_places=2,
        null=True,
        blank=True
    )
    available = models.BooleanField(_('В наличии'), default=True)
    order = models.PositiveIntegerField(_('Порядок'), default=0)

    class Meta:
        verbose_name = _('Продукт')
        verbose_name_plural = _('Продукты')
        ordering = ['order', 'name']

    def __str__(self):
        return f'{self.brand.name} - {self.name}'
