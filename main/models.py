from django.db import models
from django import forms


class TypesApartments(models.Model):
    title = models.CharField('Название', max_length=200)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'недвижимости'
        verbose_name_plural = 'Тип недвижимости'

class Typesale(models.Model):
    name = models.CharField('тип', max_length=200)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Тип продажи'
        verbose_name_plural = 'тип'

class Cities(models.Model):
    title = models.CharField('Название', max_length=200)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'города'
        verbose_name_plural = 'Город'

class Typehouse(models.Model):
    name = models.CharField('Заголовок', max_length=60)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Состояние'
        verbose_name_plural = 'Состояние'


class Leaseterms(models.Model):
    name = models.CharField('Тип аренды', max_length=60)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Тип аренды'
        verbose_name_plural = 'Тип аренды'


VIP_MASS = [
        ('1', 'Нет'),
        ('2', 'Да'),
]




class Announcement(models.Model):
    typesale = models.ForeignKey(Typesale, on_delete=models.CASCADE , max_length=50 , blank=True, verbose_name='Продажа / Аренда')
    leaseterms = models.ForeignKey(Leaseterms, on_delete=models.CASCADE, default=1, blank=True, verbose_name='Длительно/Посуточно (аренда)')
    price = models.CharField('Цена', max_length=50, blank=True)
    cities = models.ForeignKey(Cities, on_delete=models.CASCADE , max_length=50 , blank=True, verbose_name='Город')
    address = models.CharField('Район' , max_length=50 , blank=True)
    totalarea = models.CharField('Общая площадь' , max_length=50 , blank=True)
    distancesea = models.CharField('Расстояние до море' , max_length=50 , blank=True)
    distancetrack = models.CharField('Расстояние до трассы' , max_length=50 , blank=True)
    vip = models.CharField('Сделать VIP:', max_length=10, choices=VIP_MASS, default='1' , blank=True)
    ownership = models.CharField('Право собственности' , max_length=50 , blank=True)
    description = models.CharField('Описание' , max_length=300 , blank=True)


    class Meta:
        verbose_name = 'Основные характеристики'
        verbose_name_plural = 'Характеристики'



class ProjectImage(models.Model):
    image = models.ImageField(upload_to='prjimages/%Y/%m/%d/%H/%M/%S/', blank=True)
    image_project = models.ForeignKey(Announcement, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'картинку'
        verbose_name_plural = 'Все картинки'



class Condition(models.Model):
    name = models.CharField('Заголовок', max_length=60)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Состояние'
        verbose_name_plural = 'Состояние'

class Typesmaterial(models.Model):
    name = models.CharField('Заголовок', max_length=60)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Тип материала дома'
        verbose_name_plural = 'Материал дома'

class Houses(models.Model):
    name = models.CharField('Заголовок', max_length=60)
    type_material = models.ForeignKey(Typesmaterial, on_delete=models.CASCADE, default='1', blank=True, verbose_name='Тип материала')
    floor = models.CharField('Кол-во этажей', max_length=60, blank=True)
    rooms = models.CharField('Кол-во комнат', max_length=60, blank=True)
    house_area = models.CharField('Площадь дома', max_length=60, blank=True)
    condition = models.ForeignKey(Condition, on_delete=models.CASCADE, blank=True, verbose_name='Состояние')
    ceiling_height = models.CharField('Высота потолков', max_length=60, blank=True)
    year_construction = models.CharField('Высота потолков', max_length=60, blank=True)
    announcement = models.ForeignKey(Announcement, on_delete=models.CASCADE, verbose_name='Главная информация')
    name_class = 'houses'

    def __str__(self):
        return self.name + ' (' + str(self.announcement.typesale) + ')'

    class Meta:
        verbose_name = 'Дом'
        verbose_name_plural = 'Дома'



class Apartments(models.Model):
    name = models.CharField('Заголовок', max_length=60)
    condition = models.ForeignKey(Condition, on_delete=models.CASCADE, blank=True, verbose_name='Состояние')
    floor = models.CharField('Этаж/этажность', max_length=60, blank=True)
    year_construction = models.CharField('Высота потолков', max_length=60, blank=True)
    type_house = models.ForeignKey(Typehouse, on_delete=models.CASCADE, blank=True, verbose_name='Тип дома')
    rooms = models.CharField('Кол-во комнат', max_length=60, blank=True)
    announcement = models.ForeignKey(Announcement, on_delete=models.CASCADE, verbose_name='Главная информация')
    name_class = 'apartments'
    def __str__(self):
        return self.name + ' (' + str(self.announcement.typesale) + ')'

    class Meta:
        verbose_name = 'Квартиры'
        verbose_name_plural = 'Квартира'




class Plots(models.Model):
    name = models.CharField('Заголовок', max_length=60)
    announcement = models.ForeignKey(Announcement, on_delete=models.CASCADE, verbose_name='Главная информация')
    name_class = 'plots'

    def __str__(self):
        return self.name + ' (' + str(self.announcement.typesale) + ')'

    class Meta:
        verbose_name = 'Участки'
        verbose_name_plural = 'Участок'



class Commerce(models.Model):
    name = models.CharField('Заголовок (тип назначение)', max_length=60)
    condition = models.ForeignKey(Condition, on_delete=models.CASCADE, blank=True, verbose_name='Состояние')
    floor = models.CharField('Этажность здания', max_length=60, blank=True)
    announcement = models.ForeignKey(Announcement, on_delete=models.CASCADE, verbose_name='Главная информация')
    name_class = 'commerce'


    def __str__(self):
        return self.name + ' (' + str(self.announcement.typesale) + ')'

    class Meta:
        verbose_name = 'Коммерческая недвижимость'
        verbose_name_plural = 'Коммерческая недвижимость'



class Reviews(models.Model):
    name = models.CharField('Никнейм', max_length=60)
    description = models.TextField('Описание', max_length=5000, blank=True)
    photo = models.ImageField('Фото', upload_to='photos', blank=True)
    video = models.FileField('Видео', upload_to='videos', blank=True)
    date = models.DateField('Дата')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Отзывы'
        verbose_name_plural = 'Отзывы'
