from django.db import models

class signup_Table(models.Model):
    full_name = models.CharField(max_length=100)   
    email = models.EmailField(unique=True)        
    password = models.CharField(max_length=100)   
    
    def __str__(self):
        return self.full_name

class Login(models.Model):
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.email


from django.db import models

class Outfit(models.Model):
    GENDER_CHOICES = [
        ('male', 'Male'),
        ('female', 'Female'),
    ]

    OCCASION_CHOICES = [
        ('casual', 'Casual'),
        ('party', 'Party'),
        ('formal', 'Formal'),
    ]

    STYLE_CHOICES = [
        ('street', 'Street'),
        ('traditional', 'Traditional'),
        ('minimal', 'Minimal'),
    ]

    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    occasion = models.CharField(max_length=10, choices=OCCASION_CHOICES)
    style = models.CharField(max_length=15, choices=STYLE_CHOICES)
    color = models.CharField(max_length=20)
    image = models.ImageField(upload_to='outfits/')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.gender} | {self.occasion} | {self.style}"
