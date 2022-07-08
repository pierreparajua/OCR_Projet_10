from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    pass


class Projects(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    choices_priority = ['back_end', 'front_end', 'IOS', 'Android']
    type = models.CharField(max_length=50, choices=choices_priority)
    author = models.ForeignKey(to=User.pk, on_delete=models.CASCADE)


class Contributors(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    project = models.ForeignKey(to=Projects, on_delete=models.CASCADE)
    choices_priority = ['bug', 'tâche', 'amélioration']
    permission = models.CharField()
    choices = ['auteur', 'responsable', 'créateur']
    role = models.CharField(choices=choices)


class Issues(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    choices_tag = ['bug', 'tâche', 'amélioration']
    tag = models.CharField(choices=choices_tag)
    choices_priority = ['bug', 'tâche', 'amélioration']
    priority = models.CharField(choices=choices_priority)
    project = models.ForeignKey(to=Projects.pk, on_delete=models.CASCADE)
    choices_status = ['en attende', 'en cours', 'terminé']
    status = models.CharField(choices=choices_status)
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    created_time = models.DateTimeField(auto_now_add=True)


class Comments(models.Model):
    description = models.TextField()
    author = models.ForeignKey(to=User, on_delete=models.CASCADE)
    issue = models.ForeignKey(to=Issues, on_delete=models.CASCADE)
    created_time = models.DateTimeField(auto_now_add=True)
