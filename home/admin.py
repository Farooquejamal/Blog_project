from django.contrib import admin
from .models import BlogModel,Category,Profile,Comment
# Register your models here.
admin.site.register(BlogModel)
admin.site.register(Category)
admin.site.register(Profile)
admin.site.register(Comment)

