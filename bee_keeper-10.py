# === Stage 10: Группировка ===
# Project: BeeKeeper
from collections import Counter


def group_beeswarm_by_breed(beeswarms):
    breed_counts = Counter()
    for swarm in beeswarms:
        breed = swarm.get("breed")
        if breed is not None:
            breed_counts[breed] += 1
    return dict(breed_counts)


def group_beeswarm_by_breed_sorted(beeswarms):
    breed_counts = Counter()
    for swarm in beeswarms:
        breed = swarm.get("breed")
        if breed is not None:
            breed_counts[breed] += 1
    return sorted(breed_counts.items(), key=lambda item: (-item[1], item[0]))


def group_beeswarm_by_breed_detailed(beeswarms):
    groups = {}
    for swarm in beeswarms:
        breed = swarm.get("breed")
        if breed is None:
            continue
        groups.setdefault(breed, []).append(swarm)
    return groups


if __name__ == "__main__":
    sample_beeswarms = [
        {"name": "Улей А", "breed": "Италка", "strength": 8, "inspection_date": "2024-05-01"},
        {"name": "Улей Б", "breed": "Каштанка", "strength": 6, "inspection_date": "2024-05-02"},
        {"name": "Улей В", "breed": "Италка", "strength": 9, "inspection_date": "2024-05-03"},
        {"name": "Улей Г", "breed": "Италка", "strength": 7, "inspection_date": "2024-05-04"},
        {"name": "Улей Д", "breed": "Каштанка", "strength": 5, "inspection_date": "2024-05-05"},
    ]

    print("Группировка по породе (количество в каждой группе):")
    for breed, count in group_beeswarm_by_breed_sorted(sample_beeswarms):
        print(f"  {breed}: {count}")

    print("\nДетальная группировка:")
    for breed, group in group_beeswarm_by_breed_detailed(sample_beeswarms).items():
        print(f"  {breed}: {group}")
