from django.db import models

class indexhero(models.Model):
    title = models.CharField(max_length=200, default="Hi, it's me")
    subtitle = models.CharField(max_length=200, default="Subash Dhami")
    description = models.TextField(
        default="Passionate Python Django developer creating dynamic web applications that blend clean code with user-friendly design. Let’s turn your ideas into reality."
    )
    profile_image = models.ImageField(upload_to='profile/', default='static/img/profile/profile.png')
    background_image = models.ImageField(upload_to='background/', blank=True)

    def __str__(self):
        return self.title

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
    CATEGORY_CHOICES = [
        ('photography', 'Photography'),
        ('design', 'Design'),
        ('automotive', 'Automotive'),
        ('nature', 'Nature'),
    ]

    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='portfolio/')
    link = models.URLField(blank=True)
    order = models.PositiveIntegerField(default=0)  # For ordering in the showcase
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)

    def __str__(self):
        return self.title
    
class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.email}"
    

class Service(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    icon = models.CharField(max_length=100)
    order = models.PositiveIntegerField(default=0)  # For ordering in the showcase
    duration = models.CharField(max_length=100, blank=True)  # e.g., "3-6 months"
    manager = models.CharField(max_length=100, blank=True)  # e.g., "Sarah Johnson"
    contact_support = models.CharField(max_length=100, blank=True)  # e.g., "+1 (555) 123-4567"
    features = models.JSONField(blank=True, default=list)  # List of features (e.g., ["SEO", "SMM"])
    images = models.ImageField(upload_to='services/', blank=True)  # Upload a single image

    def __str__(self):
        return self.title


