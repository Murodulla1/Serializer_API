from django.db import models


class Employees(models.Model):  # hodimlar
    name = models.CharField(max_length=100, null=True, blank=True)


class Ragbat(models.Model):
    data = models.DateField(auto_now=True)
    fulname = models.CharField(max_length=200)  # ism_familyasoi
    aboutstimulation = models.TextField(max_length=255, blank=True, null=True)  # rag`banlashtirish
    by_whom = models.ForeignKey(Employees, on_delete=models.CASCADE, null=True)  # kim tomonidan
    confirmation = models.BooleanField(default=False)  # Tasdiqlash

    def __str__(self):
        return f"{self.confirmation}"
