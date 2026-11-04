# === Stage 2: Проверка полей ===
# Project: BeeKeeper
import datetime


def normalize_name(value):
    text = value.strip()
    if not text:
        return text
    words = []
    for token in text.split():
        if token.lower() in ("улей", "ул", "ус", "семья"):
            continue
        words.append(token)
    return " ".join(words).strip()


def normalize_breed(value):
    text = value.strip().lower()
    if not text:
        return text
    breed_map = {
        "кавказская": "Кавказская медовая",
        "италийская": "Италийская",
        "карниольская": "Карниольская",
        "украинская степная": "Украинская степная",
        "сибирская": "Сибирская",
        "лиманская": "Лиманская",
        "дештанская": "Дештанская",
        "бульдог": "Бульдог",
        "каштановый": "Каштановый",
        "серый": "Серый",
        "машонский": "Машонский",
    }
    return breed_map.get(text, value.strip())


def normalize_strength(value):
    text = value.strip().lower()
    if not text:
        return None
    strength_map = {
        "слабая": 1,
        "средняя": 2,
        "сильная": 3,
        "очень сильная": 4,
        "малочисленная": 1,
        "хорошая": 2,
        "отличная": 4,
    }
    return strength_map.get(text, None)


def normalize_date(value):
    if not value:
        return None
    candidate = value.strip()
    formats = ("%Y-%m-%d", "%d.%m.%Y", "%d/%m/%Y", "%m.%m.%Y", "%m-%d-%Y")
    for fmt in formats:
        try:
            return datetime.datetime.strptime(candidate, fmt).date()
        except ValueError:
            continue
    return None


def validate_hive(name, breed, strength, inspection_date):
    errors = []

    name = normalize_name(name)
    if not name:
        errors.append("Название улья обязательно для заполнения.")
    elif len(name) > 60:
        errors.append("Название улья не может превышать 60 символов.")

    breed = normalize_breed(breed)
    if not breed:
        errors.append("Порода пчел обязательно для заполнения.")

    strength = normalize_strength(strength)
    if strength is None:
        errors.append(
            "Сила семьи должна быть одной из: слабая, средняя, сильная, очень сильная."
        )

    inspection_date = normalize_date(inspection_date)
    if inspection_date is None:
        errors.append("Дата осмотра имеет неверный формат. Используйте ДД.ММ.ГГГГ.")
    else:
        today = datetime.date.today()
        if inspection_date > today:
            errors.append("Дата осмотра не может быть в будущем.")

    return name, breed, strength, inspection_date, errors
