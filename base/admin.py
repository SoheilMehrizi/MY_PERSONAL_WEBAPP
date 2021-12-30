from django.contrib import admin

from base.models import AboutMe, Academy, Economy, Experiences, ToDoer, contact, specialities

# Register your models here.
admin.site.register(AboutMe)
admin.site.register(specialities)
admin.site.register(Experiences)
admin.site.register(Academy)
admin.site.register(contact)
admin.site.register(Economy)
admin.site.register(ToDoer)