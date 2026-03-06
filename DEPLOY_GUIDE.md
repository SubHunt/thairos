# 🚀 Деплой Thairos на Ubuntu VPS (194.156.118.98)

## Что ты получишь в итоге:
- Сайт работает на gunicorn
- Nginx проксирует запросы и отдаёт статику
- Systemd держит gunicorn живым после перезагрузки

---

## ШАГ 1 — Подключись к серверу

```bash
ssh root@194.156.118.98
```

---

## ШАГ 2 — Обнови систему и установи зависимости

```bash
apt update && apt upgrade -y
apt install -y python3 python3-pip python3-venv nginx git
```

---

## ШАГ 3 — Склонируй проект

```bash
mkdir -p /var/www/thairos
cd /var/www/thairos
git clone https://github.com/SubHunt/thairos.git .
```

---

## ШАГ 4 — Создай виртуальное окружение и установи пакеты

```bash
python3 -m venv venv
source venv/bin/activate
pip install django gunicorn
# Если есть requirements.txt:
# pip install -r requirements.txt
```

---

## ШАГ 5 — Загрузи продакшн-настройки

Скопируй файл `settings_prod.py` (из архива) на сервер:

```bash
# Прямо на сервере создай файл:
nano /var/www/thairos/thairos_site/settings_prod.py
# Вставь содержимое из settings_prod.py и сохрани (Ctrl+O, Enter, Ctrl+X)
```

Затем скажи Django использовать эти настройки:

```bash
export DJANGO_SETTINGS_MODULE=thairos_site.settings_prod
```

Чтобы это применялось всегда, добавь в `/etc/environment`:
```bash
echo 'DJANGO_SETTINGS_MODULE=thairos_site.settings_prod' >> /etc/environment
```

---

## ШАГ 6 — Собери статику и примени миграции

```bash
cd /var/www/thairos
source venv/bin/activate

# Создай папки для статики
mkdir -p /var/www/thairos/static /var/www/thairos/media

# Собери статику
python manage.py collectstatic --settings=thairos_site.settings_prod --no-input

# Миграции (нужны для django.contrib.admin и сессий)
python manage.py migrate --settings=thairos_site.settings_prod
```

---

## ШАГ 7 — Настрой права доступа

```bash
chown -R www-data:www-data /var/www/thairos
chmod -R 755 /var/www/thairos
```

---

## ШАГ 8 — Установи systemd-сервис для gunicorn

```bash
# Создай папку для логов
mkdir -p /var/log/gunicorn
# Права на доступ
chown -R www-data:www-data /var/log/gunicorn
# Скопируй файл gunicorn.service (из архива) на сервер:
nano /etc/systemd/system/gunicorn.service
# Вставь содержимое из gunicorn.service, сохрани

# Запусти и включи автостарт
systemctl daemon-reload
systemctl start gunicorn
systemctl enable gunicorn

# Проверь статус — должно быть "active (running)"
systemctl status gunicorn
```

---

## ШАГ 9 — Настрой Nginx
```bash
# Установка nginx
apt install -y nginx

# Скопируй файл thairos_nginx.conf (из архива) на сервер:
nano /etc/nginx/sites-available/thairos
# Вставь содержимое из thairos_nginx.conf, сохрани

# Активируй сайт
ln -s /etc/nginx/sites-available/thairos /etc/nginx/sites-enabled/
rm -f /etc/nginx/sites-enabled/default

# Проверь конфиг
nginx -t

# Перезапусти nginx
systemctl restart nginx
systemctl enable nginx
```

---

## ШАГ 10 — Проверь сайт

Открой в браузере: **http://194.156.118.98**

Сайт должен работать! 🎉

---

## ШАГ 11 (опционально) — SSL-сертификат для thairos.ru

Если домен уже смотрит на сервер (DNS настроен):

```bash
apt install -y certbot python3-certbot-nginx
certbot --nginx -d thairos.ru -d www.thairos.ru
```
Да, этих двух команд достаточно! Certbot сам всё сделает:

Получит сертификат от Let's Encrypt
Автоматически обновит конфиг nginx (добавит HTTPS, порт 443)
Настроит автообновление сертификата каждые 90 дней

Единственное условие — DNS должен уже смотреть на сервер перед запуском certbot, иначе проверка домена не пройдёт. Когда настроишь DNS, просто подожди 10-30 минут пока записи обновятся, и запускай эти две команды.
В процессе certbot задаст пару вопросов — email для уведомлений и согласие с условиями. Всё остальное сделает сам. 🎉
Certbot сам обновит nginx-конфиг и добавит HTTPS.

---

## Полезные команды после деплоя

```bash
# Перезапустить gunicorn после изменений в коде
systemctl restart gunicorn

# Посмотреть логи gunicorn
tail -f /var/log/gunicorn/thairos-error.log

# Посмотреть логи nginx
tail -f /var/log/nginx/error.log

# Обновить код с GitHub
cd /var/www/thairos
git pull
python manage.py collectstatic --settings=thairos_site.settings_prod --no-input
systemctl restart gunicorn
```

---

## Структура файлов на сервере после деплоя

```
/var/www/thairos/          ← код проекта
/var/www/thairos/static/   ← собранная статика
/var/www/thairos/media/    ← загружаемые файлы
/var/www/thairos/venv/     ← виртуальное окружение
/etc/nginx/sites-available/thairos    ← nginx конфиг
/etc/systemd/system/gunicorn.service  ← systemd сервис
/var/log/gunicorn/         ← логи gunicorn
```
q -выход из просмотрщика текста
scp подойдёт. Но удобнее через Git — ты же уже склонировал репозиторий на сервер. Просто пушишь изменения на GitHub, а на сервере:
```bash
cd /var/www/thairos
git pull
```

    Что изменил                                     Дополнительная команда     
Python-код (views, models и т.д.)             systemctl restart gunicorn
Шаблоны HTML                                  ничего не нужно
Статику (CSS, JS, картинки)                   python manage.py collectstatic --settings=thairos_site.settings_prod --no-input

Всё сделали без Docker — классический способ: gunicorn + nginx + systemd прямо на сервере.
Docker для такого проекта действительно избыточен. Он реально полезен когда:

несколько сервисов (например, отдельно Django, отдельно БД, Redis, Celery и т.д.)
нужно одинаковое окружение у нескольких разработчиков
сложный деплой с оркестрацией (Kubernetes и т.п.)