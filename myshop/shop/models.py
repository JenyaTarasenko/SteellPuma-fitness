from django.db import models



class News(models.Model):
    title = models.CharField(
        max_length=200,
        verbose_name='Назва новини'
    )

    image = models.ImageField(
        upload_to='news/',
        verbose_name='Зображення'
    )

    description = models.TextField(
        verbose_name='Опис'
    )



    class Meta:
        verbose_name = 'Новина'
        verbose_name_plural = 'Новини'


    def __str__(self):
        return self.title
