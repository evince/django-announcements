from django.urls import path
from django.views.generic.list import ListView

from announcements.models import Announcement
from announcements.views import *


announcement_detail_info = {
    "queryset": Announcement.objects.all(),
}

urlpatterns = [
    path('<int:object_id>/', ListView.as_view(),
        announcement_detail_info, name="announcement_detail"),
    path('<int:object_id>/hide/', announcement_hide,
        name="announcement_hide"),
    path('', announcement_list, name="announcement_home"),
]
