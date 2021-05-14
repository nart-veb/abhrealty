# Generated by Django 3.1.4 on 2021-04-28 17:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_houses_type_material'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reviews',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60, verbose_name='Никнейм')),
                ('description', models.CharField(blank=True, max_length=1000, verbose_name='Описание')),
                ('photo', models.ImageField(blank=True, upload_to='photos', verbose_name='Фото')),
                ('video', models.FileField(blank=True, upload_to='videos', verbose_name='Видео')),
                ('date', models.DateField()),
            ],
            options={
                'verbose_name': 'Отзывы',
                'verbose_name_plural': 'Отзывы',
            },
        ),
    ]
