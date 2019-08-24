# Generated by Django 2.2.3 on 2019-08-21 00:07

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Başlık')),
                ('content', ckeditor.fields.RichTextField(verbose_name='Makale İçeriği')),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='Oluşturulma Tarihi')),
                ('article_slug', models.SlugField(default='defaultVal', unique=True)),
                ('article_meta_description', models.CharField(default='default meta acıklaması', max_length=250, verbose_name='Makale Meta Açıklaması')),
                ('article_kategori', models.CharField(choices=[('Mobil Uygulamar', 'Mobil Uygulamalar'), ('Web Tasarımları', 'Web Tasarımları'), ('Reklam Hizmetleri', 'Reklam Hizmetleri')], default='websitesi', max_length=50, verbose_name='Makale Kategorisi')),
                ('article_image', models.ImageField(blank=True, null=True, upload_to='', verbose_name='Makale Resmi')),
            ],
            options={
                'verbose_name': 'Makale',
                'verbose_name_plural': 'Makaleler',
                'ordering': ('-created_date',),
            },
        ),
    ]
