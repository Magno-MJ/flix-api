from rest_framework import permissions

class GenrePermissionClass(permissions.BasePermission):
  def has_permission(self, request, view):
    if request.method in ['GET', 'OPTIONS', 'HEAD']:
      return request.user.has_permission('genres.view_genre')
    
    if request.method == 'POST':
      return request.user.has_permission('genres.add_genre')
    
    if request.method in ['PUT', 'PATCH']:
      return request.user.has_permission('genres.change_genre')
    
    if request.method == 'DELETE':
      return request.user.has_permission('genres.delete_genre')
    
    return False