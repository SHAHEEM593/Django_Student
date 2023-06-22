from django.shortcuts import render,redirect
from . forms import StudentForm
from .models import Student
def student_form(request):
    if request.method == 'POST':
        form = StudentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('student_list')
    else:
        form = StudentForm()
    
    return render(request, 'forms.html', {'form': form})

def student_list(request):
    students=Student.objects.all()
    context={
        'students':students
    }    
    return render(request,'student_list.html',context)