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
            'slug': 'singha',
            'image': '/static/logos/singha logo.png',
            'description': 'Классическое тайское пиво с мягким вкусом и ароматом хмеля.',
        },
        {
            'name': 'SINGHA LIGHT',
            'slug': 'singha-light',
            'image': '/static/logos/light.jpeg',
            'description': 'Облегчённая версия легендарного тайского пива с пониженной калорийностью и крепостью.',
        },
        {
            'name': 'LEO',
            'slug': 'leo',
            'image': '/static/logos/leo logo.jpg',
            'description': 'Популярное тайское пиво с освежающим вкусом и лёгкой горчинкой.',
        },
        {
            'name': 'Saigon Lager',
            'slug': 'saigon-lager',
            'image': '/static/logos/SAIGON.png',
            'description': 'Вьетнамский лагер с чистым вкусом и золотистым цветом.',
        },
        {
            'name': 'SAN MIGUEL',
            'slug': 'san-miguel',
            'image': '/static/logos/sun miguel logo.png',
            'description': 'Филиппинское пиво с лёгким солодовым вкусом.',
        },
        {
            'name': 'SAPPORO',
            'slug': 'sapporo',
            'image': '/static/logos/SAPPORO.png',
            'description': 'Японское пиво с чистым и свежим вкусом.',
        },
        {
            'name': 'Saigon Special',
            'slug': 'saigon-special',
            'image': '/static/saigon_special/logo.jpg',
            'description': 'Особенное пиво премиум-класса из сердца Южного Вьетнама.',
        },
        {
            'name': 'BIA HA NOI',
            'slug': 'bia-ha-noi',
            'image': '/static/biahanoi/logo.png',
            'description': 'Оригинальное светлое пиво из Вьетнама, основанное в 1890 году.',
        },
        {
            'name': 'HANOI Premium',
            'slug': 'hanoi-premium',
            'image': '/static/hanoi_premium/logo.png',
            'description': 'Премиальное светлое пиво нового поколения из сердца Вьетнама.',
        },
        {
            'name': 'TIGER',
            'slug': 'tiger',
            'image': '/static/logos/Tiger logo.png',
            'description': 'Сингапурское пиво с ярким характером и высокой газированностью.',
        },
        {
            'name': 'HARBIN',
            'slug': 'harbin',
            'image': '/static/logos/SAIGON.png',  # заглушка
            'description': 'Китайское пиво с мягким вкусом и лёгкой сладостью.',
        },
        {
            'name': 'TSINGTAO',
            'slug': 'tsingtao',
            'image': '/static/logos/SAIGON.png',  # заглушка
            'description': 'Одно из самых известных китайских пив, сбалансированный вкус.',
        },
        {
            'name': 'YANJING BEER',
            'slug': 'yanjing-beer',
            'image': '/static/logos/SAIGON.png',  # заглушка
            'description': 'Китайское пиво с традиционным рецептом.',
        },
        {
            'name': 'Valech Beer',
            'slug': 'valech-beer',
            'image': '/static/logos/Valech Logo.jpg',
            'description': 'Чешское пиво, сваренное по классическим технологиям.',
        },
    ]
    return render(request, 'pages/beer_brands.html', {'brands': brands})


def about(request):
    """Страница 'О компании'"""
    return render(request, 'pages/about.html')
