from django.db import models

# Create your models here.

class personal_dtl(models.Model):
    name = models.CharField(default='Ihsan K',max_length=50)
    age = models.IntegerField(default=22)
    residence = models.CharField(max_length=100, default='Pandikkad, Malappuram ')
    address = models.CharField(max_length=200, default='Pandikkad 676521, Malappuram, Kerala')
    email = models.EmailField(default='ihsankpkd@gmail.com')
    phone = models.CharField(max_length=40, default='+91 7510719407, +91 7510719408')
    profile_photo = models.ImageField(upload_to='app/static/my_photo', blank=True, null=True)
    
    def __str__(self):
       return self.name
   
class aboutme(models.Model):
    about = models.TextField(max_length=600,default="Iam Ihsan, I recently completed my post graduation in field of MVoc Software development from university of calicut in 2023")
    
    

class education(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=600)
    start_year = models.IntegerField()
    end_year =models.IntegerField()
    university = models.CharField(max_length=50)
    score = models.FloatField()
    
    def __str__(self):
       return self.title
    
class experience(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=600)
    start_end_year = models.CharField(max_length=50)
    company_name = models.CharField(max_length=50)
    
    def __str__(self):
       return self.title
   
class skill(models.Model):
    name = models.CharField(max_length=50)
    percentage = models.IntegerField()
    
    def __str__(self):
       return self.name
    
class projects(models.Model):
    category_choice = (
        ('django', 'Django'),
        ('ml', 'ML & AI'),
    )
    title = models.CharField(max_length=50)
    category = models.CharField(max_length=50, choices=category_choice)
    description = models.CharField(max_length=400)
    image = models.ImageField(upload_to='app/static/projects')
    link = models.CharField(max_length=200)
    
    def __str__(self):
       return self.title
   
class certificates(models.Model):
    title = models.CharField(max_length=50)
    company = models.CharField(max_length=50)
    year = models.DateField()
    description = models.CharField(max_length=300)
    link = models.CharField(max_length=200)
    
    def __str__(self):
       return self.title
    

class messages(models.Model):
    snder_name = models.CharField(max_length=50)
    sndr_mail = models.EmailField()
    message = models.TextField(max_length=100)
    
    def __str__(self):
       return self.snder_name
    
