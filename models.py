from django.db import models
from mptt.models import MPTTModel,TreeForeignKey


class CornerstoneUserProfile(MPTTModel):

    guid = models.UUIDField(unique = True)
    user_id = models.IntegerField(unique = True)
    first_name = models.CharField(max_length = 50)
    last_name = models.CharField(max_length = 50)
    parent = TreeForeignKey('self',null = True, blank = True, related_name = 'children', db_index = True)
    # parent is nothing but manager_id
    manager_guid = models.UUIDField(unique = True, null = True)

    def __unicode__(self):
        return "(%s), %s, %s" % (self.parent, self.first_name, self.last_name)
