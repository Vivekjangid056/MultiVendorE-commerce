# from .models import *
# @receiver(post_save, sender = User)
# def post_save_create_profile_reciever(sender, instance, created, **kwargs):
#     print(created)
#     if created:
#         UserProfile.objects.create(user = instance)
#         print("user profile is created")
#     else:
#         try:
#             profile = UserProfile.objects.get(User = instance)
#             profile.save()
#             print("user profile is updated")
#         except:
#             UserProfile.objects.create(user = instance)
#             print("user profile was not created so I created one")


# # post_save.connect(post_save_create_profile_reciever, sender=User)