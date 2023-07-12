from django.db import models

# Create your models here.
class Estufa(models.Model):
    titulo=models.CharField(max_length=50)
    descripccion=models.CharField(max_length=50)
    imagen=models.ImageField(upload_to='estufas')
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name='estufa'
        verbose_name_plural='estufas'

        def __str__(self):
            return self.titulo