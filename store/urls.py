from django.urls import path

from . import views


app_name = 'store'

urlpatterns = [
    path('', views.StoreView.as_view(), name='store'),
    path('search/', views.StoreSearchView.as_view(), name='search_store'),
    path('detail/(?P<s_slug>[^/]+)/?$', views.StoreDetailView.as_view(), name='store_detail')
]
