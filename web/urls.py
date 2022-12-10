from django.urls import path,include
from . import views
urlpatterns = [
    path('',views.index),
    path('upload-link',views.getLink)
]
