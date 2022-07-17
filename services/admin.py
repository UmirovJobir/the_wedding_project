from ast import Or
from pyexpat import model
from django.contrib import admin
from services.models.system_info import SystemInfoModel, SystemInfoFileModel
from services.models.service import ServiceModel, Category, MenuModel
from services.models.restoran import TableModel, RestoranModel, BookedDate, EvantModel
from services.models.order import Order
from django.contrib.auth.models import Group

import nested_admin


admin.site.unregister(Group)


class SystemInfoFileInline(nested_admin.NestedStackedInline):
    model = SystemInfoFileModel
class SystemInfoAdmin(nested_admin.NestedModelAdmin):
    inlines = [SystemInfoFileInline,]
admin.site.register(SystemInfoModel, SystemInfoAdmin)

admin.site.register(EvantModel)

admin.site.register(RestoranModel)
admin.site.register(TableModel)
admin.site.register(BookedDate)

admin.site.register(MenuModel)

class ServicesInline(nested_admin.NestedStackedInline):
    model = ServiceModel
class CategoryAdmin(nested_admin.NestedModelAdmin):
    inlines = [ServicesInline,]
admin.site.register(Category, CategoryAdmin)

admin.site.register(Order)
