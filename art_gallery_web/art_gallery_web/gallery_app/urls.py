from django.urls import path

from art_gallery_web.gallery_app.views import list_arts, details_arts, create_art, delete_art, edit_art

urlpatterns = [
    path('', list_arts, name="list arts"),
    path('details/<int:pk>', details_arts, name='details arts'),
    path('create/', create_art, name='create art'),
    path('delete/<int:pk>', delete_art, name='delete art'),
    path('edit/<int:pk>', edit_art, name='edit art'),
]

