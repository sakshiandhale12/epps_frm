from django.urls import path
from .views import *


urlpatterns = [
    path('api/',DummyApi.as_view(), name='master'),

]