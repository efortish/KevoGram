"""KevoGram Middleware catalog"""

#Django
from django.shortcuts import redirect
from django.urls import reverse

class ProfileCompletionMiddleware:
    """
    Profile completion middleware:
    Ensure each user who is interacting with the app have
    their profile pic and biography
    """

    def __init__(self, get_response) -> None:
        """Middleware initialization"""
        self.get_response = get_response

    def __call__(self, request):
        """Code to be executed for each request before the view is called"""
        if not request.user.is_anonymous:
            if not request.user.is_staff:
                profile = request.user.profile
                if not profile.picture or not profile.biography:
                    if request.path not in [reverse('users:update_profile'), reverse('users:logout'), reverse('users:signup')]:
                        return redirect('users:update_profile')
        response = self.get_response(request)
        return response