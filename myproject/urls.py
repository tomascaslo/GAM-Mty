from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
	(r'^$', 'gammty.views.index'),

    (r'^nosotros/quienessomos', 'gammty.views.quienes_somos_vista'),
    (r'^nosotros/historia', 'gammty.views.historia_vista'),
    (r'^nosotros/escuela', 'gammty.views.escuela_vista'),
    (r'^nosotros/eventos/seminarioaguilas', 'gammty.views.sem_aguilas_vista'),
    (r'^nosotros/eventos/seminarioQiM', 'gammty.views.sem_qim_vista'),
    (r'^nosotros/eventos/diaaguilas', 'gammty.views.dia_aguilas_vista'),
    (r'^nosotros/eventos/cipacaipa', 'gammty.views.cipa_caipa_vista'),
    
    (r'^servicios/', 'gammty.views.servicios_vista'),
    (r'^ssc/inscripcion', 'gammty.views.ssc_vista'),
    (r'^ssc/', 'gammty.views.ssc_list_vista'),
	(r'^contacto/', 'gammty.views.contacto_vista'),
    # Examples:
    # url(r'^$', 'myproject.views.home', name='home'),
    # url(r'^myproject/', include('myproject.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
