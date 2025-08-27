from django.urls import path
from . import views
urlpatterns = [
   path("", views.home, name="home"),
   path("login/", views.login, name="login"),
   path("dashboard/", views.dashboard, name="dashboard"),
   #path("logout/", views.login, name="login"),
   path("contact/", views.contact, name="contact"),
   path("signup/", views.signup, name="signup"),
   path("about/", views.about, name="about")
]

