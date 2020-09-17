from django.urls import path, include
from users.views import RegisterView, LoginView, test

urlpatterns = [
    path('register/', RegisterView.as_view()),
    path('login/', LoginView.as_view(), name='login'),
    path('test/', test, name='test'),
]
