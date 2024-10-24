from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
import uuid
from django import forms


# Create your models here.
# ********************* Student Model ************************
class Student(models.Model):
    first_name = models.CharField(max_length=50)
    last_name  = models.CharField(max_length=50)
    user = models.OneToOneField(User, on_delete=models.CASCADE,null=True,blank=True)
    registration_number = models.CharField(max_length=20, unique=True, null=True, blank=True)
    date_of_birth = models.DateField(null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    phone = models.BigIntegerField(null=True, blank=True)
    address = models.TextField(null=True, blank=True)
    BLOOD_GROUP_CHOICES = [
        ('A+', 'A+'),
        ('A-', 'A-'),
        ('B+', 'B+'),
        ('B-', 'B-'),
        ('AB+', 'AB+'),
        ('AB-', 'AB-'),
        ('O+', 'O+'),
        ('O-', 'O-'),
    ]
    blood_group = models.CharField(max_length=3, choices=BLOOD_GROUP_CHOICES, null=True, blank=True)
    GENDER_CHOICES = [
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other'),
    ]
    gender = models.CharField(max_length=6, choices=GENDER_CHOICES, null=True, blank=True)

    department = models.ForeignKey('Department', on_delete=models.SET_NULL, null=True, blank=True)
    bach = models.ForeignKey('Batch', on_delete=models.SET_NULL, null=True, blank=True)
    
    FEES_CHOICE = [
        ('Unpaid','Unpaid'),
        ('pending','Pending'),
        ('paid','paid'),
    ]
    fees = models.CharField(max_length=10, choices=FEES_CHOICE, null=True, blank=True)
    
    ATTENTANCE_CHOICE = [
        ('Present','Present'),
        ('Absent','Absent'),
    ]
    attendence = models.CharField(max_length=10, choices=ATTENTANCE_CHOICE, null=True, blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}  {self.bach}"

# ************************ Student Profile update ************************

class StudentProfileUpdate(forms.ModelForm):
    class Meta:
        model = Student
        fields = [
            'first_name', 'last_name',  'email',
            'phone', 'address', 'blood_group', 'gender','date_of_birth'
        ]
        widgets = {
            'date_of_birth': forms.DateInput(attrs={'type': 'date'}),
            'address': forms.Textarea(attrs={'rows': 3}),
        }


# ************************ fees update ************************





# *********************** Department Model ************************

class Department(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name
    


# ************************ Batch Model ************************

class Batch(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid.uuid4, editable=False, unique=True)
    SELECT_MONTH = [
    ('JAN', 'January'),
    ('FEB', 'February'),
    ('MARCH', 'March'), 
    ('APRIL', 'April'),
    ('MAY', 'May'),
    ('JUNE', 'June'),
    ('JULY', 'July'),
    ('AUG', 'August'),
    ('SEP', 'September'),
    ('OCT', 'October'),
    ('NOV', 'November'),
    ('DEC', 'December'),
    ]

    month = models.CharField(max_length=6, choices=SELECT_MONTH, null=True, blank=True)
    date = models.IntegerField(null=True, blank=True)
    SELECT_BACH = [
        ('B1','Bach 1'),
        ('B2','Bach 2'),
        ('B3','Bach 3'),
        ('B4','Bach 4'),
        ('B5','Bach 5'),
    ]
    bach = models.CharField(max_length=2, choices=SELECT_BACH, null=True, blank=True)
    SELECT_TIME = [
        ('08:00 AM','08:00 AM'),
        ('09:00 AM','09:00 AM'),
        ('10:00 AM','10:00 AM'),
        ('11:00 AM','11:00 AM'),
        ('12:00 PM','12:00 PM'),
        ('01:00 PM','01:00 PM'),
        ('02:00 PM','02:00 PM'),
        ('03:00 PM','03:00 PM'),
        ('04:00 PM','04:00 PM'),
        
    ]

    class_time = models.TextField(max_length=8, choices=SELECT_TIME, null=True, blank=True)
    department = models.ForeignKey('Department', on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"{self.department} {self.month} {self.date} {self.bach} "

