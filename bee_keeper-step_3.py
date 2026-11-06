# === Stage 3: Хранилище в памяти ===
# Project: BeeKeeper
beekeeper_storage.py

from datetime import date


class Beehive:
    """Улей пасеки.

    Attributes:
        name (str): название улья.
        breed (str): порода пчел.
        strength (int): сила семьи (1-10).
        inspection_date (date): дата последнего осмотра.
    """

    def __init__(self, name, breed, strength, inspection_date):
        self.name = name
        self.breed = breed
        self.strength = strength
        self.inspection_date = inspection_date

    def __repr__(self):
        return (
            f"Beehive(name={self.name!r}, breed={self.breed!r}, "
            f"strength={self.strength}, inspection_date={self.inspection_date})"
        )


class BeehiveStorage:
    """Простое хранилище ульев в памяти (словарь)."""

    def __init__(self):
        self._store = {}

    def add(self, beehive):
        """Добавить улей по его названию (уникальному ключу)."""
        self._store[beehive.name] = beehive
        return beehive

    def get(self, name):
        """Вернуть улей по названию или None."""
        return self._store.get(name)

    def list_all(self):
        """Вернуть список всех ульев в порядке добавления."""
        return list(self._store.values())

    def __len__(self):
        return len(self._store)


def main():
    storage = BeehiveStorage()

    storage.add(Beehive("Солнышко", "Карниол", 6, date(2025, 3, 12)))
    storage.add(Beehive("Тёмный конь", "Италка", 8, date(2025, 3, 14)))
    storage.add(Beehive("Лесная", "Карниол", 5, date(2025, 3, 15)))

    print(f"Всего ульев: {len(storage)}")
    for beehive in storage.list_all():
        print(" - ", beehive)

    found = storage.get("Тёмный конь")
    if found:
        print("Нашёл 'Тёмный конь':", found)

    missing = storage.get("Не существует")
    print("Проверка отсутствующего:", missing)


if __name__ == "__main__":
    main()
