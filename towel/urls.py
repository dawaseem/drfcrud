from django.urls import path
from . import views

urlpatterns = [
    path('all_students/', views.all_students, name="all_students"),
    path('add_student/', views.add_student, name='add_student'),
    path('student_detail/<int:pk>/', views.student_detail, name='student_detail'),
    path('update_student/<int:pk>/', views.update_student, name='update_student'),
    path('delete_student/<int:pk>/', views.delete_student, name='delete_student')
]