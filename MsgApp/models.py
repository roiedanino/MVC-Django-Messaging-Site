from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Message(models.Model): #ORM: Object to Relational Mapping
    sender = models.ForeignKey(User, related_name='sender')
    receiver = models.ForeignKey(User, related_name='receiver')
    content = models.TextField()
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.pub_date.hour.__str__()+":"+self.pub_date.minute.__str__() + " " + self.sender.get_full_name() + ": " + self.content.__str__()




