from django.conf.urls import include, url
import views

urlpatterns = [
      url(r'^$', views.show_csod, name = 'show_csods')


]

