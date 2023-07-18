from .models import Student
from django.db.models.signals import post_save, post_delete, pre_save, pre_delete
from django.dispatch import receiver
from profiles.models import Profile


# @receiver(post_save, sender=Profile)
# def create_student(sender, instance, created, **kwargs):
#     if created:
#         print('student pre saved!')
#         profile = instance
#         if profile.profile_type == 'student':
#             print('student pre saved!')
#             user_name_sliced = profile.user_name.split(' ')
#             if len(user_name_sliced) == 1:
#                 firstName = user_name_sliced[0]
#                 lastName = ''
#             else:
#                 firstName =  ' '.join(user_name_sliced[:-1])
#                 lastName = user_name_sliced[-1]
                
#             student = Student.objects.create(
#                                         first_name=firstName,
#                                         last_name=lastName,
#                                         profile=profile,
#                                         )
#             print('Student created!')

@receiver(post_delete, sender=Student)
def delete_student(sender, instance, **kwargs):
    print('student deleted!')
    profile = instance.profile
    profile.delete()