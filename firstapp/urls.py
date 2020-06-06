from . import views
from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve

urlpatterns= [
url('hamburger/',views.Upload.as_view(),name='uploader'),
url('',views.search,name='search'),
url('genre/',views.genre,name='genre')
]
