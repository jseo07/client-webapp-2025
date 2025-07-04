from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("contact/", views.contact_page, name="contact_page"),
    path("about/", views.about, name="about"),
    path("services/", views.services, name="services"),
    path("sample_service/", views.sample_service, name="sample_service"),
    path("home_control/", views.home_control, name="home_control"),
    path("security/", views.security, name="security"),
    path("window/", views.window, name="window"),
    path("theater/", views.theater, name="theater"),
    path("lighting/", views.lighting, name="lighting"),
]
