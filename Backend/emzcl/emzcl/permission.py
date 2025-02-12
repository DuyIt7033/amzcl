from emzcl.Helpers import renderResponse
from rest_framework.permissions import BasePermission

class IsSuperAdmin(BasePermission):
    def has_permission(self, request, view):
        if hasattr(request.user, 'role') and request.user.role == 'Super Admin':
            return True
        return False
    
    def __call__(self, request):
        # Corrected this line to call `has_permission()`
        if not self.has_permission(request, None):  # You need to pass `request` to the method
            return renderResponse(data='You are not authorized to access this page', message='You are not authorized to access this page', status=401)
        return None
