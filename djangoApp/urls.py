from django.urls import path

from . import views
urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'),
    path('backlog/<backlog_id>/',views.backlog,name='backlog'),
    path('liste/', views.liste, name='liste'),
        path('statistique/', views.statistique, name='statistique'),
    path('',views.home,name='home')
    
]
