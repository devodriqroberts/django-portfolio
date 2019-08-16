from django.urls import path
from .views import HomeTemplateView, redirect_portfolio

urlpatterns = [
    path('', redirect_portfolio),
    path('portfolio', HomeTemplateView.as_view()),
    # path('about-me', AboutTemplateView.as_view()),
]
