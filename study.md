pip install django

pip install djangorestframework

python manage.py startapp user 

settings.py에 INSTALLED_APPS에 앱을 추가 

restframework를 사용하고싶다면 rest_framework도 추가

python manage.py makemigrations 

----
### 실행

python manage.py runserver

### 시작

setting.py INSTALLED_APPS에 새로운app 경로 추가

새로운app/apps.py 수정 
ex) name = 'Guardians_of_the_Coin_API.apps.coins'

