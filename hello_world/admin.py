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