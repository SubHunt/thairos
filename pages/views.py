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
            'name': 'KINGFISHER',
            'slug': 'kingfisher',
            'image': '/static/logos/Kingfisher_beer_logo.png',
            'description': 'Индийское премиальное светлое пиво, король хорошего времени.',
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


def juice_brands(request):
    """Страница брендов соков"""
    brands = [
        {
            'name': 'SINGHA SODA',
            'slug': 'singha-soda',
            'image': '/static/alcofree/singha_soda/original.png',
            'description': 'Освежающая содовая с лимоном из Таиланда.',
        },
        {
            'name': 'VINUT SPARKLING NFC JUICE',
            'slug': 'vinut-sparkling',
            'image': '/static/alcofree/vinut/watermelon.png',
            'description': 'Газированный сок премиум-класса из тропических фруктов Вьетнама.',
        },
    ]
    return render(request, 'pages/juice_brands.html', {'brands': brands})


def juice_brand_detail(request, slug):
    """Детальная страница бренда сока"""
    # Данные для брендов
    brands_data = {
        'singha-soda': {
            'name': 'SINGHA SODA',
            'slug': 'singha-soda',
            'hero_image': '/static/alcofree/singha_soda/original.png',
            'description': 'Освежающая содовая с лимоном из Таиланда.',
            'full_description': 'Singha Lemon Soda — это новая глава легендарной истории Boon Rawd Brewery, написанная для нового поколения. Напиток с уникальным вкусом — идеальное сочетание настоящей лимонной кислинки и игристой свежести, без сахара и без калорий.',
            'history': 'Это не просто газировка — это новая глава легендарной истории Boon Rawd Brewery, написанная для нового поколения. Singha Lemon Soda появилась по инициативе Бурита Бхиромбхакди — наследника основателя великой пивоварни — как ответ на запросы рынка и потребителей, ищущих напиток с уникальным вкусом. В 2020 году, когда мир переосмыслял своё отношение к здоровому образу жизни, Singha сделала смелый шаг: выпустила безалкогольный напиток, достойный имени легенды.',
            'philosophy': 'Singha Lemon Soda воплощает простую и честную идею: освежение не должно идти в ущерб здоровью. Это напиток, который прославляет игристость и идеальное сочетание настоящей лимонной кислинки — без сахара и с нулевым содержанием калорий. Он одинаково хорош и как самостоятельный напиток в жаркий день, и как основа для оригинальных миксов: Honey Lemon Soda, Raspberry Lemon Soda, Mint Lemon Soda, Soda Mojito Mocktail или Shandy Yor Yak Thai Eatery — фантазии нет предела.',
            'characteristics': [
                'Категория: Газированный безалкогольный напиток с лимонным соком',
                'Сахар: 0 г',
                'Калории: 0 ккал',
                'Кофеин: отсутствует',
                'Сертификат: Halal — подходит для мусульман и вегетарианцев',
                'Температура подачи: 4–6°С',
                'Формат: Банка 330 мл',
                'Общее для всей линейки: банка 330 мл • без кофеина • сертификат Halal • продукт Таиланда • Boon Rawd Brewery'
            ],
            'additional_images': [
                '/static/alcofree/singha_soda/banner5.jpg',
                '/static/alcofree/singha_soda/orig.webp',
                '/static/alcofree/singha_soda/c7dd42110697845.5ff3e95548623.webp',
            ],
            'flavors': [
                {
                    'name': 'Оригинальный',
                    'image': '/static/alcofree/singha_soda/original.png',
                    'description': 'Искристая лимонная содовая с кристальной прозрачностью. Чистый, терпкий вкус с лёгким цитрусовым ароматом — свежесть в тайском стиле.',
                    'features': ['0 сахара', '0 калорий', 'Halal', 'Высокое содержание витамина С'],
                },
                {
                    'name': 'Японская слива',
                    'image': '/static/alcofree/singha_soda/ume.png',
                    'description': 'Освежающий газированный напиток с ароматом японской сливы, идеально сочетающийся со вкусом настоящего лимонного сока и игристостью содовой — новое измерение свежести.',
                    'features': ['0 сахара', '0 калорий', '0 алкоголя', 'Halal', 'Высокое содержание витамина С'],
                },
                {
                    'name': 'Кремовый',
                    'image': '/static/alcofree/singha_soda/cream.png',
                    'description': 'Нежный и обволакивающий вкус — лимонная свежесть, смягчённая лёгкими сливочными нотами. Бархатистые пузырьки и деликатная кислинка создают ощущение лёгкого десерта в бокале.',
                    'features': ['0 сахара', '0 калорий', 'Halal', 'Высокое содержание витамина С'],
                },
                {
                    'name': 'Розовый',
                    'image': '/static/alcofree/singha_soda/pink.png',
                    'description': 'Сочетает свежую кислинку настоящего лимонного сока со сладким ароматом клубники и ассорти из тропических фруктов. Розовый цвет получен из натуральных фруктов и овощей, без искусственных красителей.',
                    'features': ['0 сахара', '0 калорий', 'Без искусственных красителей', 'Halal', 'Высокое содержание витамина С'],
                },
            ],
            'key_features': [
                'НАСТОЯЩИЙ ЛИМОННЫЙ СОК',
                'ИДЕАЛЬНАЯ ГАЗАЦИЯ',
                'БЕЗ САХАРА И КАЛОРИЙ',
                'СЕРТИФИКАТ HALAL',
            ],
        },
        'vinut-sparkling': {
            'name': 'VINUT SPARKLING NFC JUICE',
            'slug': 'vinut-sparkling',
            'hero_image': '/static/alcofree/vinut/watermelon.png',
            'description': 'Газированный сок премиум-класса из тропических фруктов Вьетнама.',
            'full_description': 'VINUT — это натуральные полезные напитки из тропических фруктов Вьетнама, приготовленные методом прямого отжима (NFC — Not From Concentrate). Все продукты изготовлены из 100% натуральных ингредиентов, без концентратов и без добавления консервантов.',
            'flavors': [
                {
                    'name': 'Арбуз',
                    'image': '/static/alcofree/vinut/watermelon.png',
                    'description': 'Восхитительное сочетание сладкого сочного арбузного вкуса и бодрящей газированной воды.',
                    'features': ['Не добавлен сахар', '110 ккал / банка', 'Без ГМО', 'Без консервантов'],
                },
                {
                    'name': 'Розовая гуава',
                    'image': '/static/alcofree/vinut/pink.png',
                    'description': 'Газированный фруктовый сок, сочетающий тропический вкус розовой гуавы с освежающей игристостью.',
                    'features': ['Не добавлен сахар', 'Низкое содержание калорий', 'Богат витамином C', 'Без искусственных красителей'],
                },
                {
                    'name': 'Маракуйя',
                    'image': '/static/alcofree/vinut/passion.png',
                    'description': 'Спелая маракуйя с местных ферм — яркий, истинный вкус маракуйи с кусочками мякоти.',
                    'features': ['Не добавлен сахар', 'Низкое содержание калорий', 'Богат калием и железом', 'Без ГМО'],
                },
                {
                    'name': 'Манго',
                    'image': '/static/alcofree/vinut/mango.png',
                    'description': 'Тропическое золото в банке — спелое манго, отжатое прямым методом без концентрирования.',
                    'features': ['Не добавлен сахар', 'Низкое содержание калорий', 'Богат витаминами C и A', 'Non-GMO'],
                },
            ],
            'key_features': [
                '85% НАТУРАЛЬНОГО СОКА',
                'NFC ТЕХНОЛОГИЯ (ПРЯМОЙ ОТЖИМ)',
                'БЕЗ САХАРА',
                'МЕЖДУНАРОДНЫЕ СЕРТИФИКАТЫ',
            ],
        },
    }

    brand = brands_data.get(slug)
    if not brand:
        from django.http import Http404
        raise Http404("Бренд не найден")

    return render(request, 'pages/juice_brand_detail.html', {'brand': brand})
