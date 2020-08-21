from rest_framework import permissions

class BlacklistPermission(permissions.BasePermission): #for not in blacklist only
    message = 'This IP is blocked for some good reasons., please contact if you think this is a mistake.'
    def has_permission(self, request, view):
        ip_addr = request.META['REMOTE_ADDR']
        blacklisted = Blacklist.objects.filter(ip_addr=ip_addr).exists()
        return not blacklisted

class AnonPermissionOnly(permissions.BasePermission): #for anonemus users only 
    message = 'You are already authenticated, Please logout and try again.'
    def has_permission(self, request, view):
        return not request.user.is_authenticated


class IsOwnerOrReadOnly(permissions.BasePermission): #for the owners only
    message = 'You are not the owner of this content. Access forbidden.'
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.owner == request.user
