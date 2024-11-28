from rest_framework import permissions


# Permissão global para todos os endpoints
class GlobalDefaultPermissions(permissions.BasePermission):

    # verificando a permissão para todos os endpoints
    def has_permission(self, request, view):
        model_permissions_codename = self.__get_model_permissions_codename(method=request.method, view=view)

        if not model_permissions_codename:
            return False

        # Verifica se o usuário possui a permissão do model e retorna o resultado
        return request.user.has_perm(model_permissions_codename)


    # Função para Coletar o Method, App, View e retorna na Class Global de permissão
    def __get_model_permissions_codename(self, method, view):
        try:
            model_name = view.queryset.model._meta.model_name # identifica o nome do model
            app_label =  view.queryset.model._meta.app_label #  identifica o nome do app
            action = self.__get_action_sufix(method) # identifica o nome do metodo da request
            return f'{app_label}.{action}_{model_name}'

        except AttributeError:
            return None


    # Função para identificar o metodo da requisição
    def __get_action_sufix(self, method):
        method_actions = {
            'GET': 'view',
            'POST': 'add',
            'PUT': 'change',
            'PATCH': 'change',
            'DELETE': 'delete',
            'OPTIONS': 'view',
            'HEAD': 'view',
        }
        return method_actions.get(method, '')