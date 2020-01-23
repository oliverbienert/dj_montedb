from django.urls import path
from .views import AdultsView, ChildrenView

app_name = 'montedb'

urlpatterns = [
    path('children/', ChildrenView.as_view(), name='child-list'),
    path('adults/', AdultsView.as_view(), name='adult-list'),
]