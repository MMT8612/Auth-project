"""authProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url

from loginPage.views import login_view,signUp_view,signup_form_submission,success_page,login_form_submission

app_name="loginPage"

urlpatterns = [
	url(r'^login/',login_view,name='login'),
	url(r'^signUp/',signUp_view,name='signup'),
    url(r'^signup_form_submission$',signup_form_submission,name='signup_form_submission'),
    url(r'^login_form_submission$',login_form_submission,name='login_form_submission'),
    url(r'^success_page$',success_page,name='success_page'),

]
