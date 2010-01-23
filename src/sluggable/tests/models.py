from django.db import models
from sluggable.models import SluggableModel

class SimpleSluggableModel(SluggableModel):
    alpha = models.CharField(max_length=255)
    
    def __unicode__(self):
        return u'%s' % self.alpha

class MultiFieldSluggableModel(SluggableModel):
    alpha = models.CharField(max_length=255)
    beta = models.CharField(max_length=255)
    
    def __unicode__(self):
        return u'%s %s' % (self.alpha, self.beta)

class UniqueTogetherSluggableModel(SluggableModel):
    alpha = models.CharField(max_length=255)
    beta = models.CharField(max_length=255)
    
    def __unicode__(self):
        return u'%s' % self.alpha
    
    class Meta:
        unique_together = (('slug', 'beta'),)