from django.url import path

from profiles_api import views


urlpatterns = [
    path('hello-view/', views.HelloApiView.as_view())
]
