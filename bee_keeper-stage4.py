# === Stage 4: Удаление и восстановление ===
# Project: BeeKeeper
import uuid


class SoftDeleteMixin:
    """Добавляет поля мягкого удаления к сущности «улей»."""

    def __init__(self, name, breed, strength):
        self.id = str(uuid.uuid4())
        self.name = name
        self.breed = breed
        self.strength = strength
        self.is_deleted = False

    def delete(self):
        self.is_deleted = True
        return self

    def restore(self):
        self.is_deleted = False
        return self

    @property
    def is_active(self):
        return not self.is_deleted


class Hive(SoftDeleteMixin):
    """Сущность «улей» с мягкой возможностью удаления и восстановлением."""

    def __init__(self, name, breed, strength):
        super().__init__(name, breed, strength)

    def delete(self):
        return super().delete()

    def restore(self):
        return super().restore()

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "breed": self.breed,
            "strength": self.strength,
            "is_deleted": self.is_deleted,
        }


def list_active_hives(hives):
    return [hive for hive in hives if hive.is_active]


def list_deleted_hives(hives):
    return [hive for hive in hives if not hive.is_active]


def get_hive(hives, hive_id):
    for hive in hives:
        if hive.id == hive_id:
            return hive
    return None


if __name__ == "__main__":
    hive1 = Hive("Солнечный", "Карлик", 8)
    hive2 = Hive("Тёмный", "Итальянец", 6)
    hive3 = Hive("Сильный", "Карлик", 10)

    all_hives = [hive1, hive2, hive3]

    print("Активные ульи:")
    for hive in list_active_hives(all_hives):
        print(f"  {hive.name} ({hive.breed}), сила={hive.strength}")

    hive2.delete()
    print("\nПосле удаления 'Тёмный':")
    print("Активные ульи:")
    for hive in list_active_hives(all_hives):
        print(f"  {hive.name} ({hive.breed})")

    print("\nУдалённые ульи:")
    for hive in list_deleted_hives(all_hives):
        print(f"  {hive.name} ({hive.breed})")

    deleted_hive = get_hive(all_hives, hive2.id)
    deleted_hive.restore()
    print("\nПосле восстановления 'Тёмный':")
    for hive in list_active_hives(all_hives):
        print(f"  {hive.name} ({hive.breed})")
