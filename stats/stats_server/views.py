from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect

def stats(request):
    return HttpResponse("Users stats")

def main(request):
    return HttpResponse("main site")

def create_user(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = UserCreationForm()
    
    return render(request, 'create_user.html', {'form': form})

