from django.http import HttpResponse
from django.shortcuts import render
from .forms import CalendarForm

# Create your views here.

def index(request):
    form = CalendarForm()
    return render(request, 'ptpud03/index.html', {'form': form})

def calendar(request):
    if request.method == 'GET':
        form = CalendarForm(request.GET)
        if form.is_valid():
            return render(request, 'ptpud03/calendar.html')
        else:
            return render(request, 'ptpud03/index.html', {'form': form})
    return HttpResponse(status=400)


