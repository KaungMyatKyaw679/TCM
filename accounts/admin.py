from django.contrib import admin
from . import models;
# Register your models here.
admin.site.register(models.Feed)
admin.site.register(models.Writer)
admin.site.register(models.Book)

