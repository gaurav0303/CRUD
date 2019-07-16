from django.contrib import admin
from .models import BookList


class BookLis(admin.ModelAdmin):
	list_display=('title','price','author')





admin.site.register(BookList,BookLis)
