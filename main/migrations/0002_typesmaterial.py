# Generated by Django 3.1.4 on 2021-04-26 17:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Typesmaterial',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60, verbose_name='Заголовок')),
            ],
            options={
                'verbose_name': 'Тип материала дома',
                'verbose_name_plural': 'Материал дома',
            },
        ),
    ]
