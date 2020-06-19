from django.contrib import admin
from .models import Order, OrderLineItem


class OrderLineItemAdminInline(admin.TabularInline):
    model = OrderLineItem
    readonly_fields = ("lineitem_total",)


class OrderAdmin(admin.ModelAdmin):
    inlines = (OrderLineItemAdminInline,)
    readonly_fields = (
        "order_number",
        "date",
        "delivery_cost",
        "order_total",
        "grand_total",
        "original_basket",
        "stripe_pid",
    )
    fields = (
        "order_number",
        "date",
        "full_name",
        "email",
        "phone_number",
        "country",
        "postcode",
        "post_town",
        "address_1",
        "address_2",
        "county",
        "delivery_cost",
        "order_total",
        "grand_total",
        "original_basket",
        "stripe_pid",
    )
    list_display = (
        "order_number",
        "date",
        "full_name",
        "delivery_cost",
        "order_total",
        "grand_total",
    )
    ordering = ("-date",)


admin.site.register(Order, OrderAdmin)
