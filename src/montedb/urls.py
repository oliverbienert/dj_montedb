from django.urls import path
from .views import ChildrenView, ChildCreate, ChildUpdate, ChildDelete


urlpatterns = [
    path('children/', ChildrenView.as_view(), name='child-list'),
    path('child/add/', ChildCreate.as_view(), name='child-add'),
    path('child/<int:pk>/', ChildUpdate.as_view(), name='child-update'),
    path('child/<int:pk>/delete/', ChildDelete.as_view(), name='child-delete'),
]