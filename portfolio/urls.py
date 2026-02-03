from django.urls import path
from portfolio import views

app_name = 'portfolio'
urlpatterns = [
    path('', views.Homepage.as_view(), name='homepage'),
    path('about-me/', views.AboutMe.as_view(), name='about-me'),
    path('resume/', views.Resume.as_view(), name='resume'),
    path('projects/', views.Projects.as_view(), name='projects'),
    path('blog/', views.Blog.as_view(), name='blog'),
]
