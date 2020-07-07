django-admin startproject myjango1
python/python3 manage.py startapp myapp1
python manage.py runserver
python manage.py makemigrations myapp1
python manage.py migrate

-----------------------------------------------------------------------------------------------
Model methods::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
-----------------------------------------------------------------------------------------------
class Person(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    birth_date = models.DateField()

    def baby_boomer_status(self):
        "Returns the person's baby-boomer status."
        import datetime
        if self.birth_date < datetime.date(1945, 8, 1):
            return "Pre-boomer"
        elif self.birth_date < datetime.date(1965, 1, 1):
            return "Baby boomer"
        else:
            return "Post-boomer"

    @property
    def full_name(self):
        "Returns the person's full name."
        return '%s %s' % (self.first_name, self.last_name)
-----------------------------------------------------------------------------------------------
Multi-table inheritance::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
-----------------------------------------------------------------------------------------------
    from django.db import models

    class Place(models.Model):
        name = models.CharField(max_length=50)
        address = models.CharField(max_length=80)

    class Restaurant(Place):
        serves_hot_dogs = models.BooleanField(default=False)
        serves_pizza = models.BooleanField(default=False)
-----------------------------------------------------------------------------------------------
Abstract base classes::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
-----------------------------------------------------------------------------------------------
Abstract base classes are useful when you want to put some common information into a number of other models. You write your base class and put abstract=True in the Meta class. This model will then not be used to create any database table. Instead, when it is used as a base class for other models, its fields will be added to those of the child class.

    from django.db import models

    class CommonInfo(models.Model):
        name = models.CharField(max_length=100)
        age = models.PositiveIntegerField()

        class Meta:
            abstract = True

    class Student(CommonInfo):
        home_group = models.CharField(max_length=5)
-----------------------------------------------------------------------------------------------
Meta inheritance:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
-----------------------------------------------------------------------------------------------
    from django.db import models

    class CommonInfo(models.Model):
        # ...
        class Meta:
            abstract = True
            ordering = ['name']

    class Student(CommonInfo):
        # ...
        class Meta(CommonInfo.Meta):
            db_table = 'student_info'
-----------------------------------------------------------------------------------------------
Django Model Fields::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
-----------------------------------------------------------------------------------------------
Field Name	            Class	                            Particular
--==--==--              -==-==                              --==--==--==
AutoField 	            class AutoField(**options)	        It An IntegerField that automatically increments.
BigAutoField	        class BigAutoField(**options)	    It is a 64-bit integer, much like an AutoField except that it is guaranteed to fit numbers from 1 to 9223372036854775807.
BigIntegerField	        class BigIntegerField(**options)	It is a 64-bit integer, much like an IntegerField except that it is guaranteed to fit numbers from  -9223372036854775808 to 9223372036854775807.
BinaryField	            class BinaryField(**options)	    A field to store raw binary data.
BooleanField	        class BooleanField(**options)	    A true/false field. The default form widget for this field is a CheckboxInput.
CharField	            class DateField(auto_now=False, auto_now_add=False, **options)	    It is a date, represented in Python by a datetime.date instance.
DateTimeField	        class DateTimeField(auto_now=False, auto_now_add=False, **options)	It is a date, represented in Python by a datetime.date instance.
DateTimeField	        class DateTimeField(auto_now=False, auto_now_add=False, **options)	It is used for date and time, represented in Python by a datetime.datetime instance.
DecimalField	        class DecimalField(max_digits=None, decimal_places=None, **options)	It is a fixed-precision decimal number, represented in Python by a Decimal instance.
DurationField	        class DurationField(**options)	                                    A field for storing periods of time.
EmailField	            class EmailField(max_length=254, **options)	                        It is a CharField that checks that the value is a valid email address.
FileField	            class FileField(upload_to=None, max_length=100, **options)	        It is a file-upload field.
FloatField	            class FloatField(**options)	                                        It is a floating-point number represented in Python by a float instance.
ImageField	            class ImageField(upload_to=None, height_field=None, width_field=None, max_length=100, **options)	It inherits all attributes and methods from FileField, but also validates that the uploaded object is a valid image.
IntegerField	        class IntegerField(**options)                                       It is an integer field. Values from -2147483648 to 2147483647 are safe in all databases supported by Django.
NullBooleanField	    class NullBooleanField(**options)	                                Like a BooleanField, but allows NULL as one of the options.
PositiveIntegerField	class PositiveIntegerField(**options)	                            Like an IntegerField, but must be either positive or zero (0). Values from 0 to 2147483647 are safe in all databases supported by Django.
SmallIntegerField	    class SmallIntegerField(**options)	                                It is like an IntegerField, but only allows values under a certain (database-dependent) point.
TextField	            class TextField(**options)	                                        A large text field. The default form widget for this field is a Textarea.
TimeField	            class TimeField(auto_now=False, auto_now_add=False, **options)	    A time, represented in Python by a datetime.time instance.