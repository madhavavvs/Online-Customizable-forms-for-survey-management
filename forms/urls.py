from django.conf.urls import include
from django.contrib.auth import views
from django.contrib import admin
from django.urls import path
from forms.survey import views as survey_views


urlpatterns = [
	path('admin/',admin.site.urls),
    path('', survey_views.main, name='main'),
    path('login/', views.LoginView.as_view(),{'template_name': 'registration/login.html'}, name='login'),
    path('logout/', survey_views.logout_request, name='logout'),
    path('signup/', survey_views.signup, name='signup'),
    path('home/', survey_views.home, name='home'),
    path('password/', survey_views.password, name='password'),
	  path('createform/', survey_views.create, name="createform"),    
	  path('formlist/', survey_views.formlist, name= "formlist"),
   	path('displayform/<pk>', survey_views.displayform, name="displayform"),
   	path('answer/<pk>', survey_views.answer, name="answer"),
    path('question/<pk>',survey_views.question, name="question"),
    
]

