from django.urls import path
from .views import AdultsView, AdultCreate, AdultUpdate, AdultDelete, ChildrenView, ChildCreate, ChildUpdate, ChildDelete

urlpatterns = [
    path('children/', ChildrenView.as_view(), name='child-list'),
    path('child/add/', ChildCreate.as_view(), name='child-add'),
    path('child/<int:pk>/', ChildUpdate.as_view(), name='child-update'),
    path('child/<int:pk>/delete/', ChildDelete.as_view(), name='child-delete'),
    path('adults/', AdultsView.as_view(), name='adult-list'),
    path('adult/add/', AdultCreate.as_view(), name='adult-add'),
    path('adult/<int:pk>/', AdultUpdate.as_view(), name='adult-update'),
    path('adult/<int:pk>/delete/', AdultDelete.as_view(), name='adult-delete'),
]