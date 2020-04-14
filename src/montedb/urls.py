from django.urls import path
from .views import AdultsView, ChildrenView, ParentFeeView

app_name = 'montedb'

urlpatterns = [
    path('children/', ChildrenView.as_view(), name='child-list'),
    path('adults/', AdultsView.as_view(), name='adult-list'),
    path('fee/<int:pk>/', ParentFeeView.as_view(), name='parent-fee')
]