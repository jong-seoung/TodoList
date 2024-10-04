from rest_framework import permissions

class IsAuthorOrReadonly(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user.is_authenticated
    
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        
        if not hasattr(obj, "author"):
            return False
        
        return obj.author == request.user
    

class IsAuthenticatedAndOnwerOrReadonly(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated
    
    def has_object_permission(self, request, view, obj):
        if not hasattr(obj, "receiver"):
            return False
        
        return obj.receiver == request.user