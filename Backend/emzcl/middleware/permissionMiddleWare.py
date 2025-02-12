from emzcl.Helpers import renderResponse
from rest_framework.permissions import BasePermission
class IsSuperAdmin(BasePermission):
    def has_permission(self, request, view):
        if hasattr(request.user, 'role') and request.user.role == 'Super Admin':
            return True
        return False
    
    def __call__(self, request):
        if not self.has_permission:
            return renderResponse(data = 'You are not authorized to access thí page',message='You are not authorized to access thí page', status=401)
        return None