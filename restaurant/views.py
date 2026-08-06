# from django.http import HttpResponse
from django.shortcuts import render
from django.http import Http404, HttpResponseNotFound
from .forms import BookingForm
from .models import Menu


def home(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def book(request):
    form = BookingForm()
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
    context = {'form':form}
    return render(request, 'book.html', context)

def menu(request):
    menu_date = Menu.objects.all()
    context = {'menu': menu_date}

    return render(request, 'menu.html', context)

def display_menu_item(request, pk=None):
    if pk:
        try:
            menu_item = Menu.objects.get(pk=pk)
        except Menu.DoesNotExist:
            raise Http404(f'There is no menu item with id "{pk}"')
    else:
        menu_item = ''

    return render(request, 'menu_item.html', {'menu_item': menu_item})