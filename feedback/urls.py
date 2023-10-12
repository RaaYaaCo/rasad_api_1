from django.urls import path

from . import views


app_name = 'feedback'
urlpatterns = [
    path('rating/', views.RatingStoreAPIView.as_view(), name='rating'),
    path('complaint/', views.ComplaintView.as_view(), name='complaint'),
    path('complaint/detail/', views.ComplaintDetailView.as_view(), name='complaint_detail'),
    path('complaint/user/', views.ComplaintDetailUser.as_view(), name='complaint_detail_user'),
    path('complaint/store/', views.ComplaintDetailStore.as_view(), name='complaint_detail_store'),

]