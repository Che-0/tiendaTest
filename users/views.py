import django
from django.shortcuts import redirect, render
from django.http import HttpResponse
from  .forms import RegisterForm
from django.contrib import messages
from django.contrib.auth import logout

# Create your views here.
def register(request):
    
    form = RegisterForm(request.POST or None)
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('users:login')
    return render(request, 'users/register.html', {'form': form})

def logout_view(request):
    logout(request)
    return render(request, 'users/logout.html', {'message': 'You have been logged out.'})