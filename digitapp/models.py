from django.utils import timezone
from django.db import models
from django.urls import reverse


class Lab(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    fields = models.ManyToManyField('Field', related_name='lab')
    image = models.ImageField()
    slug = models.SlugField(max_length=100, unique=True, db_index=True, blank=True)
    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse('lab', kwargs={'lab_slug': self.slug})


class Field(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField()
    slug = models.SlugField(max_length=100, unique=True, db_index=True, blank=True)
    def __str__(self):
        return self.name


class Project(models.Model):
    lab = models.ForeignKey('Lab', on_delete=models.DO_NOTHING)
    field = models.ForeignKey('Field', on_delete=models.DO_NOTHING)
    name = models.CharField(max_length=100)
    description = models.TextField()
    content = models.TextField()
    slug = models.SlugField(max_length=100, unique=True, db_index=True, blank=True)
    date = models.DateField(default=timezone.now())
    image = models.ImageField()


    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse('project', kwargs={'project_slug': self.slug})
    

class Application(models.Model):
    full_name = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    topic = models.CharField(max_length=50)
    message = models.CharField(max_length=500)

    def __str__(self):
        return f'{self.full_name} - {self.topic}'


class Mailing(models.Model):
    email = models.EmailField()
    def __str__(self):
        return self.email 
