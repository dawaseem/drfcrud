from django.urls import path
from . import views

urlpatterns = [
    path('all_students/', views.all_students, name="all_students"),
    path('add_student/', views.add_student, name='add_student'),
    path('student_details/<int:id>/', views.student_details, name='student_details'),
    path('delete_student/<str:pk>/', views.delete_student, name='delete_student')
]