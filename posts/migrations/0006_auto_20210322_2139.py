# Generated by Django 2.2.6 on 2021-03-22 18:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0005_post_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, help_text='Добавьте изображение к посту', null=True, upload_to='posts/', verbose_name='Изображение'),
        ),
    ]
