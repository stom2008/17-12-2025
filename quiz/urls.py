from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name = "index"),
    path('quiz-page/', quiz_page, name = "quiz-page"),
    path('result/', result, name = "result"),
    path('dashboard/', dashboard, name = "dashboard"),
    path('login/', login_html, name = "login"),
    path('login-enter/', login_page, name = "login-enter"),
    path('profile/', profile, name = "profile"),
    path('logout/', logout_page, name="logout"),
]