from django.contrib import admin

from art_gallery_web.gallery_app.models import Arts, Post


class ArtAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'created_by')
    list_filter = ('created_by', 'price')


class PostAdmin(admin.ModelAdmin):
    list_display = ('name', 'text', 'art', 'created_on', 'email')
    list_filter = ('art', 'created_on')
    search_fields = ('name', 'email', 'text')


admin.site.register(Arts, ArtAdmin)
admin.site.register(Post, PostAdmin)
