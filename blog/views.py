import random
from urllib.parse import quote_plus 
from django.core.paginator import Paginator
from django.shortcuts import render
from django.utils import timezone


from django.http import Http404
from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q
from django.views.generic import ListView, DetailView
from .models import Post, Category
from .utils import *



def error_404(request, allowed_hosts=True):
    data = {'message': '404 - Page not found'}
    return render(request, 'error.html', data)

def error_500(request, allowed_hosts=True):
    data = {'message': '500 Internal Server Error'}
    return render(request, 'error.html', data)


class DoList(ListView):
	def get(self, request, name, *args, **kwargs):
		context = generalCategory(request, name )
		return render(request, "category.html", context)


class DetailPost(DetailView):
	def get(self,request,slug,*args,**kwargs):
		try:
		    instance = Post.objects.get(slug = slug)
		    category_name = instance.category
		    if instance.timestamp > timezone.now() or not instance.published:
		    	if not request.user.is_staff or not request.user.is_superuser:
		    		raise Http404
		except:
		    raise Http404
		
		posts = list(Post.objects.filter(
					state = True,
					published = True,
					category = category_name
					).values_list('id',flat = True))
					    
		if request.user.is_staff or request.user.is_superuser:
			posts = list(Post.objects.filter(
					state = True,
					category = category_name

					).values_list('id',flat = True))


		posts.remove(instance.id)
		post1 = random.choice(posts)
		posts.remove(post1)
		post2 = random.choice(posts)
		posts.remove(post2)
		post3 = random.choice(posts)
		posts.remove(post3)
		post4 = random.choice(posts)
		posts.remove(post4)

		context ={
			"title": instance.title,
			"instance": instance,
			# "social": getNetworks(),
			# "web": getWeb(),

			"post1": consul(post1),
			"post2": consul(post2),
			"post3": consul(post3),
			"post4": consul(post4),
		}
		return render(request,'post_detail.html',context)




class PostList(ListView):
	def get(self, request, *args, **kwargs):#To list items
		today = timezone.now()	#change the cloman in datebase	
		post_general = Post.objects.active()
		if request.user.is_staff or request.user.is_superuser:
			post_general = Post.objects.all()

		paginator = Paginator(post_general, 8)
		page = request.GET.get('page')
		post_general = paginator.get_page(page)


		context = {
			"posts":post_general,
			"today": today,
			
		}		
		return render(request, "post_list.html", context)

def search_post(request):
    if request.method == 'POST':
        data = request.POST['search']
        if data:
        	posts = Post.objects.filter(Q(title__icontains=data) |
											Q(content__icontains=data)).distinct()
        context = {
            'posts': posts
        }
        return render(request, 'search.html', context)
    return render(request, 'search.html')
