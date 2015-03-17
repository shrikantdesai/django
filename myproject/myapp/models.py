from django.db import models

class gmailContacts(models.Model):
    user = models.CharField(max_length=100)
    contacts = models.CharField(max_length=100)
#    def __unicode__(self):
#        return u'%s %s' % (self.user, self.contacts)
