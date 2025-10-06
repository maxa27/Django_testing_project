from django.contrib import admin
from django.contrib.auth.models import Group
from .models import Post, Category, Location

admin.site.site_header = 'Блог'
admin.site.site_title = 'Блог'
admin.site.index_title = 'Не задано'

admin.site.register(Post)
admin.site.register(Category)
admin.site.register(Location)

try:
    admin.site.unregister(Group)
except:
    pass
