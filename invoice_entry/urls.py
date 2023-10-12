from django.urls import path

from . import views

app_name = 'InvoiceEntry'
urlpatterns = [
    path('add/', views.InvoiceEntryAddView.as_view(), name='add'),
    path('item/add/', views.InvoiceEntryItemAddView.as_view(), name='item-add'),
]
