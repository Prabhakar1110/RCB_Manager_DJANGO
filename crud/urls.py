from django.urls import path
from . import views

app_name = 'crud'

urlpatterns = [
    path('',views.list_player, name='list_player'),
    path('create/', views.create_player, name='create_player'),
    path('view/<int:pk>/', views.view_player, name='view_player'),
    path('update/<int:pk>/', views.update_player, name='update_player'),
    path('delete/<int:pk>/', views.delete_player, name='delete_player'),
    path('super_user/', views.create_super, name="create_super"),
]