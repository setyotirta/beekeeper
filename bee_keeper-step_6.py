# === Stage 6: Связи между сущностями ===
# Project: BeeKeeper
beekeeper_module.py

from datetime import date


class Hive:
    """Улей: название, порода, сила семьи, дата последнего осмотра."""

    def __init__(self, name, breed, strength, last_inspection):
        self.name = name
        self.breed = breed
        self.strength = strength
        self.last_inspection = last_inspection


class Inspection:
    """Осмотр: ссылка на улей и содержимое осмотра."""

    def __init__(self, hive, notes, harvest, feeding):
        self.hive = hive
        self.notes = notes
        self.harvest = harvest
        self.feeding = feeding


def get_inspections_for_hive(hive, inspections):
    """Получить все осмотры для заданного улья и проверить целостность связи."""
    result = []
    for inspection in inspections:
        if inspection.hive is not None and inspection.hive.name == hive.name:
            result.append(inspection)
    return result


def check_integrity(inspections, hive_names):
    """Проверить, что каждый осмотр ссылается на существующий улей."""
    problems = []
    for inspection in inspections:
        if inspection.hive is None:
            problems.append(f"Осмотр без улья: {id(inspection)}")
        elif inspection.hive.name not in hive_names:
            problems.append(f"Осмотр с несуществующим ульем: {inspection.hive.name}")
    return problems


def main():
    hive_a = Hive("Солнечный", "Итальянский", 5, date(2024, 5, 1))
    hive_b = Hive("Лесной", "Кавказский", 4, date(2024, 4, 20))

    inspections = [
        Inspection(hive_a, "Хорошее состояние", 10, 2),
        Inspection(hive_a, "Мало расплода", 0, 1),
        Inspection(hive_b, "Активный рой", 15, 5),
        Inspection(None, "Пропущенный осмотр", 0, 0),
    ]

    hive_names = {hive.name for hive in (hive_a, hive_b)}
    problems = check_integrity(inspections, hive_names)
    if problems:
        print("Проблемы с целостностью:")
        for problem in problems:
            print(problem)
    else:
        print("Целостность проверена успешно")


if __name__ == "__main__":
    main()
