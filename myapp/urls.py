from django.urls import path
from myapp.views import getMembersView

urlpatterns = [
    path('members', getMembersView.as_view())
]