from django.db import models


class Commands_table(models.Model):
    data = models.DateTimeField(auto_now_add=True)
    content_commands = models.TextField(max_length=255) # Buyruqlar mazmuni
    responsible = models.BooleanField(default=False) # masul tasdiqlash
    confirmation = models.BooleanField(default=False) # Derektor tasdiqlash

    def __str__(self):
        return self.confirmation






