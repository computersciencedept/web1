from django.contrib.auth.models import AbstractUser
from django.db import models


def validate_room_size(value):
    if (value < 200 and value > 0):
        return value
    else:
        raise ValidationError("Room size is not valid")




class CustomUser(AbstractUser):

   STATUS = (
     ('student', 'student'),
     ('faculty', 'faculty'),
     ('admin', 'admin'),
   )

   email = models.EmailField(unique=True)
   status = models.CharField(max_length=100, choices=STATUS, default='regular')
   description = models.TextField("Description", max_length=600, default='', blank=True)
   def __str__(self):
      return self.username

class classroom(models.Model):
    CAMPUS = (
            ("Middletown","Middletown"),
            ("Newburgh","Newburgh"),
            ("Other","Other"),
    )
    roomtype = models.CharField(max_length = 100)
    capacity = models.IntegerField(validators =[validate_room_size])
    class_room_id = models.AutoField(auto_created = True,
                  primary_key = True,
                  serialize = False, 
                  verbose_name ='class_room_id')
    location = models.CharField(max_length = 30)
    room_number = models.CharField(max_length = 30)
    campus = models.CharField(max_length = 30,choices=CAMPUS,default="Middletown")
    def __str__(self):
      return self.room_number

class classes(models.Model):
    class_room_id = models.ForeignKey(classroom,on_delete=models.DO_NOTHING)
    CRN = models.AutoField(auto_created = True,
                  primary_key = True,
                  serialize = False,
                  verbose_name ='class_room_id')
    teacher_id = models.IntegerField()
    description = models.TextField()
    size = models.IntegerField()
    registered_total = models.IntegerField()
    wait_list = models.IntegerField()
    time = models.CharField(max_length = 100)
    credits = models.IntegerField()
    day_of_week = models.CharField(max_length = 30)
    semester = models.CharField(max_length = 30)
    semester_year = models.IntegerField()
    semester_session = models.CharField(max_length = 30)
    subject = models.CharField(max_length = 100)
    instruction_method = models.CharField(max_length = 100)
    campus = models.CharField(max_length = 100)
    time_start = models.TimeField()
    time_end = models.TimeField()

    def __str__(self):
      return self.CRN

class student(models.Model):
    student_id = models.OneToOneField(CustomUser,on_delete=models.DO_NOTHING,primary_key = True,verbose_name ='student_id')
    gpa = models.FloatField()
    credits = models.FloatField()
    major = models.CharField(max_length = 50)
    courses_taken = models.ManyToManyField(classes)

    def __str__(self):
      return self.student_id


class teacher(models.Model):
    teacher_id = models.OneToOneField(CustomUser,on_delete=models.DO_NOTHING,primary_key = True,verbose_name ='teacher_id')
    title = models.CharField(max_length = 50)
    title = models.CharField(max_length = 50)
    courses_teaching = models.ManyToManyField(classes)

    def __str__(self):
      return self.teacher_id
# Create your models here.
