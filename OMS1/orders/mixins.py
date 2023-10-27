from django.shortcuts import redirect

class IsAuthenticatedMixin:
    def dispatch(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            return super().dispatch(request, *args, **kwargs)
        return redirect("user_login")
