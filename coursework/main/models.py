from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now


class Equation(models.Model):
    n = models.IntegerField("Количество уравнений", default=0)
    a = models.TextField("Система уравнений")
    x = models.TextField("Начальное приближение")
    y = models.TextField("Решение системы уравнений")
    iterations = models.IntegerField("Количество итераций", default=0)
    create_date = models.DateTimeField("Дата создания игры", default=now, editable=True)

    def __str__(self):
        return self.a

    class Meta:
        verbose_name = "Решение"
        verbose_name_plural = "Решения"
        ordering = ["-create_date"]
