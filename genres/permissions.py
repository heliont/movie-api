# File permissions de App Genres

from rest_framework import permissions


# Descontinuado, pode ser ignorado
class GenrePermissionClass(permissions.BasePermission):

    def has_permission(self, request, view):
        # Lógica da Permissão
        # A permissão do usuário tem que esta adicionado a view desejada
        # passar no parametro do has_perm('app.view_model')

        # METODO SEGURO SEM PERMISSÃO DE ALTERAR DADOS
        if request.method in ['GET', 'OPTIONS', 'HEAD']:
            return request.user.has_perm('genres.view_genre')

        if request.method == 'POST':
            return request.user.has_perm('genres.add_genre')

        if request.method in ['PUT', 'PATCH']:
            return request.user.has_perm('genres.change_genre')

        if request.method == 'DELETE':
            return request.user.has_perm('genres.delete_genre')

        return False