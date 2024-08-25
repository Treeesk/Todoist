from django.urls import path
from . import views

app_name = 'todoist'

urlpatterns = [
    path('', views.index, name='index'),
    path('add', views.add, name='add'),
    path('delete/<int:today_id>/', views.delete, name='delete'),
    path('update/<int:today_id>/', views.update, name='update'),
    path('edit/<int:today_id>/', views.edit, name='edit'),
    path('close/<int:today_id>/',views.close, name='close'),
]