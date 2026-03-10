from django.contrib import admin
from .models import UserProfile, Order

admin.site.site_header = "Администрирование MyProject"
admin.site.site_title = "MyProject Admin"
admin.site.index_title = "Добро пожаловать в панель управления"


class OrderInline(admin.TabularInline): # Или StackedInline для вертикального вида
    extra = 1 # Количество пустых полей для добавления нормы заказов
    model = Order

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'age') # Поля, отображаемые в списке
    search_fields = ('name', 'email') # Поля для поиска по имени и email
    list_filter = ('age', ) # Фильтрация по возрасту
    ordering = ("name", ) # Сортировка по имени
    inlines = [OrderInline]
admin.site.register(UserProfile, UserProfileAdmin)
