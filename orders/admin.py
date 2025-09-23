from django.contrib import admin
from .models import Order, OrderItem


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    raw_id_fields = ['product']


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'last_name', 'email', 'phone', 'city', 'status', 'created_at', 'get_total_cost']
    list_filter = ['status', 'created_at', 'updated_at']
    inlines = [OrderItemInline]
    search_fields = ['first_name', 'last_name', 'email', 'phone']
    list_editable = ['status']
    
    def get_total_cost(self, obj):
        return f"{obj.get_total_cost():,.0f} VND"
    get_total_cost.short_description = 'Tổng tiền'
