from django.shortcuts import render

from TaskCategory.models import TaskCategorys
# Create your views here.

def home(request):
    data = TaskCategorys.objects.all()
    return render(request, 'home.html', {'data' : data})