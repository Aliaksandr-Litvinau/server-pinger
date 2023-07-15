from django.db import models


class Domain(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class ResponseTime(models.Model):
    domain = models.ForeignKey(Domain, on_delete=models.CASCADE)
    time = models.DateTimeField()
    response_time = models.FloatField()

    def __str__(self):
        return f"{self.domain}: {self.response_time}ms"
