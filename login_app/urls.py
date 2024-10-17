from django.urls import path
from login_app.views import test_logout , test_signup ,test_login ,additional_info_profile



urlpatterns = [
    path('login/', test_login,name="login"),
    path('logout/', test_logout,name="logout"),
    path('signup/', test_signup,name="signup"),
    path('profile/', additional_info_profile , name= "profile"),
    path('', test_login,name="welcome"),
]

