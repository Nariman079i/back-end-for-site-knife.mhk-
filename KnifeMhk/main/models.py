from django.db import models

class Knife(models.Model):
    article = models.IntegerField('Артикул')
    title = models.CharField('Наименование' , max_length=50 , default="Knife")
    img = models.ImageField('Изображение' ,upload_to='img/' ,null=False)
    description = models.TextField('Описание' , null=True)
    price = models.IntegerField('Стоимость' , null=False)
    type_id = models.ForeignKey('Type' , on_delete=models.CASCADE)

class Type(models.Model):
    slug = models.CharField( max_length=50)
    title = models.CharField("Название" ,max_length=50)
