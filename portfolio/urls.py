from django.urls import path
from portfolio import views

urlpatterns = [
    path(
        '',
        views.Homepage.as_view(),
        name='home',
    )
]