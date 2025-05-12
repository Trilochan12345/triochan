from django.contrib import admin
from .models import Student

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('student_name', 'student_class', 'admission_date', 'created_at', 'deleted_at')
    list_filter = ('student_class', 'deleted_at')
