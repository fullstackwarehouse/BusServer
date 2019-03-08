from django.urls import path
from django.conf.urls import url
# from . import views
from .views import (
    HomePageView,
)
urlpatterns = [
    # path('', views.HomePageView.as_view(), name='home'),
    url(r'^$', HomePageView.as_view(), name='home'),
]
