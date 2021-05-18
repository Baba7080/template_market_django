from django.db import models
from django.contrib.auth.models import User


    
    
    
    
    
CATEGORY_CHOICES = (
    ('PYTHON' , 'PYTHON'),
    ('PHP' , 'PHP PATNERS'),
    ('JAVA' , 'JAVA'),
    ('MERN' , 'MERN'),
    ('MEAN' , 'MEAN'),
    )
# Create your models here.
class template_post(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    name = models.CharField(max_length=120)
    description = models.TextField()
    category = models.CharField(choices=CATEGORY_CHOICES,max_length=12)
    image1 = models.ImageField(default='default.jpg', null= True,blank=True ,upload_to='profile_pics')
    image2 = models.ImageField(default='default.jpg',null= True,blank=True , upload_to='profile_pics')
    image3 = models.ImageField(default='default.jpg',null= True,blank=True , upload_to='profile_pics')
    image4 = models.ImageField(default='default.jpg',null= True,blank=True , upload_to='profile_pics')
    image5 = models.ImageField(default='default.jpg', null= True,blank=True ,upload_to='profile_pics')
    is_pro = models.BooleanField(default=False)
    file = models.FileField(upload_to='media')


    def __str__(self):
        return str(self.name)