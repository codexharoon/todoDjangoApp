from django.urls import path
from . import views

urlpatterns = [
    path('',views.login,name='login'),
    path('signup',views.signup,name='signup'),
    path('todo',views.todo,name='todo'),
    path('logout',views.logout,name='logout'),
    path('edit/<str:pk>/',views.edit,name='edit'),
    path('delete/<str:pk>/',views.delete,name='delete'),
]