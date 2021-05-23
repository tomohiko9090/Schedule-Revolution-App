from django.urls import path
from .views import Oneteam_List, Oneteam_Create, Oneteam_Detail, Oneteam_Delete, matrixfunk, analysis, UserCsvDownloadView, barfunk, Oneteam_Table, Oneteam_Update

urlpatterns = [
    path('list/', Oneteam_List.as_view(), name='list'),
    path('create/', Oneteam_Create.as_view(), name='create'),
    path('detail/<int:pk>/', Oneteam_Detail.as_view(), name='detail'),
    path('detail/<int:pk>/matrix/', matrixfunk, name='plot'),
    path('detail/<int:pk>/aa/', UserCsvDownloadView.as_view(), name='plan'),
    path('table/<int:pk>', analysis, name='table'),
    path('list/bar/', barfunk, name='bar'),
    path('delete/<int:pk>', Oneteam_Delete.as_view(), name='delete'),
    path('update/<int:pk>', Oneteam_Update.as_view(), name='update'),
]



