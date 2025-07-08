from django.db import models

class AboutImage(models.Model):
    image = models.ImageField(upload_to='about_images/')

    def __str__(self):
        return self.image.name

class AboutGalleryImage(models.Model):
    image = models.ImageField(upload_to='about_gallery_images/')

    def __str__(self):
        return self.image.name

class Speaker(models.Model):
    name = models.CharField(max_length=100)
    designation = models.CharField(max_length=100, blank=True, null=True)
    image = models.ImageField(upload_to='speakers/', blank=True, null=True)

    def __str__(self):
        return self.name

class Schedule(models.Model):
    day = models.CharField(max_length=50)
    time = models.TimeField()
    event = models.CharField(max_length=200)

    def __str__(self):
        return self.event

class Blog(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    category = models.CharField(max_length=100, blank=True, null=True)
    comments = models.IntegerField(default=0)
    image = models.ImageField(upload_to='blog/', blank=True, null=True)

    def __str__(self):
        return self.title

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return self.name

class Event(models.Model):
    title = models.CharField(max_length=200)
    date = models.DateField()
    location = models.CharField(max_length=200)
    image = models.ImageField(upload_to='events/', blank=True, null=True)

    def __str__(self):
        return self.title

class TicketBook(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    mobile = models.CharField(max_length=15)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    date_booked = models.DateField()

    def __str__(self):
        return self.name

class User(models.Model):
    fname = models.CharField(max_length=100)
    lname = models.CharField(max_length=100)
    address = models.TextField()
    email = models.EmailField()
    mobile = models.CharField()
    password = models.CharField(max_length=100)
    profile_picture = models.ImageField(upload_to='profile_picture/')


    def __str__(self):
        return self.fname+" " + self.lname
    