from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

urlpatterns = [
                  path('', views.home, name='home'),
                  path('signup/patient/', views.patient_signup, name='patient_signup'),
                  path('signup/doctor/', views.doctor_signup, name='doctor_signup'),
                  path('login/', views.login_view, name='login'),
                  path('dashboard/patient/', views.patient_dashboard, name='patient_dashboard'),
                  path('dashboard/doctor/', views.doctor_dashboard, name='doctor_dashboard'),
                  path('logout/', views.logout_view, name='logout'),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)+static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

