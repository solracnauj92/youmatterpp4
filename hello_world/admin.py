from django.contrib import admin
from .models import Post, Comment

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created_on', 'status') 
    list_filter = ('author', 'created_on', 'status') 

    fieldsets = (
        ('Basic Information', {
            'fields': ('title', 'slug', 'author', 'featured_image', 'content')
        }),
        ('Publication Information', {
            'fields': ('created_on', 'status', 'excerpt', 'updated_on')
        }),
    )

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('post', 'author', 'created_on', 'approved', 'published_date')
    list_filter = ('post', 'author', 'approved', 'created_on')
    
    fieldsets = (
        ('Basic Information', {
            'fields': ('post', 'author', 'body')
        }),
        ('Status Information', {
            'fields': ('approved', 'created_on', 'published_date')
        }),
    )