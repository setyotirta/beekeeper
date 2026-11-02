# === Stage 1: Каркас модуля ===
# Project: BeeKeeper
from dataclasses import dataclass, field
from datetime import date


@dataclass
class Hive:
    name: str
    breed: str
    strength: int
    inspection_date: date


def create_demo_hives() -> list[Hive]:
    return [
        Hive(name="Западный", breed="Итальянский", strength=8, inspection_date=date(2024, 5, 12)),
        Hive(name="Северный", breed="Карниколо", strength=5, inspection_date=date(2024, 5, 13)),
        Hive(name="Южный", breed="Итальянский", strength=10, inspection_date=date(2024, 5, 14)),
    ]


def main() -> None:
    hives = create_demo_hives()
    print("Добро пожаловать в BeeKeeper — дневник пасеки!")
    print(f"Загружено ульев: {len(hives)}")
    for hive in hives:
        print(
            f"Улей '{hive.name}' ({hive.breed}), "
            f"сила семьи: {hive.strength}, осмотр: {hive.inspection_date}"
        )


if __name__ == "__main__":
    main()
