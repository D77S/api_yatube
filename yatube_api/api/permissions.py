from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    '''Кастомный класс разрешений.'''

    def has_permission(self, request, view):
        '''Перегружаем метод разрешений уровня запроса.
        Возвращает True (запрос разрешён), только если юзер в запросе
        аутентифицирован, дал валидный токен.
        Безотносительно метода запроса, хоть GET, хоть POST.
        '''
        return request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        '''Перегружаем метод разрешений уровня объекта запроса.
        Возвращает True (доступ к объекту запроса разрешен), если
        автор объекта запроса равен юзеру из запроса.
        '''
        return obj.author == request.user
