from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.add_person, name='add_person'),
    path('', views.persons_list, name='persons_list'),
    path('give_points/<int:student_id>/', views.give_points, name='give_points'),
    path('view_points/<int:student_id>/', views.view_points, name='view_points'),
    path('schedule/<str:faculty>/', views.view_schedule, name='schedule'),
    path('students/', views.persons_list, name='persons_list'),
    path('dishes/', views.dish_list, name='dish_list'),
    path('dishes/add/', views.add_dishes, name='add_dishes'),
    path('students/', views.persons_list, name='persons_list'),
    path('students/remove/<int:student_id>/', views.remove_person, name='remove_person'),
    path('dishes/', views.dish_list, name='dish_list'),
    path('dishes/add/', views.add_dishes, name='add_dishes'),
    path('create_order/', views.create_order, name='create_order'),
    path('view_orders/', views.view_orders, name='view_orders'),
    
]
