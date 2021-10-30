from django.db import models
# Create your models here.

class Writer(models.Model):
    name=models.CharField(max_length=100,null=True)
    def __str__(self):
        return self.name

class Book(models.Model):
    category=(
        ('သုတ','သုတ'),
        ('ရသ','ရသ')
    )
    status=(
        ('ရရှိနိုင်','ရရှိနိုင်'),
        ('မရရှိနိုင်သေးပါ','မရရှိနိုင်သေးပါ')
    )
    Writer=models.ForeignKey(Writer, null=True, on_delete=models.CASCADE)
    bookname=models.CharField(max_length=100,null=True)
    bookno=models.CharField(max_length=100,null=True)
    category=models.CharField(max_length=50,null=True,choices=category)
    status=models.CharField(max_length=100,null=True,choices=status)

    def __str__(self):
        return self.bookname
    

class Feed(models.Model):
    photo=models.ImageField( upload_to='static\images', null=True,blank=True)
    content=models.CharField(max_length=1000,null=True)
    created_at=models.DateTimeField(auto_now_add=True)