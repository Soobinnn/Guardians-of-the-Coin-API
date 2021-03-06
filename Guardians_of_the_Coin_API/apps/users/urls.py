from django.urls import path
from . import views
 
app_name = 'users'
urlpatterns = [
    path('', views.UserView.as_view()),#User에 관한 API를 처리하는 view로 Request를 넘김
    path('<int:user_id>', views.UserView.as_view()) #User pk id가 전달되는 경우
]
