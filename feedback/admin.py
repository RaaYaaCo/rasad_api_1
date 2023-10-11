from django.contrib import admin
from .models import Rating, RatingStore, Complaint


admin.site.register(Rating)
admin.site.register(RatingStore)
admin.site.register(Complaint)