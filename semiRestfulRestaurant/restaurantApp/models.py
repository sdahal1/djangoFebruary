from django.db import models

#the purpose of this manager class is so that i can put methods in there that we can extend the functionality of the "objects" keyword
class MenuManager(models.Manager):
    #create a method here to validate the information from the form
    def menuCreationValidator(self, formInfo):
        errors = {}
        if len(formInfo['dishname']) == 0:
            errors['dishnameRequired'] = "The Name of the Menu item is required!"
        elif len(formInfo['dishname']) < 3:
            errors['3charsreq_dishName'] = "Dish Name must be at least 3 characters long"
        
        if len(formInfo['desc']) < 10:
            errors['desc10chars'] = "Description must be at least 10 characters long!"
        
        if float(formInfo['priceInput']) < 5:
            errors['priceNotexpensiveEnoughWebougieOutHere'] = "Please enter a higher price, organic foods are expensive!"

        

        return errors

    # def basic_validator(self, postData):
    #     errors = {}
    #     # add keys and values to errors dictionary for each invalid field
    #     if len(postData['name']) < 5:
    #         errors["name"] = "Blog name should be at least 5 characters"
    #     if len(postData['desc']) < 10:
    #         errors["desc"] = "Blog description should be at least 10 characters"
    #     return errors



# Create your models here.
class Menu(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = MenuManager()



