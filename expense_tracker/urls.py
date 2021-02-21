from django.urls import path

from . import views

app_name = 'expense_tracker'
urlpatterns = [
    path('', views.index, name='index'),
    path('add_transaction/', views.add_transaction, name='add_transaction')
]
