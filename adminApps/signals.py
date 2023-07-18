from .models import Admin
from django.db.models.signals import post_save, post_delete, pre_save, pre_delete
from django.dispatch import receiver
from profiles.models import Profile


# @receiver(post_save, sender=Profile)
# def create_admin(sender, instance, created, **kwargs):
#     if created:
#         print('admin pre saved!')
#         profile = instance
#         if profile.profile_type == 'admin':
#             print('admin pre saved!')
#             user_name_sliced = profile.user_name.split(' ')
#             if len(user_name_sliced) == 1:
#                 firstName = user_name_sliced[0]
#                 lastName = ''
#             else:
#                 firstName =  ' '.join(user_name_sliced[:-1])
#                 lastName = user_name_sliced[-1]
                
#             admin = Admin.objects.create(
#                                         first_name=firstName,
#                                         last_name=lastName,
#                                         profile=profile,
#                                         )
#             print('admin created!')


@receiver(post_delete, sender=Admin)
def delete_admin(sender, instance, **kwargs):
    print('admin deleted!')
    profile = instance.profile
    profile.delete()
