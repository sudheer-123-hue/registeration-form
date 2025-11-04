from django.shortcuts import render
from .forms import RegistrationForm
from .models import Registration

def register_user(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()  # Save the registered user
            return render(request, 'accounts/success.html', {'user': user})
    else:
        form = RegistrationForm()
    return render(request, 'accounts/register.html', {'form': form})

