from django.db import models

from services.models.restoran import EvantModel

class Category(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name
    
    class Meta:
         verbose_name_plural = "Услуги" # "Категория услуг"

class ServiceModel(models.Model):
    event_type_id = models.ForeignKey(EvantModel, on_delete=models.CASCADE)
    category_type_id = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    type = models.CharField(max_length=30)
    price = models.PositiveIntegerField(default=0)
    image = models.ImageField(upload_to='service/', blank=True, null=True)
    file = models.FileField(upload_to='service/', blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return str(self.category_type_id)
    
    # class Meta:
    #     verbose_name_plural = "Услуги"


class MenuModel(models.Model):
    event_id = models.ForeignKey(EvantModel, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    type = models.CharField(max_length=30)
    price = models.PositiveIntegerField(default=0)
    image = models.ImageField(upload_to='service/', blank=True, null=True)

    def __str__(self):
        return str(self.name)

    class Meta:
        verbose_name_plural = "Меню"