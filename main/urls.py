from django.urls import path
from . import views

app_name = "main"

urlpatterns = [
    path('', views.veganai, name="veganai"),
    # path('dovanos/', views.dovanos, name="dovanos"),
    # path('test/', views.test, name="test"),
    # path('mamytes/', views.mamytes, name="mamytes"),
    # path('vilnius/', views.vilnius, name="vilnius"),
    # path('kaunas/', views.kaunas, name="kaunas"),
    
    # path("success", views.success),
]
