from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, UpdateView, DetailView
from django.urls import reverse_lazy
from .models import Student
from .forms import StudentForm
from django.utils import timezone

# ListView (only non-deleted students)
class StudentListView(ListView):
    model = Student
    template_name = 'student_list.html'
    context_object_name = 'students'

    def get_queryset(self):
        return Student.objects.filter(deleted_at__isnull=True)

# DetailView
class StudentDetailView(DetailView):
    model = Student
    template_name = 'student_detail.html'
# UpdateView
class StudentUpdateView(UpdateView):
    model = Student
    form_class = StudentForm
    template_name = 'student_form.html'
    success_url = reverse_lazy('student_list')

# Soft Delete View
def student_delete_view(request, pk):
    student = get_object_or_404(Student, pk=pk)
    student.deleted_at = timezone.now()
    student.save()
    return redirect('student_list')

def student_create_view(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()  # Save the new student to the database
            return redirect('student_list')  # Redirect to the student list page after saving
    else:
        form = StudentForm()  # Initialize the empty form

    return render(request, 'student_form.html', {'form': form})