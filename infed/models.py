from django.db import models
from django.urls import reverse


class ServiceProvider(models.Model):
    xml = models.TextField(verbose_name='SAML Metadata XML')

    def get_absolute_url(self):
        return reverse('serviceprovider_detail', kwargs={'pk': self.pk})