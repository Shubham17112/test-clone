



from django.contrib import admin
 
# Register your models here.
from .models import Category,Event, EventDetail
 
admin.site.register(Event)
 
admin.site.register(Category)
admin.site.register(EventDetail)
