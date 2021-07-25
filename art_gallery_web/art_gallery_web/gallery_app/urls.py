from django.urls import path

from art_gallery_web.gallery_app.views import main_page#, about_page

urlpatterns = [
    path('', main_page, name='index'),
    #path('about/', about_page, name='about page'),
]