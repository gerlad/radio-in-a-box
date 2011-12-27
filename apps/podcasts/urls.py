from django.conf.urls.defaults import patterns, url
from django.views.generic.simple import direct_to_template

from podcasts.views import ShowListView, ShowDetailView, EpisodeListView, EpisodeDetailView

urlpatterns = patterns("",
	url(r"^upload/$", direct_to_template, {"template": "podcasts/upload.html"}, name="upload"),
	)

'''
from django.conf.urls.defaults import patterns, url
from podcasting.views import ShowListView, ShowDetailView, EpisodeListView, EpisodeDetailView


urlpatterns = patterns("",
    url(r"^$", ShowListView.as_view(),
        name="podcasting_show_list"),
    url(r"^(?P<slug>[-\w]+)/$", ShowDetailView.as_view(),
        name="podcasting_show_detail"),
    url(r"^(?P<show_slug>[-\w]+)/archive/$", EpisodeListView.as_view(),
        name="podcasting_episode_list"),
    url(r"^(?P<show_slug>[-\w]+)/(?P<slug>[-\w]+)/$", EpisodeDetailView.as_view(),
        name="podcasting_episode_detail"),
)
'''