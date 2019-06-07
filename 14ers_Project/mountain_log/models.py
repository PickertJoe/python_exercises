from django.db import models

# Create your models here.


class Mountain(models.Model):
    """Information for a mountain the user would like to describe"""
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Return a string representation of the model"""
        return self.text


class Entry(models.Model):
    """Adding specific information about the mountain in question"""
    topic = models.ForeignKey(Mountain, on_delete=models.CASCADE)
    text = models.TextField()
    elevation = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'entries'

    def __str__(self):
        """Returns a string representation of the model"""
        if len(self.text) > 50:
            return self.text[:50] + "..."
        else:
            return self.text
