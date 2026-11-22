# === Stage 9: Поиск по нескольким словам ===
# Project: BeeKeeper
import re


def search_hives(hives, query):
    query = query.strip()
    if not query:
        return list(hives)

    terms = re.findall(r"-?[a-zA-Z0-9_]+", query)
    if not terms:
        return list(hives)

    required = [term for term in terms if not term.startswith("-")]
    excluded = set(term[1:] for term in terms if term.startswith("-"))
    pattern = re.compile(
        "|".join(re.escape(term) for term in required),
        re.IGNORECASE,
    )

    result = []
    for hive in hives:
        text = " ".join(
            str(getattr(hive, field, ""))
            for field in ("name", "breed", "strength", "inspection_date")
        )
        if not pattern.search(text):
            continue
        if any(term in text for term in excluded):
            continue
        result.append(hive)
    return result


def search_hives_by_name(hives, query):
    query = query.strip()
    if not query:
        return list(hives)

    terms = re.findall(r"-?[a-zA-Z0-9_]+", query)
    if not terms:
        return list(hives)

    required = [term for term in terms if not term.startswith("-")]
    excluded = set(term[1:] for term in terms if term.startswith("-"))
    pattern = re.compile(
        "|".join(re.escape(term) for term in required),
        re.IGNORECASE,
    )

    result = []
    for hive in hives:
        if not pattern.search(getattr(hive, "name", "")):
            continue
        if any(term in getattr(hive, "name", "") for term in excluded):
            continue
        result.append(hive)
    return result


if __name__ == "__main__":
    sample = [
        {"name": "Липа-1", "breed": "Карниол", "strength": 8, "inspection_date": "2024-06-01"},
        {"name": "Липа-2", "breed": "Италка", "strength": 5, "inspection_date": "2024-06-02"},
        {"name": "Груша-3", "breed": "Карниол", "strength": 9, "inspection_date": "2024-06-03"},
    ]

    print(search_hives(sample, "Карниол"))
    print(search_hives(sample, "Липа"))
    print(search_hives(sample, "-Липа"))
    print(search_hives(sample, "Карниол -Липа"))
    print(search_hives(sample, "Липа-1"))
    print(search_hives(sample, ""))
    print(search_hives(sample, "Липа -Груша"))

    print(search_hives_by_name(sample, "Карниол"))
    print(search_hives_by_name(sample, "-Липа"))
    print(search_hives_by_name(sample, ""))
