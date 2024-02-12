from django.urls import path
from app import views
from django.contrib.auth import views as auth_views

urlpatterns=[
        path("", views.index, name="index"),
        path("register", auth_views.LoginView.as_view(template_name='register.html'), name='register'),
        path("index", views.index, name="index"),
        path("waterreq", views.waterreq, name="waterreq"),
        path("complaint", views.complaint, name="complaint"),
        path("report", views.report, name="report"),
        path("contact", views.contact, name="contact"),
        path("addData", views.addData, name="addData"),
        path("dataa", views.dataa, name="dataa"),
        path("datum", views.datum, name="datum"),
        ]