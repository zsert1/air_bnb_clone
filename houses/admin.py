from django.contrib import admin
from .models import House


@admin.register(House)
class HouseAdmin(admin.ModelAdmin):
   list_display=[
      "name",
      "price_per_night",
      "address",
      "pets_allow"
   ]
   list_filter=["price_per_night",'pets_allow']
   search_fields=["address"]
   list_display_links=("name","address")
   list_editable=("pets_allow",)