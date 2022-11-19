from django.urls import path
from api.views import (
    ItemDetailPageView,
    BuyItemSessionView,
    SuccessView,
    CancelView
)


urlpatterns = [
    path('item/<int:item_id>/', ItemDetailPageView.as_view(), name='item-detail'),
    path('buy/<int:pk>/', BuyItemSessionView.as_view(), name='buy-item-session'),
    path('success/', SuccessView.as_view(), name='success'),
    path('cancel/', CancelView.as_view(), name='cancel'),
]