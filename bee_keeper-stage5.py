# === Stage 5: Связанная сущность ===
# Project: BeeKeeper
import uuid
from datetime import date


class Inspection:
    def __init__(self, hive_id, notes="", temperature=None, humidity=None,
                 brood_pattern="нормально", queen_present=True, pests="нет",
                 inspection_date=None):
        self.id = uuid.uuid4().hex
        self.hive_id = hive_id
        self.notes = notes
        self.temperature = temperature
        self.humidity = humidity
        self.brood_pattern = brood_pattern
        self.queen_present = queen_present
        self.pests = pests
        self.inspection_date = inspection_date or date.today()


def add_inspection(inspections, hive_id, notes="", temperature=None,
                   humidity=None, brood_pattern="нормально",
                   queen_present=True, pests="нет", inspection_date=None):
    inspection = Inspection(
        hive_id=hive_id,
        notes=notes,
        temperature=temperature,
        humidity=humidity,
        brood_pattern=brood_pattern,
        queen_present=queen_present,
        pests=pests,
        inspection_date=inspection_date,
    )
    inspections.append(inspection)
    return inspection


def find_inspection(inspections, inspection_id):
    for inspection in inspections:
        if inspection.id == inspection_id:
            return inspection
    return None


def list_inspections_by_hive(inspections, hive_id):
    return [i for i in inspections if i.hive_id == hive_id]


def get_hive_last_inspection(inspections, hive_id):
    hive_inspections = list_inspections_by_hive(inspections, hive_id)
    if not hive_inspections:
        return None
    return max(hive_inspections, key=lambda i: i.inspection_date)


if __name__ == "__main__":
    inspections = []
    add_inspection(inspections, hive_id="hive_001", notes="Сильная семья, много расплода",
                   temperature=34.5, humidity=62, queen_present=True,
                   inspection_date=date(2024, 4, 15))
    add_inspection(inspections, hive_id="hive_001", notes="Требуется подкормка",
                   temperature=33.8, humidity=65, queen_present=True,
                   pests="варроа", inspection_date=date(2024, 4, 22))
    print(f"Всего осмотров: {len(inspections)}")
    print(f"Осмотры улья hive_001: {len(list_inspections_by_hive(inspections, 'hive_001'))}")
    print(f"Последний осмотр hive_001: {get_hive_last_inspection(inspections, 'hive_001')}")
