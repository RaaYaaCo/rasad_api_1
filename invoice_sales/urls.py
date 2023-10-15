from django.urls import path

from . import views

app_name = 'InvoiceSales'
urlpatterns = [
    path('add/', views.InvoiceSalesAddView.as_view(), name='add'),
    path('item/add/', views.InvoiceSalesItemAddView.as_view(), name='item-add'),
    path('show/all/', views.InvoiceSalesShowAllView.as_view(), name='show all'),
    path('show/detail/<int:pk>/', views.InvoiceSalesShowDetailView.as_view(), name='show-detail'),
    path('show/detail/wholesaler/<int:u_wholesaler_id>/', views.InvoiceSalesShowDetailWholesalerView.as_view(), name='detail-wholesaler'),
    path('show/detail/store/<int:u_store_id>/', views.InvoiceSalesShowDetailStoreView.as_view(), name='detail-store')
]
