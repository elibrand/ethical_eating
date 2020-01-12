from django.contrib import admin

# Register your models here.
from resources.models import Questions, Book, Restaurant, Review, Question, Answer

admin.site.register(Questions)
admin.site.register(Book)
admin.site.register(Restaurant)
admin.site.register(Review)
admin.site.register(Question)
admin.site.register(Answer)