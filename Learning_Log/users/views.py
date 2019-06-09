from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.forms import UserCreationForm


# Create your views here.
def logout_view(request):
    """Logs the user out"""
    logout(request)
    return HttpResponseRedirect(reverse('learning_logs:index'))


def register(request):
    """Registers a new user in the database"""
    if request.method != 'POST':
        # Displays the blank registration form
        form = UserCreationForm()
    else:
        # Process the completed form
        form = UserCreationForm(data=request.POST)

        if form_is.valid():
            new_user = form.save()
            # Log the user in and redirect to home page
            authenticated_user = authenticate(username=new_user.username,
                                              password=request.POST['password'])
            login(request, authenticated_user)
            return HttpResponseRedirect(reverse('learning_logs:index'))

    context = {'form': form}
    return render(request, 'users/register.htm;', context)
