from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('updated/<str:pk>/',views.update_task,name='updated'),
    path('delete/<str:pk>/',views.delete_task,name='update_task')
    
]