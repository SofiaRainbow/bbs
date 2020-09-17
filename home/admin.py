from django.contrib import admin
from home.models import CategoryModel, ArticleModel, Reply
from modeltranslation.admin import TranslationAdmin


class CategoryModelAdmin(TranslationAdmin):
    list_display = ['name']


class ArticleModelAdmin(TranslationAdmin):
    list_display = ['title', 'content']


class ReplyAdmin(TranslationAdmin):
    list_display = ['r_content']


admin.site.register(CategoryModel, CategoryModelAdmin)
admin.site.register(ArticleModel, ArticleModelAdmin)
admin.site.register(Reply, ReplyAdmin)
