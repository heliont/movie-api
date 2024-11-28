# File permissions de App Movies

from rest_framework import permissions


class MoviePermissionClass(permissions.BasePermission):

    def has_permission(self, request, view):
        # Lógica da Permissão
        # A permissão do usuário tem que esta adicionado a view desejada
        # passar no parametro do has_perm('app.view_model')

        if request.method in ['GET', 'OPTIONS', 'HEAD']:  # METODO SEGURO SEM PERMISSÃO DE ALTERAR DADOS
            return request.user.has_perm('movies.view_movie')

        if request.method == 'POST':
            return request.user.has_perm('movies.add_movie')

        if request.method in ['PUT', 'PATCH']:
            return request.user.has_perm('movies.change_movie')

        if request.method == 'DELETE':
            return request.user.has_perm('movies.delete_movie')

        return False