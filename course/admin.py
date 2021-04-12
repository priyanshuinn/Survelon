from django.contrib import admin
from .models import  post_data,upload_file
# Register your models here.
admin.site.register(post_data)
admin.site.register(upload_file)