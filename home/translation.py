from modeltranslation.translator import translator, TranslationOptions

from home.models import CategoryModel, ArticleModel, Reply


class CategoryModelTranslationOptions(TranslationOptions):
    fields = ('name',)


class ArticleModelTranslationOptions(TranslationOptions):
    fields = ('title', 'content')


class ReplyTranslationOptions(TranslationOptions):
    fields = ('r_content',)


translator.register(CategoryModel, CategoryModelTranslationOptions)
translator.register(ArticleModel, ArticleModelTranslationOptions)
translator.register(Reply, ReplyTranslationOptions)
