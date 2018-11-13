from django.db import models

# Create your models here.
class Guestbook(models.Model):
    name = models.CharField(max_length=50)
    password = models.CharField(max_length=1000)
    message = models.CharField(max_length=200)
    reg_date = models.DateTimeField(auto_now=True)




    def __str__(self):
        return 'Guestbook(%s , %s , %s,%s)' %(self.name, self.password , self.message,self.reg_date)

