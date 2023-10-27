from django.shortcuts import render
from django.views.decorators.http import require_http_methods
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from django.contrib.auth.models import User, auth

# Create your views here.
@require_http_methods(["POST", "GET"])
def LoginView(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if not user:
            messages.warning(request, "User not found")
            return HttpResponseRedirect(request.path)

        login(request, user)
        return redirect("order_list")

    if request.method == "GET":
        return render(request, "users/login.html")
    
def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        name = request.POST.get('name')
        password = request.POST.get('password')
        password_confirmation = request.POST.get('password_confirmation')
        address = request.POST.get('address')
        phone = request.POST.get('phone')
        
        if password_confirmation == password:
            if User.objects.filter(email=email).exists():
                messages.info(request, 'Email already exists')
                return redirect('user_register')
            elif User.objects.filter(username=username).exists():
                messages.info(request, 'Username already exists')
                return redirect('user_register')
            else:
                user=User.objects.create_user(username=username, email=email, password=password_confirmation, first_name=name)
                user.save()
                return redirect('user_login')
        else:
            messages.info(request, 'Password is not the same')
            return redirect('user_register')
    else:
        return render(request, 'users/register.html')

def logout_view(request):
    auth.logout(request)
    return redirect('user_login')

def profile_view(request):
    return render(request, 'users/profile.html', {'user': request.user})