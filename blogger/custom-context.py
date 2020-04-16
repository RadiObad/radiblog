from blog.models import Category, Tags, MenuCategory, Post
from contact.models import Socialnetworks, Web
from django.db.models import Count
# from contact.forms import NewsletterForm


def mycontext(request):
    tag = Tags.objects.all()
    menu = MenuCategory.objects.all()
    recent_post = Post.objects.active()[:3]
    context = {
        'tag': tag,
        'menu': menu,
        'recent_post': recent_post
    }
    return context

# def newsletter_form(request):
#     forms = NewsletterForm()
#     if request.method == 'POST':
#         forms = NewsletterForm(request.POST)
#         if forms.is_valid():
#             forms.save()

#     context = {
#         'forms': forms
#     }
#     return context
def getNetworks():
	social = Socialnetworks.objects.filter(state = True).latest('creation_date')
	context={"social":social}
	return context
def getWeb():
    web = Web.objects.filter(state = True).latest('creation_date')
    return {"web":web}