from django.db import models

class Project(models.Model):
    STATUS_CHOICES = [
        ('قيد التنفيذ', 'قيد التنفيذ'),
        ('مكتمل', 'مكتمل'),
        ('تحت الدراسة', 'تحت الدراسة'),
    ]

    name = models.CharField(max_length=100)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='قيد التنفيذ')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
