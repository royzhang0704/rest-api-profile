from django.urls import path
from . import views
urlpatterns = [
    path('hello-api/',views.HelloApiView.as_view())
]
