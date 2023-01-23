from django.db import models
import uuid


# Create your models here.

class Student(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    name = models.CharField(max_length=255)
    roll_no = models.IntegerField()
    age = models.IntegerField()
    is_deleted = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.name } {self.age}"
