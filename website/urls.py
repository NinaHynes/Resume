
from django.urls import path
from .views import index, portfolio_details, django_filters, thank_you

urlpatterns = [
    path("", index, name='website_index'),
    path("portfolio-details/", portfolio_details, name='website_portfolio-details'),
    path("filters/", django_filters, name='website_django_filter'),
    path('thank_you/', thank_you, name='website_thank_you'),
]


