from django.db import models


# About Model
class About(models.Model):
    short_description = models.TextField()
    description = models.TextField()
    image = models.ImageField(upload_to="about")

    class Meta:
        verbose_name = "About me"
        verbose_name_plural = "About me"

    def __str__(self):
        return "About me"


# Skills Model
class Skill(models.Model):
    name = models.CharField(max_length=100, verbose_name="Skill name")
    description = models.TextField(verbose_name="About skill")
    rank = models.PositiveIntegerField()

    ordering = [rank]

    def __str__(self):
        return self.name


# Recent Work Model
class RecentWork(models.Model):

    LINK_TYPE_CHOICES = (
        ('Code','Code'),
        ('Notebook','Notebook')
    )

    title = models.CharField(max_length=100, verbose_name="Work title")
    image = models.ImageField(upload_to="works")
    rank = models.PositiveIntegerField()
    url = models.URLField(max_length=200)
    file_type = models.CharField(max_length=10, null=False, choices=LINK_TYPE_CHOICES)
    photo_credit = models.CharField(max_length=100)

    ordering = [rank]

    def __str__(self):
        return self.title


# Client model
class Client(models.Model):
    name = models.CharField(max_length=100, verbose_name="Client name")
    description = models.TextField(verbose_name="Client say")
    image = models.ImageField(upload_to="clients", default="default.png")

    def __str__(self):
        return self.name
