from django.urls import path
from . import views

app_name = "main"

urlpatterns = [
    path('', views.homepage, name="homepage"),
    path('test/', views.test, name="test"),
    
    # path("success", views.success),
]
