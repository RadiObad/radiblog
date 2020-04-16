from django.db import models
from django.urls import reverse
from django.utils import timezone

from ckeditor.fields import RichTextField

class ModelBase(models.Model):
    id = models.AutoField(primary_key = True)
    state = models.BooleanField('State',default = True)
    creation_date = models.DateField('Creation date',auto_now = False, auto_now_add = True)
    modification_date = models.DateField('Modification date',auto_now = True, auto_now_add = False)
    removal_date = models.DateField('Elimination Date',auto_now = True, auto_now_add = False)

    class Meta:
        abstract = True

class Category(ModelBase):
    name = models.CharField('Category Name', max_length = 100, unique = True)
    referential_image = models.ImageField('Referential image',upload_to = 'categorys/')
    create_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name

class MenuCategory(models.Model):
    menu = models.OneToOneField(Category, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.menu)

class Tags(models.Model):
    name = models.CharField(max_length=45, unique=True)
    create_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


def upload_locatio(instance, filename):
    PostModel = instance.__class__
    new_id = PostModel.objects.order_by("id").last().id + 1
    """
    instance.__class__ gets the model Post. We must use this method because the model is defined below.
    Then create a queryset ordered by the "id"s of each object, 
    Then we get the last object in the queryset with `.last()`
    Which will give us the most recently created Model instance
    We add 1 to it, so we get what should be the same id as the the post we are creating.
    """
    return "posts/%s/%s" %(new_id, filename)

class PostispanManager(models.Manager):
    def active(self, *args, **kwargs):
        return super(PostispanManager, self).filter(state=True, published = True).filter(
                                                                    publication_date__lte=timezone.now())

class Post(ModelBase):
    title = models.CharField('Post title',max_length = 150, unique = True)
    slug = models.CharField('Slug', max_length = 150, unique = True)
    description = models.TextField('Description')
    # author = models.ForeignKey(Author, on_delete = models.CASCADE)
    category = models.ForeignKey(Category, on_delete = models.CASCADE)
    content = RichTextField(null=True, blank=True)
    content2 = models.TextField(null=True, blank=True)
    referential_image = models.ImageField('Referential image',
                                        upload_to=upload_locatio,
                                        max_length = 255,
                                        null=True, blank=True,
                                        height_field ="height_field",
                                        width_field="width_field"
                                          )
    height_field = models.IntegerField(default=0)
    width_field = models.IntegerField(default=0)
    tags = models.ManyToManyField(Tags)

    published = models.BooleanField('Published / Not Published',default = False)
    publication_date = models.DateField('Publication date')
    updated = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    objects = PostispanManager()
    
    def get_absolute_url(self):
        return reverse("posts:detail_post", kwargs={"slug": self.slug})
        #return "/posts/%s/" %(self.id)# this no more dynimce
        
    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'
        ordering = ["-publication_date", "-timestamp", "-updated"]


    def __str__(self):
        return self.title
