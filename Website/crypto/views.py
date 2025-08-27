from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.http import HttpResponse
def home(request):
    return render(request, "home.html")
def login(request):
   return render(request, "login.html")
def signup(request):
   if request.method == "POST":
       name = request.POST.get("name")
       email = request.POST.get("email")
       message = request.POST.get("message")
       send_mail(
          subject = f"Hello {name}, Am from ISCC",
          from_email = email,
          message = message,
          recipient_list = ["bash@gmail.com","isaac@gmail.com"],
          fail_silently = False,
          )
       return redirect('home')
   return render(request, "signup.html")
def dashboard(request):
   #email = request.session.get("email", None)
   data = {"email":"Bash"}
   return render(request, "dashboard.html", data)
def about(request):
   return render(request, "dashboard.html")
def contact(request):
   pass
