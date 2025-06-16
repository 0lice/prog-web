from django.urls import path
from loja.views.produtoview import list_produto_view
urlpatterns = [
    path('', list_produto_view, name= 'produto'),
    path('<int:id>', list_produto_view, name= 'produto'),
]
