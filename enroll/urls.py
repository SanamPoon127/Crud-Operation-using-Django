from django.urls import path
from enroll import views

urlpatterns = [
    path('', views.add_show, name= "addandshow"),
    path('', views.add_show, name='addandshow'),
    path('delete/<int:id>/', views.delete_data, name="deletedata"), # Delete data by ID
    path ('update<int:id>/', views.update_data, name="updatedata"), # Update data by ID
]