from django.db import models
from django.core.exceptions import ValidationError

class Employee(models.Model):
    start_date = models.DateField()
    end_date = models.DateField()
    leapyear_count = models.IntegerField(default=0)
    non_leapyear_count = models.IntegerField(default=0)

    def clean(self):
        # Ensure start_date is before end_date
        if self.start_date > self.end_date:
            raise ValidationError("Start date cannot be after the end date.")
    
    def save(self):
        self.clean()  # Call the validation logic
        super().save()  # Save the object