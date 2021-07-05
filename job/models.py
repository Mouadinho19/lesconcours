from django.contrib.auth.models import User
from django.db import models
from django.db.models.fields import CharField
from django.template.defaultfilters import slugify
# Create your models here.

'''
 django model field : 
    - html widget
    - validation 
    - db size 
'''

JOB_TYPE = (
    ('Full Time','Full Time'),
    ('Part Time','Part Time'),
)


class Job(models.Model):  # table 
    owner = models.ForeignKey(User, related_name='job_owner', on_delete=models.CASCADE, verbose_name='propriétaire')
    title = models.CharField(max_length=150, verbose_name='titre', help_text="Titre de Concours")  # column
    # location 
    description = models.TextField(max_length=1000, help_text='Description du Concours')
    published_at = models.DateTimeField(auto_now=True)
    Vacancy = models.IntegerField(default=1, verbose_name='position')
    experience = models.IntegerField(default=1, help_text="Nombre d'années d'expérience") 
    category = models.ForeignKey('Category',on_delete=models.CASCADE, verbose_name='catégorie')
    image = models.ImageField(upload_to='jobs/')
    slug = models.SlugField(blank=True, null=True)
    class Meta:
        verbose_name_plural = "concours"

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)
    def __str__(self):
        return self.title

class Category(models.Model):
    name = models.CharField(max_length=25, verbose_name='nom')

    class Meta:
        verbose_name_plural = "catégorie"

    def __str__(self):
        return self.name

class Apply(models.Model):
    job = models.ForeignKey(Job, related_name='apply_job', on_delete=models.CASCADE, verbose_name="titre de concours")
    name = models.CharField(max_length=50, verbose_name='nom et prenom')
    email = models.EmailField(max_length=80)
    cv = models.FileField(upload_to='apply/')
    letter = models.TextField(max_length=400, verbose_name='lettre')
    created_at = models.DateTimeField(auto_now=True)
    class Meta:
        verbose_name_plural = "postuler"

    def __str__(self):
        return self.name

class Contact(models.Model):
    username = models.CharField(max_length=40, verbose_name="nom d'utulisateur")
    email = models.EmailField(max_length=50)
    message = models.TextField(max_length=1000)
    created_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name_plural = "contact"

    def __str__(self):
        return self.username