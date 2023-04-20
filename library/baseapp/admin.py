from django.contrib import admin
from .models import Author, Book


# Register your models here.
# class MemberAdmin(admin.ModelAdmin):
#     list_display = ('id', 'firstname', 'lastname', 'email')
admin.site.register(Author)
admin.site.register(Book)