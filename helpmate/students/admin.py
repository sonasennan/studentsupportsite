from django.contrib import admin
from students.models import Notes,Questionpapers,CustomUser
# Register your models here.
admin.site.register(Notes)
admin.site.register(Questionpapers)
admin.site.register(CustomUser)
