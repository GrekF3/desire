from django.urls import path
from .views import index, about, blog, gallery, contacts, BlogConent


urlpatterns = [
    path('', index, name='home'),
    path('about/',about, name='about'),
    path('blog/', blog, name='blog'),
    path('gallery/', gallery, name='gallery'),
    path('contact/', contacts, name='contacts'),
    path('blog/post',BlogConent, name='post')
]
