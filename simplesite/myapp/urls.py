from django.urls import path
from . import views

app_name = "myapp"

urlpatterns = [
    path('', views.fleat, name="fleat")
]