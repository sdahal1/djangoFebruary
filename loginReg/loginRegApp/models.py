from django.db import models
from datetime import date


class UserManager(models.Manager):
    def registrationValidator(self, formInfo):
        today = date.today()
        print("******")
        print(formInfo['birthday'])
        print(today)
        print("******")

        errors = {}
        if len(formInfo['fname']) == 0:
            errors['fnamereq'] = "First Name is required!"
        elif len(formInfo['fname']) < 2:
            errors['fnamelength'] = "First Name must be at least 2 characters!"

        if len(formInfo['lname']) == 0:
            errors['lnamereq'] = "Last Name is required!"

        if len(formInfo['email']) == 0:
            errors['emailreq'] = "email is required!"

        if len(formInfo['pw']) == 0:
            errors['pwReq'] = "Password is required!"
        elif len(formInfo['pw']) < 8:
            errors['pwlength'] = "Password must be at least 8 characters!"
        
        if formInfo['pw'] != formInfo['cpw']:
            errors['pwMatch'] = "Passwords must match!"

        if len(formInfo['birthday']) == 0:
            errors['bdayReq'] = "Birthday is required!"
        elif formInfo['birthday'] > str(today):
            errors['noFuturebday'] = "Birthday can't be in future!"
            
        

        return errors

# Create your models here.
class User(models.Model):
    firstName = models.CharField(max_length = 255)
    lastName = models.CharField(max_length = 255)
    email = models.CharField(max_length = 255)
    password = models.CharField(max_length = 255)
    birthday = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects= UserManager()


