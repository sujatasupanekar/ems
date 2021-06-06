from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from django.contrib.auth.views import PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView,PasswordResetCompleteView
from django.conf.urls import handler404, handler500, handler403, handler400
from django.contrib.auth import views as auth_views
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^$', views.index),
    url(r'^about$', views.about, name='about'),
    url(r'^home$', views.home, name='home'),
    url(r'^login$', views.login, name='login_page'),
    url(r'^logout/$', views.logout, name='logout'),
    url(r'^adminpage$', views.adminpage, name='adminpage'),
    url(r'^userpage$', views.userpage, name='userpage'),
    url(r'^consumption_graph',views.consumption_graph,name='consumption_graph'),
    ### URL for company
    path('addcompany',views.addcompany,name="addcompany"),
    path('showcompany', views.showcompany),
    path('editcompany/<int:id>', views.editcompany),
    path('updatecompany/<int:id>', views.updatecompany),
    path('deletecompany/<int:id>', views.destroycompany),
    ### URL for location
    path('addlocation',views.addlocation),
    path('showlocation',views.showlocation),
    path('editlocation/<int:id>', views.editlocation),
    path('updatelocation/<int:id>', views.updatelocation),
    path('deletelocation/<int:id>', views.destroylocation),
    ### URL for area
    path('addarea', views.addarea),
    path('showarea', views.showarea),
    path('editarea/<int:id>', views.editarea),
    path('updatearea/<int:id>', views.updatearea),
    path('deletearea/<int:id>', views.destroyarea),
    path('load-location/', views.load_location, name='load_location'), # AJAX
    path('roicalc',views.roicalc),
                  ### for smart meter
    url(r'addsmscreen$',views.addsmscreen,name='addsmscreen'),
    url(r'showsmscreen$',views.showsmscreen,name='showsmscreen'),
    url(r'addsmport',views.addsmport,name='addsmport'),
    url(r'showsmport',views.showsmport,name='showsmport'),
    url(r'addsmlink', views.addsmlink, name='addsmlink'),
    url(r'showsmlink', views.showsmlink, name='showsmlink'),
    url(r'addsmoverview', views.addsmoverview, name='addsmoverview'),
    url(r'showsmoverview',views.showsmoverview,name='showsmoverview'),
    url(r'sm_brand_n_manf',views.sm_brand_n_manf,name='sm_brand_n_manf'),
    url(r'sm_device_address',views.sm_device_address,name='sm_device_address'),
                ### for brand and manufacturer
    url(r'brandandmanuf$', views.brandandmanuf, name='brandandmanuf'),
    url(r'showbrandandmanuf$', views.showbrandandmanuf, name='showbrandandmanuf'),
                ## Cost center
    url(r'costarea',views.addcostarea,name='costarea'),
    url(r'showcostarea',views.showcostarea,name='showcostarea'),
    url(r'house',views.addhouse,name='house'),
    url(r'showhouse',views.showhouse,name='showhouse'),
    url(r'consumerobject',views.addconsumerobj,name='consumerobject'),
    url(r'showconsumerobject',views.showconsumerobj,name='showconsumerobject'),
            ### FOrgot password
    path(r'password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='Forgot_password/password_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="Forgot_password/password_reset_confirm.html"), name='password_reset_confirm'),
#    path(r'^reset/(?P<uidb36>[0-9A-Za-z]+)-(?P<token>.+)/$', auth_views.PasswordResetConfirmView.as_view(template_name="Forgot_password/password_reset_confirm.html"), name='password_reset_confirm'),
    path(r'reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='Forgot_password/password_reset_complete.html'), name='password_reset_complete'),
    path(r"password_reset", views.password_reset_request, name="password_reset"),
] + static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)

handler404 = 'site_ems.views.error_404'
handler500 = 'site_ems.views.server_error'
handler403 = 'site_ems.views.error_403'
handler400 = 'site_ems.views.error_400'

