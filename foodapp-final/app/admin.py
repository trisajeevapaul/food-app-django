from django.contrib import admin
from .models import Booking, MenuItem,Order,OrderItem  # ✅ Make sure Menu is imported

# Register both models (optional but good)
admin.site.register(Booking)
admin.site.register(MenuItem)
admin.site.register(Order)
admin.site.register(OrderItem)
