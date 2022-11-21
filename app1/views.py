from django.shortcuts import render, HttpResponse
from .models import StudentDetail
from django.views.generic import ListView

# Create your views here.
def Response(request):
    return HttpResponse("<h1>Hello, This is the Http Response From App </h1>")

# Template Integration
def home(request):
    return render(request, 'home.html')

def contact(request):
    return render(request, 'contact.html')

def about(request):
    return render(request, 'about.html')

# Requests POST
def DataPOST(request):
    if request.method == "POST":
        val1 = int(request.POST['val1'])
        val2 = int(request.POST['val2'])
        val3 = int(request.POST['val3'])
        val4 = int(request.POST['val4'])
        val5 = int(request.POST['val5'])

        result = val1 + val2 + val3 + val4 + val5

        context = {
            'val1':val1,
            'val2':val2,
            'val3':val3,
            'val4':val4,
            'val5':val5,
            'result':result
        }
        return render(request, 'form.html', context)
    return render(request, 'form.html')

# Model Implementation

# Function Based View
# def StudentList(request):
#     students = StudentDetail.objects.all()
#     context = {
#         'object_list':students
#     }
#     return render(request, 'student_list.html', context)

# Class Based View
class StudentList(ListView):
    model = StudentDetail
    template_name = 'student_list.html'