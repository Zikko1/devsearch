from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import Profile
from django.core.mail import send_mail
from django.conf import settings

# SIGNALS WHEN USER IS CREATED
#@receiver(post_save,sender=Profile)
def createProfile(sender,instance,created,**kwargs):
     if created:
         user = instance
         profile = Profile.objects.create(
            user = user,
            username = user.username,
            email = user.email,
            name = user.first_name,
         )

         subject = 'Welcome to DevSearch'
         message = 'Thank you for creating an account,kindly complete your profile'

         send_mail(
            subject,
            message,
            settings.EMAIL_HOST_USER,
            [profile.email],
            fail_silently=False,
         )

# UPDATE USER SIGNAL FUNCTION
def updateUser(sender,instance,created,**kwargs):
    profile = instance
    user = profile.user
    if created == False:
        user.first_name = profile.name
        user.username = profile.username
        user.email = profile.email
        user.save()


# SIGNALS WHEN USER IS DELETED
def deleteUser(sender, instance, **kwargs):
    try:
        user = instance.user
        user.delete()
    except:
        pass

post_save.connect(createProfile,sender=User)

post_save.connect(updateUser,sender=Profile)

post_delete.connect(deleteUser,sender=Profile)
