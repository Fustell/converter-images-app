from django.db import models
import os

class Document(models.Model):

    document = models.FileField(upload_to='documents/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return os.path.basename(self.document.name)

    class Meta:
        verbose_name = 'Зображення'