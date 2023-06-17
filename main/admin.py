from django.contrib import admin
from .models import Article, ArticleSeries

class ArticleSeriesAdmin(admin.ModelAdmin):
    fields = [
        'title',
        'subtitle',
        'slug',
        # 'published'
    ]

class ArticleAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Header', {'fields':['title', 'subtitle', 'article_slug','series']}),
        ('content', {'fields':['content','notes']}),
        ('Date', {'fields':['modified']})
    ]
admin.site.register(Article,ArticleAdmin)
admin.site.register(ArticleSeries, ArticleSeriesAdmin)
