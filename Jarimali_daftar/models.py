from django.db import models

class Fines(models.Model):
    data = models.DateField(auto_now=True)
    to_do = models.TextField() # Ishlar ro`yxati
    by_whom = models.CharField(max_length=250, blank=True, null=True)# Kim tomonidan
    time_Lider = models.DateField(auto_now=True) # Rahbardan muddat
    fine = models.IntegerField()  # Jarima
    signature = models.BooleanField(default=False)  # Tasdiqlash
    def __str__(self):
        return self.Time_Lider






