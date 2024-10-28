from django.urls import path

from catches import views

urlpatterns = [
    path("new/", views.catche_new, name="catch_new"),
    path("<int:catche_id>/", views.catche_detail, name="catche_detail"),
    path("<int:catche_id>/edit/", views.catche_edit, name="catche_edit"),
]