from django.urls import path
from index.views import index, email


urlpatterns = [
    path('', index, name='index'),
    path('send_email/', email, name='send_email'),
]
