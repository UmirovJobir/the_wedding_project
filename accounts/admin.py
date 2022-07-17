from django.contrib import admin
from .models import UserModel, BlacklistUser


@admin.register(UserModel)
class UserAdmin(admin.ModelAdmin):
    list_display = ['username', 'number']
    list_filter = ['username', 'number']
    search_fields = ['username', 'number']

@admin.register(BlacklistUser)
class BlacklistAdmin(admin.ModelAdmin):
    list_display = ['user_id', 'reason', 'date']
    search_fields = ['number']
