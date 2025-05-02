# sondage/urls.py
from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

app_name = 'sondage'  # Namespace "sondage"

urlpatterns = [
    path('', views.survey_form, name='survey_form'),
    path('submit/', views.submit_survey, name='submit_survey'),
    path('report/', views.generate_report, name='generate_report'),
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('logout/', views.logout_view, name='logout'),
    path('admin-stats/', views.admin_stats, name='admin_stats'),
    path('admin-stats/word/', views.admin_stats_word, name='admin_stats_word'),
    path('admin-stats/pdf/', views.admin_stats_pdf, name='admin_stats_pdf'),
]

urlpatterns += staticfiles_urlpatterns()