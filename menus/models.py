from django.db import models
from django.urls import reverse


class MenuItem(models.Model):
    name = models.CharField(max_length=50)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True)
    url = models.CharField(max_length=100, blank=True, null=True, unique=True)
    named_url_parts = models.CharField(max_length=100, blank=True, null=True)

    def save(self, *args, **kwargs):
        if self.named_url_parts:
            url_name = self.named_url_parts[0]
            params = self.named_url_parts[1:]
            self.url = reverse(url_name, args=params)
        else:
            self.url = self.url
        super(MenuItem, self).save(*args, **kwargs)


    def __str__(self):
        return self.name

    def children(self):
        return self.menuitem_set.all()

    def get_elder_ids(self):
        if self.parent:
            return self.parent.get_elder_ids() + [self.parent.id]
        else:
            return []
