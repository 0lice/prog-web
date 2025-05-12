from django.urls import path
from loja.views.homeview import home_view
urlpatterns = [
    path('', home_view),
]
