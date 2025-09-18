from django.db import models

class about(models.Model):
    name = models.CharField(max_length=100)
    profession = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    location = models.CharField(max_length=100)
    profile_image = models.ImageField(upload_to='profile/')
    description = models.TextField()
    description_secondary = models.TextField(blank=True)
    specialization = models.CharField(max_length=100)
    experience_level = models.CharField(max_length=100)
    education = models.CharField(max_length=200)
    languages = models.CharField(max_length=200)
    resume_link = models.URLField(blank=True)
    talk_link = models.URLField(blank=True)

    projects_completed = models.PositiveIntegerField(default=0)
    years_experience = models.PositiveIntegerField(default=0)
    client_satisfaction = models.PositiveIntegerField(default=0)  # Store as percentage

    def __str__(self):
        return self.name
    

class Stat(models.Model):
    count = models.PositiveIntegerField()
    label = models.CharField(max_length=100)  # e.g., 'Happy Clients'
    order = models.PositiveIntegerField(default=0)  # For ordering in the template

    def __str__(self):
        return f"{self.label}: {self.count}"


class Skill(models.Model):
    description = models.TextField(blank=True)
    name = models.CharField(max_length=100)
    icon = models.ImageField(upload_to='skills/', blank=True)  # Store skill icon images
    order = models.PositiveIntegerField(default=0)  # For ordering in the showcase

    def __str__(self):
        return self.name


class Portfolio(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='portfolio/')
    link = models.URLField(blank=True)
    order = models.PositiveIntegerField(default=0)  # For ordering in the showcase

    def __str__(self):
        return self.title
