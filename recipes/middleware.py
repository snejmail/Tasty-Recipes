# from .models import Profile
#
#
# class ProfileMiddleware:
#     def __init__(self, get_response):
#         self.get_response = get_response
#
#     def __call__(self, request):
#         profile_exists = Profile.objects.exists()
#         request.profile_exists = profile_exists
#         response = self.get_response(request)
#         return response
