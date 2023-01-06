from django.db import models

# Create your models here.
class Emp(models.Model):
    name = models.CharField(max_length=50)
    emp_id = models.CharField(max_length=50)
    phone = models.CharField(max_length=10)
    city = models.CharField(max_length=50)
    working = models.BooleanField(default=True)
    department = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    
    
class Testimonial(models.Model):
    name = models.CharField(max_length=50)
    testimonial = models.TextField(default=' ')
    picture = models.ImageField(upload_to="testimonials/",default=0)
    rating = models.IntegerField(default=0)

    def __str__(self):
        return self.testimonial



     