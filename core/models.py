from django.db import models


# About Model
class About(models.Model):
    short_description = models.TextField()
    description = models.TextField()
    image = models.ImageField(upload_to="about")
    cv = models.URLField( max_length=100)

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

    STATUS_CHOICES = (
        ('enabled', 'enabled'),
        ('disabled', 'disabled'),
    )

    title = models.CharField(max_length=100, verbose_name="Work title")
    image = models.ImageField(upload_to="works")
    rank = models.PositiveIntegerField()
    code_url = models.URLField(max_length=200, null=True, blank=True)
    notebook_url = models.URLField(max_length=200, null=True, blank=True)
    code_status = models.CharField(max_length=10, null=False, choices=STATUS_CHOICES)
    notebook_status = models.CharField(max_length=10, null=False, choices=STATUS_CHOICES)
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


# MOOC Model
class MOOC(models.Model):
    name = models.CharField(max_length=100, verbose_name="Course name")
    issuer = models.CharField(max_length=100, verbose_name="issuer")
    certificate_link = models.URLField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.name
