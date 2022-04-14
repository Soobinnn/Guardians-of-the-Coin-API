from django.urls import path
from . import views
 
app_name = 'coins'
urlpatterns = [
    path('', views.CoinView.as_view()),
    path('recommend', views.CoinRecommendView.as_view()),
    path('rsi', views.CoinRSIView.as_view()),
]
