from django.urls import path, include
from .views import home, definition, ModLoginView, sign_up, log_out

urlpatterns = [
    path('', home, name='home'),
    path('home', home, name='home'),
    path('search/<str:search_query>/', definition, name='definition'),
    path('login/', ModLoginView.as_view(), name='login'),
    path('log-out/', log_out, name='logout'),
    path('sign-up/', sign_up, name='sign_up'),
    path('', include('django.contrib.auth.urls'))
]
