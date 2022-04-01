from django.db import models


class Person(models.Model):
    img_profile = models.ImageField(default=None, null=True, blank=True)
    registration_number = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    first_name = models.CharField(max_length=30)
    birth_date = models.DateField(blank=True)
    email = models.EmailField()
    home_phone_number = models.CharField(max_length=20, blank=True)
    cellphone_number = models.CharField(max_length=20, blank=True)
    password = models.CharField(max_length=32)
    friends = models.ManyToManyField('self', null=True, blank=True)
    faculty = models.ForeignKey('Faculty', on_delete=models.CASCADE, default=None)
    person_type = 'generic'

    def __str__(self):
        return self.first_name + " " + self.last_name


class Message(models.Model):
    author = models.ForeignKey('Person', on_delete=models.CASCADE, default=None)
    content = models.TextField()
    publication_date = models.DateField(auto_now=False, auto_now_add=True)

    def __str__(self):
        if len(self.content) > 20:
            return self.content[:19] + "..."
        else:
            return self.content


class Faculty(models.Model):
    name = models.CharField(max_length=30)
    color = models.CharField(max_length=6)

    def __str__(self):
        return self.name


class Campus(models.Model):
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=60)

    def __str__(self):
        return self.name


class Job(models.Model):
    title = models.CharField(max_length=30)

    def __str__(self):
        return self.title


class Cursus(models.Model):
    title = models.CharField(max_length=30)

    def __str__(self):
        return self.title


class Employee(Person):
    office = models.CharField(max_length=30)
    campus = models.ForeignKey('Campus', on_delete=models.CASCADE, default=None)
    job = models.ForeignKey('Job', on_delete=models.CASCADE, default=None)
    person_type = 'employee'


class Student(Person):
    cursus = models.ForeignKey('Cursus', on_delete=models.CASCADE, default=None)
    year = models.IntegerField()
    person_type = 'student'


class Publication(models.Model):
    nb_like = models.IntegerField()
    comment = models.CharField(max_length=255)
    nb_sharing = models.IntegerField()
    author_fk = models.ForeignKey('Person', on_delete=models.CASCADE, default=None)
    content_fk = models.ForeignKey('Content_pub', on_delete=models.CASCADE, default=None)
    date = models.DateField()


class Content_pub(models.Model):
    text = models.TextField(blank=True)
    img = models.ImageField(blank=True)
    videos_path = models.CharField(max_length=255, blank=True)


class Notifications(models.Model):
    state = models.CharField(max_length=10)
    type = models.CharField(max_length=5)
    content = models.CharField(max_length=255)

    def __str__(self):
        return self.content
