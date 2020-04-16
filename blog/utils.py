from django.core.paginator import Paginator

from .models import Post, Category
def consul(id):
    try:
        return Post.objects.get(id = id)
    except:
        return None


def generalCategory(request, category_name ):
    posts = Post.objects.filter(
                                        state = True,
                                        published = True,
                                        category = Category.objects.get(name=category_name)
                                        )
    try:
        category = Category.objects.get(name = category_name)
    except:
        category = None #return 404 page
    paginator = Paginator(posts,4)
    page = request.GET.get('page')
    posts = paginator.get_page(page)

    context = {
        "title":category_name,
        "posts": posts,
        "category": category    
    }
    return context  
