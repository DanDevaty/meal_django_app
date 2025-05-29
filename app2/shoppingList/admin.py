from django.contrib import admin
from .models import ShoppingList, ShoppingListItem


class ShoppingListAdmin(admin.ModelAdmin):
    list_display = ['user', 'created_at', 'updated_at']
    search_fields = ['user__username']
    list_filter = ['created_at']

class ShoppingListItemAdmin(admin.ModelAdmin):
    list_display = ['shopping_list', 'ingredient', 'quantity', 'is_purchased']
    list_filter = ['shopping_list', 'quantity']

admin.site.register(ShoppingList, ShoppingListAdmin)
admin.site.register(ShoppingListItem, ShoppingListItemAdmin)