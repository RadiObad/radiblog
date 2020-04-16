from django.urls import path

# from . import views
from .views import (
				PostList,
				DoList,
				DetailPost,
				error_404,
				error_500,
				search_post

	)
from django.conf.urls import handler404, handler500



app_name = "post"
urlpatterns = [
	path('', PostList.as_view(), name='post-list'),
	path('<slug:slug>/', DetailPost.as_view(), name='detail_post'),
	path('category/<name>', DoList.as_view(), name='category'),
    path('search', search_post, name='search')

]
handler404 = error_404
handler500 = error_500