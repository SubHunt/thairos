from django.shortcuts import render, redirect
from django.http import HttpResponseForbidden


def age_gate(request):
    """Страница подтверждения возраста"""
    if request.method == 'POST':
        if 'confirm' in request.POST:
            # Пользователь подтвердил возраст
            response = redirect('home')
            response.set_cookie('age_verified', 'true',
                                max_age=30*24*60*60)  # 30 дней
            return response
        else:
            # Отказ
            return HttpResponseForbidden("Доступ запрещён: вы должны быть старше 18 лет.")
    return render(request, 'pages/age_gate.html')


def home(request):
    """Главная страница после age gate"""
    # Проверка cookie (в реальности middleware будет это делать)
    return render(request, 'pages/home.html')


def brand_detail(request, slug):
    """Страница бренда"""
    # Заглушка
    return render(request, 'pages/brand_detail.html', {'slug': slug})


def product_list(request):
    """Список продуктов"""
    return render(request, 'pages/product_list.html')


def beer_brands(request):
    """Страница брендов пива"""
    # Список брендов с данными
    brands = [
        {
            'name': 'SINGHA',
            'image': '/static/logos/singha logo.png',
            'description': 'Классическое тайское пиво с мягким вкусом и ароматом хмеля.',
        },
        {
            'name': 'LEO',
            'image': '/static/logos/leo logo.jpg',
            'description': 'Популярное тайское пиво с освежающим вкусом и лёгкой горчинкой.',
        },
        {
            'name': 'Saigon Lager',
            'image': '/static/logos/SAIGON.png',
            'description': 'Вьетнамский лагер с чистым вкусом и золотистым цветом.',
        },
        {
            'name': 'Saigon Special',
            'image': '/static/logos/SAIGON.png',  # можно другую картинку, но пока та же
            'description': 'Особый сорт пива Saigon с более насыщенным вкусом.',
        },
        {
            'name': 'BIA HA NOI',
            'image': '/static/logos/SAIGON.png',  # нет отдельного лого, используем заглушку
            'description': 'Традиционное вьетнамское пиво из Ханоя.',
        },
        {
            'name': 'HANOI Premium',
            'image': '/static/logos/SAIGON.png',
            'description': 'Премиальное пиво с богатым вкусом и ароматом.',
        },
        {
            'name': 'TIGER',
            'image': '/static/logos/Tiger logo.png',
            'description': 'Сингапурское пиво с ярким характером и высокой газированностью.',
        },
        {
            'name': 'SAN MIGUEL',
            'image': '/static/logos/sun miguel logo.png',
            'description': 'Филиппинское пиво с лёгким солодовым вкусом.',
        },
        {
            'name': 'SAPPORO',
            'image': '/static/logos/SAPPORO.png',
            'description': 'Японское пиво с чистым и свежим вкусом.',
        },
        {
            'name': 'HARBIN',
            'image': '/static/logos/SAIGON.png',  # заглушка
            'description': 'Китайское пиво с мягким вкусом и лёгкой сладостью.',
        },
        {
            'name': 'TSINGTAO',
            'image': '/static/logos/SAIGON.png',  # заглушка
            'description': 'Одно из самых известных китайских пив, сбалансированный вкус.',
        },
        {
            'name': 'YANJING BEER',
            'image': '/static/logos/SAIGON.png',  # заглушка
            'description': 'Китайское пиво с традиционным рецептом.',
        },
        {
            'name': 'Valech Beer',
            'image': '/static/logos/Valech Logo.jpg',
            'description': 'Чешское пиво, сваренное по классическим технологиям.',
        },
    ]
    return render(request, 'pages/beer_brands.html', {'brands': brands})
