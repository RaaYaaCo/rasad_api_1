from django.urls import path, re_path
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
    re_path(r'detail/(?P<p_slug>[^/]+)/?$', views.ProductDetailView.as_view(), name='product-detail'),
    path('price/', views.ProductPriceView.as_view(), name='product-price'),
    path('price/<int:p_id>', views.EachProductPriceView.as_view(), name='product_price_history')
]
