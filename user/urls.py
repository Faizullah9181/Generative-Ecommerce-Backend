from django.urls import path
from . import views


urlpatterns = [
    path('login/', views.MyTokenObtainPairView.as_view(),
         name='token_obtain_pair'),
    path('register/', views.registerUser, name='register'),

]
