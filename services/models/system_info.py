
from django.db import models
from accounts.models import UserModel

class SingletonModel(models.Model):
    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        self.pk = 1
        super(SingletonModel, self).save(*args, **kwargs)

    def delete(self, *args, **kwargs):
       self.pk = 1
       super(SingletonModel, self).delete(*args, **kwargs)

    @classmethod
    def load(cls):
        obj, created = cls.objects.get_or_create(pk=1)
        return obj

class SystemInfoModel(SingletonModel):
    title = models.CharField(max_length=40)
    description = models.TextField()
    image = models.ImageField(upload_to='info/', blank=True, null=True)

    def save(self, *args, **kwargs):
        super(SystemInfoModel, self).save(*args, **kwargs)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name_plural = "Информация o сайте"

class SystemInfoFileModel(models.Model):
    # systeminfo_id = models.ForeignKey(SystemInfoModel, on_delete=models.CASCADE)
    file = models.FileField(upload_to='gallery/', blank=True)

    def __str__(self):
        return str(self.file)


