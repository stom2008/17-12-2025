from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name = "index"),
    path('quiz-page/', quiz_page, name = "quiz-page"),
    path('result/', result, name = "result"),
    path('dashboard/', dashboard, name = "dashboard"),
    path('login/', login, name = "login "),
    path('profile/', profile, name = "profile"),
]