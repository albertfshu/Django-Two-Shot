from django.urls import path
from accounts.views import login_user, logout_view, signup

urlpatterns = [
    path("login/", login_user, name="login"),
    path("logout/", logout_view, name="logout"),
    path("signup/", signup, name="signup"),
]
