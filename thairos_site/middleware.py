from django.http import HttpResponseRedirect
from django.urls import reverse


class AgeGateMiddleware:
    """Проверяет, прошёл ли пользователь возрастное подтверждение."""

    def __init__(self, get_response):
        self.get_response = get_response
        # Исключаемые пути (чтобы не попасть в бесконечный редирект)
        self.excluded_paths = [
            reverse('age_gate'),
            '/static/',
            '/media/',
            '/admin/',
        ]

    def __call__(self, request):
        # Проверяем, нужно ли проверять возраст
        if not self.should_check(request):
            return self.get_response(request)

        # Проверяем cookie
        if not request.COOKIES.get('age_verified'):
            # Перенаправляем на страницу age gate
            return HttpResponseRedirect(reverse('age_gate'))

        return self.get_response(request)

    def should_check(self, request):
        """Определяет, нужно ли проверять возраст для данного запроса."""
        path = request.path_info
        # Исключаем статику, медиа, админку и саму страницу age gate
        for excluded in self.excluded_paths:
            if path.startswith(excluded):
                return False
        return True
