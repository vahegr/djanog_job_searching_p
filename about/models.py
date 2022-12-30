from django.db import models


class About(models.Model):
    location = models.TextField(max_length=1000)
    employer_call = models.CharField(max_length=15)
    job_searcher_call = models.CharField(max_length=15)
    email = models.EmailField(max_length=150)
    telegram = models.URLField(max_length=600)
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.email
