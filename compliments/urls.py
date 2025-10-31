from django.urls import path
from .views import home, get_random_compliment, share_compliment, view_shared

urlpatterns = [
    path('', home, name='home'),
    path('get-compliment/', get_random_compliment, name='get_compliment'),
    path('share/<uuid:compliment_id>/', share_compliment, name='share_compliment'),
    path('shared/<uuid:share_id>/', view_shared, name='view_shared'),
]
