from django.db import models
from accounts.models import UserModel
from services.models import RestoranModel, TableModel, ServiceModel, ServiceModel, MenuModel



class Order(models.Model):
    IN_PROCESS = "In process"
    COMPLETED = "Completed"
    CANCELED = "Canceled"
    STATUS = (
        (IN_PROCESS, "In process"),
        (COMPLETED, "Completed"),
        (CANCELED, "Canceled")
    )
    user_id = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    day = models.DateField(blank=True)
    restoran_id = models.ForeignKey(RestoranModel, on_delete=models.CASCADE)
    table_id = models.ForeignKey(TableModel, on_delete=models.CASCADE)
    menu_id = models.ManyToManyField(MenuModel, blank=True)
    service_id = models.ManyToManyField(ServiceModel, blank=True)
    status = models.CharField(max_length=15, choices=STATUS, blank=True, default=IN_PROCESS)
    total_price = models.PositiveIntegerField(default=0, blank=True, null=True)

    def __str__(self):
        return str(self.user_id)

    class Meta:
         verbose_name_plural = "Заказы"

    # @property
    # def menu_price(self):
    #     menu_price = self.menu.price
    #     return menu_price


    # @property
    # def gests_price_all(self):
    #     number = int(self.menu_price) * int(self.gests_amount)
    #     return number
        

    # @property
    # def service_price(self):
    #     total_price = 0
    #     for service in self.service.all():
    #         total_price += service.price  
    #     return total_price


