from django.db import models
from django.contrib.auth.models import  AbstractUser
from django.core.exceptions import ValidationError

def validate_length(value,length=9):
    if value.isdigit():
        if len(str(value))!=length:
            raise ValidationError(f"Ошибка: Номер должен содержать {length} цифр.")
    else:
        raise ValidationError("Ошибка: Пишите только цифры.")

class UserModel(AbstractUser):

    TOSHKENT = "Toshkent"
    TOSHKENT_V = "Toshkent_v"
    ANDIJON = "Andijon "
    BUXORO = "Buxoro"
    FARGONA = "Farg'ona"
    SIRDARYO = "Sirdaryo"
    JIZZAX = "Jizzax"
    NAMANGAN = "Namangan"
    NAVOIY = "Navoiy"
    QORAQAL = "Qoraqalpog'iston Respublikasi"
    SAMARQAND = "Samarqand"
    SURXONDARYO = "Surxondaryo"
    XORAZM = "Xorazm"
    QASHQADARYO = "Qashqadaryo"

    CITY = (
        (TOSHKENT, "Toshkent"),
        (TOSHKENT_V, "Toshkent_v"),
        (ANDIJON, "Andijon"),
        (BUXORO, "Buxoro"),
        (FARGONA, "Farg'ona"),
        (SIRDARYO, "Sirdaryo"),
        (JIZZAX, "Jizzax"),
        (NAMANGAN, "Namangan"),
        (NAVOIY, "Navoiy"),
        (QORAQAL, "Qoraqalpog'iston Respublikasi"),
        (SAMARQAND, "Samarqand"),
        (SURXONDARYO, "Surxondaryo"),
        (XORAZM, "Xorazm"),
        (QASHQADARYO, "Qashqadaryo"),


    )

    username = models.CharField(max_length=30)
    number = models.CharField(max_length=9, unique=True, validators=[validate_length])
    city = models.CharField(max_length=50, choices=CITY)
    event_date = models.DateField(blank=True, null=True)

    USERNAME_FIELD = 'number'
    REQUIRED_FIELDS = ['username']

    class Meta:
        ordering = ['-date_joined']
        verbose_name_plural = "Пользователи"


class BlacklistUser(models.Model):
    reason = models.CharField(max_length=100, blank=True, null=True)
    date = models.DateField(auto_now_add=True)
    user_id = models.OneToOneField(UserModel, on_delete=models.CASCADE)

    def __str__(self):
        return self.user_id
    
    class Meta:
        verbose_name_plural = "Черный список пользователей"
    


 