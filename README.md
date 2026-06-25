# T&A Corner

Інтернет-магазин парфумів на Django.

## Вимоги

- Python 3.10+
- pip

## Швидкий старт

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
python manage.py migrate
python manage.py load_demo_data   # optional: demo products from mockup
python manage.py createsuperuser
python manage.py runserver
```

Сайт: http://127.0.0.1:8000/  
Адмін-панель: http://127.0.0.1:8000/admin/

## Структура проєкту

```
config/          # Налаштування Django
shop/            # Каталог, бренди, парфуми
pages/           # Статичні сторінки (головна)
templates/       # HTML-шаблони
static/          # CSS, JS, зображення
media/           # Завантажені файли (товари, логотипи)
```

## Моделі

- **Category** — категорії парфумів
- **Brand** — бренди
- **Perfume** — товари (назва, ціна, обʼєм, зображення)

## Наступні кроки

- Інтеграція макету дизайну
- Кошик та оформлення замовлення
- Пошук і фільтри
