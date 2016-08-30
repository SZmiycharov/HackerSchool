from django.conf.urls import url
from . import views


app_name = 'store'

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^products/$', views.ProductsView.as_view(), name='products'),
    url(r'^searchdetails/$', views.SearchDetailsView.as_view(), name='searchdetails'),
    url(r'^profile/$', views.ProfileView.as_view(), name='profile'),
    url(r'^updateprofile/$', views.UpdateProfileView.as_view(), name='updateprofile'),
    url(r'^register/$', views.RegisterView.as_view(), name='register'),
    url(r'^login/$', views.LoginView.as_view(), name='login'),
    url(r'^logout/$', views.LogoutView.as_view(), name='logout'),
    url(r'^(?P<pk>[0-9a-z-]+)/$', views.DetailView.as_view(), name='detail'),

]
