from django.urls import path
from .views import (
    StudentListView, StudentDetailView, StudentUpdateView,
    student_create_view, student_delete_view
)

urlpatterns = [
    path('', StudentListView.as_view(), name='student_list'),
    path('student/add/', student_create_view, name='student_add'),
    path('student/<int:pk>/', StudentDetailView.as_view(), name='student_detail'),
    path('student/<int:pk>/edit/', StudentUpdateView.as_view(), name='student_edit'),
    path('student/<int:pk>/delete/', student_delete_view, name='student_delete'),
]
