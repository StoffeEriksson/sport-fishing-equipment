from django.contrib import admin
from .models import Like, Rating, Comment


@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    list_display = ('user', 'product', 'liked_at')
    list_filter = ('liked_at',)
    search_fields = ('user__username', 'product__name')


@admin.register(Rating)
class RatingAdmin(admin.ModelAdmin):
    list_display = ('user', 'product', 'score', 'rated_at')
    list_filter = ('score', 'rated_at')
    search_fields = ('user__username', 'product__name')


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('user', 'product', 'created_at', 'short_content')
    list_filter = ('created_at',)
    search_fields = ('user__username', 'product__name', 'content')
    ordering = ('-created_at',)
    actions = ['delete_selected']

    def short_content(self, obj):
        return obj.content[:50] + "..." if len(
            obj.content) > 50 else obj.content
    short_content.short_description = 'Content Preview'
