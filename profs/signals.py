from .models import Prof
from django.db.models.signals import post_save, post_delete, pre_save, pre_delete
from django.dispatch import receiver
from profiles.models import Profile






# @receiver(post_save, sender=Profile)
# def create_prof(sender, instance, created, **kwargs):
#     if created:
#         print('prof pre saved!')
#         profile = instance
#         if profile.profile_type == 'prof':
#             print('prof pre saved!')
#             user_name_sliced = profile.user_name.split(' ')
#             if len(user_name_sliced) == 1:
#                 firstName = user_name_sliced[0]
#                 lastName = ''
#             else:
#                 firstName =  ' '.join(user_name_sliced[:-1])
#                 lastName = user_name_sliced[-1]
                
#             student = Prof.objects.create(
#                                         first_name=firstName,
#                                         last_name=lastName,
#                                         profile=profile,
#                                         )
#             print('Prof created!')

@receiver(post_delete, sender=Prof)
def delete_prof(sender, instance, **kwargs):
    print('prof deleted!')
    profile = instance.profile
    profile.delete()