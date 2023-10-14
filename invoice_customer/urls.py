from django.urls import path

from . import views


app_name = 'InvoiceCustomer'
urlpatterns = [
    path('add/', views.InvoiceCustomerAddView.as_view(), name='add'),
    path('item/add/', views.InvoiceCustomerItemAddView.as_view(), name='item-add'),
    path('show/all/', views.InvoiceCustomerShowAllView.as_view(), name='show-all'),
    path('show/detail/<int:pk>/', views.InvoiceCustomerShowDetailView.as_view(), name='detail'),
    path('product-entity/update/<int:pk>/', views.ProductEntityUpdatePriceView.as_view(), name='product-entity-update'),
    path('product-entity/show/store/<int:u_store_id>/', views.ProductEntityShowStoreView.as_view(), name='product-entity-show-store'),
    path('product-entity/show/detail/<int:pk>/', views.ProductEntityDetailView.as_view(), name='product-entity-detail')
]
