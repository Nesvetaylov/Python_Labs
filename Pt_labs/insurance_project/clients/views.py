from django.shortcuts import render, redirect
from .models import Client
from .form import ClientForm

def add_client(request):
    if request.method == 'POST':
        form = ClientForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'clients/success.html', {'name': form.cleaned_data['name']})
    else:
        form = ClientForm()
    return render(request, 'clients/add_client.html', {'form': form})

def clients_list(request):
    clients = Client.objects.all()
    return render(request, 'clients/clients_list.html', {'clients': clients})