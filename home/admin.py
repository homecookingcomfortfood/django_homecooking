from django.contrib import admin
from home.models import Contact
from home.models import smoothie
from home.models import receipe
from home.models import frontimage
# Register your models here.

admin.site.register(Contact)
admin.site.register(smoothie)
admin.site.register(receipe)
admin.site.register(frontimage)