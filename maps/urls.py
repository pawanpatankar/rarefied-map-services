from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('forum/', views.forum, name='forum'),
    path('departments/', views.departments_list, name='departments_list'),
    path('department/<int:department_id>/', views.department_detail, name='department_detail'),
    path('category/<int:category_id>/', views.category_detail, name='category_detail'),
    path('map/<int:map_id>/', views.map_viewer, name='map_viewer'),
    path('map/<int:map_id>/file/', views.serve_map_file, name='serve_map_file'),
]
