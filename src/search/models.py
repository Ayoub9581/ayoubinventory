from django.db import models
from django.db.models.signals import pre_save, post_save
from analytics.signals import object_viewed_signal


class Search(models.Model):
    query = models.CharField(max_length=255,null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    ip_address = models.CharField(max_length=120,null=True, blank=True)




# def pre_receive_search_receiver(sender, instance, request,*args, **kwargs):
#     request = self.request
#     instance.ip_address = get_client_ip(request)


# pre_save.connect(pre_receive_search_receiver, sender=Search)