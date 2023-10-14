from django.urls import path

from . import views


app_name = 'feedback'
urlpatterns = [
    path('rating/', views.RatingStoreAPIView.as_view(), name='rating'),
    path('rating/average/', views.AverageRatingStore.as_view(),name='average'),
    path('rating/show/', views.RatingShowView.as_view(), name='rating-show'),
    path('complaint/', views.ComplaintView.as_view(), name='complaint'),
    path('complaint/detail/', views.ComplaintDetailView.as_view(), name='complaint_detail'),
    path('complaint/detail/user/', views.ComplaintDetailUser.as_view(), name='complaint_detail_user'),
    path('complaint/detail/store/', views.ComplaintDetailStore.as_view(), name='complaint_detail_store'),
    path('complaint/show/', views.ComplaintDetailAPIView.as_view(), name='complaint_show'),



]