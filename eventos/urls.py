from django.urls import path
from . import views
urlpatterns = [
    path('', views.page_eventos, name='eventos'),
]