from django.urls import path

# import views file from same level
from .import views


urlpatterns = [
    path('', views.index, name="index"),
    path('<int:course_id>', views.detail, name="detail")
]
