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
            'description': 'Светлое пиво европейского качества.',
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
            'image': '/static/alcofree/singha_soda/singha_logo.jpg',
            'description': 'Освежающий сокосодержащий напиток с лимоном из Таиланда.',
        },
        {
            'name': 'VINUT',
            'slug': 'vinut-sparkling',
            'image': '/static/alcofree/vinut/vinut_logo.png',
            'description': 'Сокосодержащий напиток премиум-класса из тропических фруктов Вьетнама.',
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
            'hero_image': '/static/alcofree/singha_soda/singha_logo.jpg',
            'description': 'Освежающий сокосодержащий напиток с лимоном из Таиланда.',
            'full_description': 'Singha Lemon Soda — это новая глава легендарной истории Boon Rawd Brewery, написанная для нового поколения. Напиток с уникальным вкусом — идеальное сочетание настоящей лимонной кислинки и игристой свежести, без сахара и без калорий.',
            'history': 'Это не просто газировка — это новая глава легендарной истории Boon Rawd Brewery, написанная для нового поколения. Singha Lemon Soda появилась по инициативе Бурита Бхиромбхакди — наследника основателя великой пивоварни — как ответ на запросы рынка и потребителей, ищущих напиток с уникальным вкусом. В 2020 году, когда мир переосмыслял своё отношение к здоровому образу жизни, Singha сделала смелый шаг: выпустила безалкогольный напиток, достойный имени легенды.',
            'philosophy': 'Singha Lemon Soda воплощает простую и честную идею: освежение не должно идти в ущерб здоровью. Это напиток, который прославляет игристость и идеальное сочетание настоящей лимонной кислинки — без сахара и с нулевым содержанием калорий. Он одинаково хорош и как самостоятельный напиток в жаркий день, и как основа для оригинальных миксов: Honey Lemon Soda, Raspberry Lemon Soda, Mint Lemon Soda, Soda Mojito Mocktail или Shandy Yor Yak Thai Eatery — фантазии нет предела.',
            'characteristics': [
                'Категория: Сокосодержащий безалкогольный напиток с лимонным соком',
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
            'name': 'VINUT',
            'slug': 'vinut-sparkling',
            'hero_image': '/static/alcofree/vinut/vinut_logo.png',
            'description': 'Сокосодержащий напиток премиум-класса из тропических фруктов Вьетнама.',
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
            'coffee_flavors': [
                {
                    'name': 'Латте',
                    'image': '/static/alcofree/vinut/cofffee/V_Mockup_250ml_Coffee late.png',
                    'description': 'Нежный кофейный напиток с молоком, идеальный баланс кофе и сливочности.',
                    'features': ['250 мл', 'Содержит молоко', 'Средняя крепость', 'Без искусственных ароматизаторов'],
                },
                {
                    'name': 'Айс кофе',
                    'image': '/static/alcofree/vinut/cofffee/V_Mockup_250ml_Ice Coffee.png',
                    'description': 'Освежающий холодный кофе с лёгкой сладостью, идеален для жаркого дня.',
                    'features': ['250 мл', 'Холодный напиток', 'Низкая калорийность', 'Без ГМО'],
                },
                {
                    'name': 'Капучино',
                    'image': '/static/alcofree/vinut/cofffee/V_Mockup_250ml_Coffee cappuchino.png',
                    'description': 'Классический итальянский кофе с воздушной молочной пенкой и насыщенным вкусом.',
                    'features': ['250 мл', 'Пышная пенка', 'Средняя обжарка', 'Без консервантов'],
                },
            ],
        },
    }

    brand = brands_data.get(slug)
    if not brand:
        from django.http import Http404
        raise Http404("Бренд не найден")

    return render(request, 'pages/juice_brand_detail.html', {'brand': brand})


def snacks_landing(request):
    """Лендинг-страница снеков Masita Singha"""
    product = {
        'name': 'Masita Singha Fried Seaweed',
        'title': 'Жареные водоросли Masita Singha 36 г',
        'subtitle': 'Хрустящий вкус моря',
        'description': 'Насладитесь настоящим вкусом корейской кухни с Masita Singha Fried Seaweed. Это не просто снек – это полезная альтернатива чипсам и сухарикам.',
        'logo': '/static/snacks/logo.png',
        'hero_image': '/static/snacks/Masita Original.png',
        'images': [
            '/static/snacks/Masita Original.png',
            '/static/snacks/masita spicy.jfif',
            '/static/snacks/masita-group.jpg',
            '/static/snacks/7a92eac02ade857a2c605f906ac024e62389b7e4_hq.jpg',
        ],
        'features': [
            'Идеальный хруст – водоросли обжариваются особым способом, оставаясь лёгкими и хрустящими.',
            'Чистый вкус – никакой горечи, только натуральная солёность водорослей.',
            '36 граммов – достаточно, чтобы утолить голод, но не оставить тяжести.',
            'Здоровый перекус – низкая калорийность, нет трансжиров, содержит природный йод.',
        ],
        'usage': [
            'Просто откройте и ешьте',
            'Покрошите в рис или лапшу',
            'Добавьте в салат вместо гренок',
        ],
        'composition': 'Морские водоросли, растительное масло, соль (возможны натуральные специи в зависимости от партии).',
        'storage': 'Хранить в сухом, прохладном месте при температуре до +25°C. После вскрытия плотно закрывать упаковку и употребить в течение 2–3 дней.',
        'characteristics': [
            'Вес — 36 г',
            'Тип — Жареные водоросли',
            'Вкус — Солоноватый, неострый',
            'Подходит для — Веганов, вегетарианцев',
            'Страна производства — Таиланд / Корея',
        ],
    }
    return render(request, 'pages/snacks_landing.html', {'product': product})


def snacks_brands(request):
    """Страница брендов снеков"""
    brands = [
        {
            'name': 'Masita',
            'slug': 'masita',
            'image': '/static/snacks/Masita/logo.png',
            'description': 'Корейские жареные водоросли с натуральным вкусом моря. Идеальный полезный перекус.',
        },
        {
            'name': 'RollnRoll',
            'slug': 'rollnroll',
            'image': '/static/snacks/RollnRoll/rollNrolllogo.png',
            'description': 'Вьетнамские спринг-роллы с начинкой из креветок и овощей. Хрустящее удовольствие.',
        },
    ]
    return render(request, 'pages/snacks_brands.html', {'brands': brands})


def snack_brand_detail(request, slug):
    """Детальная страница бренда снеков"""
    # Данные для брендов
    brands_data = {
        'masita': {
            'name': 'Masita',
            'title': 'Жареные водоросли Masita',
            'subtitle': 'Натуральный вкус моря',
            'description': 'Корейские жареные водоросли Masita — это идеальный полезный перекус с хрустящей текстурой и натуральным вкусом моря. Без искусственных добавок, консервантов и усилителей вкуса.',
            'logo': '/static/snacks/Masita/logo.png',
            'hero_image': '/static/snacks/Masita/original.png',
            'features': [
                'Идеальный хруст – водоросли обжариваются особым способом, оставаясь лёгкими и хрустящими.',
                'Чистый вкус – никакой горечи, только натуральная солёность водорослей.',
                '36 граммов – достаточно, чтобы утолить голод, но не оставить тяжести.',
                'Здоровый перекус – низкая калорийность, нет трансжиров, содержит природный йод.',
            ],
            'usage': [
                'Просто откройте и ешьте',
                'Покрошите в рис или лапшу',
                'Добавьте в салат вместо гренок',
            ],
            'composition': 'Морские водоросли, растительное масло, соль (возможны натуральные специи в зависимости от партии).',
            'storage': 'Хранить в сухом, прохладном месте при температуре до +25°C. После вскрытия плотно закрывать упаковку и употребить в течение 2–3 дней.',
            'characteristics': [
                'Вес — 36 г',
                'Тип — Жареные водоросли',
                'Вкус — Солоноватый, неострый',
                'Подходит для — Веганов, вегетарианцев',
                'Страна производства — Таиланд / Корея',
            ],
            'products': [
                {
                    'name': 'Original',
                    'image': '/static/snacks/Masita/original.png',
                    'description': 'Классический вкус морских водорослей с лёгкой солоноватостью.',
                    'tags': ['Классический', 'Неострый', 'Веганский'],
                },
                {
                    'name': 'Spicy',
                    'image': '/static/snacks/Masita/spicy.png',
                    'description': 'Острый вариант с добавлением корейских специй для любителей пикантного.',
                    'tags': ['Острый', 'Пикантный', 'Веганский'],
                },
            ],
            'benefits': [
                'НАСТОЯЩИЙ ВКУС МОРЯ',
                'БЕЗ КОНСЕРВАНТОВ',
                'НИЗКАЯ КАЛОРИЙНОСТЬ',
                'ИСТОЧНИК ЙОДА',
            ],
            'benefit_descriptions': {
                'НАСТОЯЩИЙ ВКУС МОРЯ': 'Водоросли собирают в чистых водах Жёлтого моря и бережно обжаривают, сохраняя натуральный вкус.',
                'БЕЗ КОНСЕРВАНТОВ': 'Никаких искусственных добавок, только натуральные ингредиенты.',
                'НИЗКАЯ КАЛОРИЙНОСТЬ': 'Всего 120 ккал на упаковку — идеально для тех, кто следит за фигурой.',
                'ИСТОЧНИК ЙОДА': 'Естественное содержание йода поддерживает здоровье щитовидной железы.',
            },
            'images': [
                '/static/snacks/Masita/original.png',
                '/static/snacks/Masita/spicy.png',
                '/static/snacks/masita-group.jpg',
                '/static/snacks/7a92eac02ade857a2c605f906ac024e62389b7e4_hq.jpg',
            ],
        },
        'rollnroll': {
            'name': 'RollnRoll',
            'title': 'Спринг-роллы RollnRoll',
            'subtitle': 'Хрустящее удовольствие из Вьетнама',
            'description': 'Вьетнамские спринг-роллы RollnRoll — это тонкое рисовое тесто с начинкой из свежих овощей и креветок, обжаренное до золотистой хрустящей корочки. Идеальная закуска к любому поводу.',
            'logo': '/static/snacks/RollnRoll/rollNrolllogo.png',
            'hero_image': '/static/snacks/RollnRoll/shrimp.png',
            'features': [
                'Аутентичный рецепт – приготовлено по традиционному вьетнамскому рецепту.',
                'Хрустящая текстура – двойная обжарка создаёт неповторимый хруст.',
                'Сбалансированная начинка – идеальное сочетание овощей и морепродуктов.',
                'Удобная упаковка – индивидуальная вакуумная упаковка сохраняет свежесть.',
            ],
            'usage': [
                'Разогреть в духовке 5–7 минут',
                'Подавать с соусом чили или сладким соусом',
                'Украсить свежей зеленью',
            ],
            'composition': 'Рисовое тесто, креветки, морковь, капуста, лук, специи, растительное масло.',
            'storage': 'Хранить в морозильной камере при температуре –18°C. После разморозки не замораживать повторно. Готовить без разморозки.',
            'characteristics': [
                'Вес — 250 г (10 шт.)',
                'Тип — Замороженные спринг-роллы',
                'Вкус — Креветочный или овощной',
                'Подходит для — Не веганский (креветки), веганский (овощной)',
                'Страна производства — Вьетнам',
            ],
            'products': [
                {
                    'name': 'С креветкой острые',
                    'image': '/static/snacks/RollnRoll/shrimp.png',
                    'description': 'Спринг-роллы с начинкой из сочных креветок и острых специй.',
                    'tags': ['Креветки', 'Острый', 'Морепродукты'],
                },
                {
                    'name': 'С грибами веган',
                    'image': '/static/snacks/RollnRoll/vegetable.png',
                    'description': 'Веганский вариант с грибами шиитаке и свежими овощами.',
                    'tags': ['Веганский', 'Грибы', 'Овощи'],
                },
            ],
            'benefits': [
                'АУТЕНТИЧНЫЙ РЕЦЕПТ',
                'ХРУСТЯЩАЯ ТЕКСТУРА',
                'СВЕЖИЕ ИНГРЕДИЕНТЫ',
                'БЫСТРОЕ ПРИГОТОВЛЕНИЕ',
            ],
            'benefit_descriptions': {
                'АУТЕНТИЧНЫЙ РЕЦЕПТ': 'Рецепт передан от вьетнамских шеф-поваров, сохраняя традиционный вкус.',
                'ХРУСТЯЩАЯ ТЕКСТУРА': 'Двойная обжарка в масле канола даёт непревзойдённый хруст.',
                'СВЕЖИЕ ИНГРЕДИЕНТЫ': 'Овощи и морепродукты доставляются ежедневно с местных рынков.',
                'БЫСТРОЕ ПРИГОТОВЛЕНИЕ': 'Достаточно 7 минут в духовке — и хрустящие роллы готовы.',
            },
            'images': [
                '/static/snacks/RollnRoll/shrimp.png',
                '/static/snacks/RollnRoll/vegetable.png',
                '/static/snacks/RollnRoll/0_0_695x600.webp',
                '/static/snacks/RollnRoll/0_0_695x600_2.webp',
            ],
        },
    }

    brand = brands_data.get(slug)
    if not brand:
        from django.http import Http404
        raise Http404("Бренд не найден")

    # Преобразуем benefit_descriptions в список словарей для удобства шаблона
    benefit_list = []
    for benefit_key in brand.get('benefits', []):
        benefit_list.append({
            'title': benefit_key,
            'description': brand.get('benefit_descriptions', {}).get(benefit_key, '')
        })
    brand['benefit_list'] = benefit_list

    return render(request, 'pages/snack_brand_detail.html', {'brand': brand})


def where_to_buy(request):
    """Страница 'Где купить'"""
    return render(request, 'pages/where_to_buy.html')


def terms(request):
    """Страница 'Условия сотрудничества'"""
    return render(request, 'pages/terms.html')
