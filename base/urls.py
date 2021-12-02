from django.urls import path
from . import views


urlpatterns = [
    path("", views.home, name="home"),
    path("about-us/", views.about, name="about"),
    path("our-services/",views.services, name="services"),
    path("contact-us/",views.contact, name="contact"),
    path("subscribe/",views.subscribe, name="subscribe"),
    path("send-message/",views.sendMessage, name="send_message"),
]
