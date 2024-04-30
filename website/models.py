from django.db import models

class Contact(models.Model):
    name =models.CharField(max_length=300)
    email = models.EmailField(max_length = 300)
    subject = models.CharField(max_length=350)
    message = models.TextField()

# class Education(models.Model):
#     name =models.CharField(max_length=300)
#     email = models.EmailField(max_length = 300)
#     subject = models.CharField(max_length=350)
#     message = models.TextField()
   
    
# class ProfessionalExperience(models.Models):
#     name =models.CharField(max_length=300)
#     email = models.EmailField(max_length = 300)
#     subject = models.CharField(max_length=350)
#     message = models.TextField()


    