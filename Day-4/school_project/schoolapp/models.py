from django.db import models

#classroom model
class Classroom(models.Model):
    class_name = models.CharField(max_length=50)
    section = models.CharField(max_length=1)

    def __str__(self):
        return f"{self.class_name}-{self.section}"


#student model with ForeignKey
class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    is_active = models.BooleanField(default=True)
    joined_date = models.DateField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now=True)
    classroom = models.ForeignKey(Classroom, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


#  Teacher model with OneToOneField
class Teacher(models.Model):
    name = models.CharField(max_length=100)
    subject = models.CharField(max_length=100)
    classroom = models.OneToOneField(Classroom, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


# Activity model with ManyToManyField
class Activity(models.Model):
    name = models.CharField(max_length=100)
    students = models.ManyToManyField(Student)

    def __str__(self):
        return self.name
