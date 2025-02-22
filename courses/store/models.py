from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Course(models.Model):
    user = models.ForeignKey(User , on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    desc= models.TextField(max_length=200)
    start_date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='images')
    price=models.IntegerField()
    duration =models.IntegerField()
    online = models.BooleanField(True)

    def __str__(self) -> str:
        return self.title



class Review (models.Model):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    rate = models.CharField(max_length=100)
    comment = models.TextField(max_length=112)
    course=models.ForeignKey(Course,on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.rate



class Order(models.Model):
    courses = models.ForeignKey(Course, on_delete=models.DO_NOTHING)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    date = models.DateTimeField(auto_now_add=True)
    total_price = models.IntegerField()

    def __str__(self) -> str:
        return self.total_price

