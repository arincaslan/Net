from django.db import models
from ckeditor.fields import RichTextField
from django.template.defaultfilters import slugify
from unidecode import unidecode
# Create your models here.


class Article(models.Model):
    title = models.CharField(max_length = 50, verbose_name="Başlık")
    content = RichTextField(('Makale İçeriği'))
    created_date = models.DateTimeField(auto_now_add=True, verbose_name="Oluşturulma Tarihi")
    article_slug = models.SlugField(unique= True, default='defaultVal')
    article_meta_description = models.CharField(('Makale Meta Açıklaması'), max_length= 250, default= 'default meta acıklaması')

    KATEGORILER = (
        ('Mobil Uygulamar', 'Mobil Uygulamalar'),
        ('Web Tasarımları', 'Web Tasarımları'),
        ('Reklam Hizmetleri', 'Reklam Hizmetleri'),
    )

    article_kategori = models.CharField(('Makale Kategorisi'), max_length=50, choices=KATEGORILER, default= 'websitesi')

    article_image = models.ImageField(('Makale Resmi'), null= True, blank= True)

    def __str__(self):
        return self.title

    class Meta:
        ordering= ('-created_date',)
        verbose_name = 'Makale'
        verbose_name_plural = 'Makaleler'

    def save(self, *args, **kwargs):
        self.article_slug = slugify(unidecode(self.title))
        super(Article, self).save(*args, **kwargs)

class Product(models.Model):
    product_title = models.CharField(max_length = 50, verbose_name="Ürün İsmi")
    product_content= RichTextField(('Ürün Açıklaması'))
    product_created_date = models.DateTimeField(auto_now_add=True, verbose_name="İlan Oluşturulma Tarihi")
    product_slug = models.SlugField(unique= True, default='defaultVal')
    product_meta_description = models.CharField(('Makale Meta Açıklaması'), max_length= 250, default= 'default meta acıklaması')

    FIYATLAR = (
    ("TL","TL"),
    ("$","$"),
    ("€","€")
    )

    product_price= models.CharField(max_length = 50 ,verbose_name="Ürün Fiyatı")
    product_price_unit=models.CharField(max_length = 50, choices=FIYATLAR ,verbose_name="Ürün Fiyatı Birimi", default= 'fbirim')
    product_image = models.ImageField(('Ürün Resmi'), null= True, blank= True)

    def __str__(self):
        return self.product_title

    class Meta:
        ordering= ('-product_created_date',)
        verbose_name = 'Ürün'
        verbose_name_plural = 'Ürünler'

    def save(self, *args, **kwargs):
        self.product_slug = slugify(unidecode(self.product_title))
        super(Product, self).save(*args, **kwargs)


class Contact(models.Model):
    iletisim_isim = models.CharField(('isim'), max_length=100, null=True)
    iletisim_mail = models.CharField(("email"), max_length=100)
    iletisim_mesaj = models.TextField(("mesaj"))
    iletisim_tarihi = models.DateTimeField(('İletişim Formu Gönderilme Tarihi'), auto_now_add=True)

    def __str__(self):
        return self.iletisim_isim

    class Meta:
        verbose_name = ("İletişim Talebi")
        verbose_name_plural = ("İletişim Talepleri")
        ordering = ("-iletisim_tarihi",)
