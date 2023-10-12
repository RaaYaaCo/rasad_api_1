from django.urls import path
from . import views

app_name = 'product'
urlpatterns = [
    path('type/', views.ProductTypeView.as_view(), name='product-type'),
    path('type/detail/<int:id>', views.ProductTypeDetailView.as_view(), name='product-type-detail'),
    path('degree/', views.DegreeView.as_view(), name='degree'),
    path('degree/detail/<int:id>', views.DegreeDetailView.as_view(), name='degree-detail'),
    path('unit/', views.UnitView.as_view(), name='unit'),
    path('unit/detail/<int:id>', views.UnitDetailView.as_view(), name='unit-detail'),
    path('add/', views.ProductView.as_view(), name='product'),
    path('detail/<int:id>', views.ProductDetailView.as_view(), name='product-detail'),
]