from django.contrib import admin	
from .models import *

class PostModelAdmin(admin.ModelAdmin):
	list_display = ["title", "updated", "timestamp"]
	list_display_links = ["updated"]
	list_editable = ["title"]
	list_filter = ["updated", "timestamp"]
	search_fields = ["title", "content"]
	class Meta:
		model = Post
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'create_date']

class TagsAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'create_date']

# class FeaturedPostAdmin(admin.ModelAdmin):
#     list_display = ['id', 'post', 'date']

class MenuCategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'menu', 'date']

admin.site.register(Category, CategoryAdmin)
admin.site.register(Tags, TagsAdmin)
admin.site.register(MenuCategory, MenuCategoryAdmin)

admin.site.register(Post, PostModelAdmin)



