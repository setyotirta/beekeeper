# === Stage 8: Текстовый поиск ===
# Project: BeeKeeper
import re


def find_bees() -> list[dict]:
    return [
        {"название": "Солнышко", "порода": "Итальянская", "сила": 8, "дата": "2024-05-01"},
        {"название": "Медовый", "порода": "Карника", "сила": 6, "дата": "2024-05-02"},
        {"название": "Пчёлка", "порода": "Итальянская", "сила": 9, "дата": "2024-05-03"},
    ]


def highlight(text: str, match: str) -> str:
    if not match:
        return text
    pattern = re.compile(re.escape(match), re.IGNORECASE)
    return pattern.sub(
        lambda m: f"\033[1m{m.group(0)}\033[0m",
        text,
    )


def search_bees(bee_list: list[dict], query: str) -> list[dict]:
    query = query.strip()
    if not query:
        return bee_list

    results = []
    for bee in bee_list:
        haystacks = [bee.get("название", ""), bee.get("порода", ""), bee.get("сила", ""), bee.get("дата", "")]
        if any(query.lower() in value.lower() for value in haystacks):
            hits = []
            for key in ("название", "порода", "сила", "дата"):
                value = bee.get(key, "")
                if value and query.lower() in value.lower():
                    hits.append(f"{key}: {highlight(str(value), query)}")
            results.append({"bee": bee, "hits": hits})

    return results


def print_bees(bee_list: list[dict]) -> None:
    for bee in bee_list:
        print(f"Название: {bee['название']}, Порода: {bee['порода']}, Сила: {bee['сила']}, Дата: {bee['дата']}")


def main() -> None:
    bees = find_bees()
    query = input("Введите поисковый запрос: ").strip()
    results = search_bees(bees, query)
    if not results:
        print("Ничего не найдено")
        return
    for item in results:
        bee = item["bee"]
        print(f"Название: {bee['название']}, Порода: {bee['порода']}, Сила: {bee['сила']}, Дата: {bee['дата']}")
        for hit in item["hits"]:
            print(f"    {hit}")


if __name__ == "__main__":
    main()
