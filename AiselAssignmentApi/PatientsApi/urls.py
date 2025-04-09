from django.urls import path
from rest_framework_simplejwt import views as jwt_views
from . import views

urlpatterns = [
    path('token/obtain/', jwt_views.TokenObtainPairView.as_view(), name='token_create'),
    path('token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    path('user/login', views.user_login, name='user_login'),
    path('user/register', views.user_register, name='user_register'),
    path('user/all', views.user_all, name='user_all'),
    path('patients/all', views.patients_all, name='patients_all'),
    path('patients/get/<patient_id>/', views.patient_item, name='patients_item'),
    path('patients/update/<patient_id>/', views.patient_update, name='patients_update'),
    path('patients/delete/<patient_id>/', views.patient_delete, name='patients_delete'),
    path('patients/new/', views.patient_new, name='patients_new')
]
