from django.contrib import admin

from reviews.models import Category, Comment, Genre, Review, Title, TitleTwo

admin.site.register(Category)
admin.site.register(Genre)
admin.site.register(Title)
admin.site.register(TitleTwo)
admin.site.register(Review)
admin.site.register(Comment)
