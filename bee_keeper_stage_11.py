# === Stage 11: Постраничный вывод ===
# Project: BeeKeeper
from typing import List, Tuple


def paginate(items: List, page: int, page_size: int) -> Tuple[List, int, int]:
    page = max(1, page)
    page_size = max(1, page_size)
    total_pages = max(1, (len(items) + page_size - 1) // page_size)
    page = min(page, total_pages)
    start = (page - 1) * page_size
    end = start + page_size
    return items[start:end], page, total_pages


def parse_page_params(raw: str) -> Tuple[int, int]:
    tokens = [t.strip() for t in raw.replace(",", " ").split()]
    page = int(tokens[0])
    page_size = int(tokens[1]) if len(tokens) > 1 else 20
    return page, page_size
