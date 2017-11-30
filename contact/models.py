from django.db import models


class Person(models.Model):

    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    description = models.TextField(null=True)


class Address(models.Model):

    person_id = models.ForeignKey(Person, on_delete=models.CASCADE)
    city = models.CharField(max_length=64)
    street = models.CharField(max_length=64)
    street_number = models.IntegerField()
    home_number = models.IntegerField()


class Telephone(models.Model):

    person_id = models.ForeignKey(Person, on_delete=models.CASCADE)
    number = models.CharField(max_length=32)
    type = models.CharField(max_length=64, null=True)


class Email(models.Model):

    person_id = models.ForeignKey(Person, on_delete=models.CASCADE)
    address = models.CharField(max_length=64)
    type = models.CharField(max_length=64, null=True)


class Group(models.Model):

    name = models.CharField(max_length=128)
    description = models.TextField(null=True)
    people = models.ManyToManyField(Person)
