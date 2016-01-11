from __future__ import unicode_literals
import requests
from django.db import models

# Create your models here.

class Test(models.Model):
    Summary = models.CharField(max_length=2000)


def TestSaveToDatabase():
    
    r = requests.get('https://api.github.com/users/defunkt')
    rjson = r.json()
    
    test = Test(Summary = rjson['name'])
    test.save()
