# === Stage 7: Генерация идентификаторов ===
# Project: BeeKeeper
import uuid
import datetime


PROJECT_PREFIX = "beekeeper"


def generate_unique_id() -> str:
    counter = 0
    while True:
        candidate = f"{PROJECT_PREFIX}-{uuid.uuid4().hex[:8]}-{counter}"
        counter += 1
        if not _is_taken(candidate):
            return candidate


def _is_taken(candidate: str) -> bool:
    return candidate in _used_ids


_used_ids: set[str] = set()


def register_id(candidate: str) -> None:
    _used_ids.add(candidate)


def clear_ids() -> None:
    _used_ids.clear()


def current_date() -> str:
    return datetime.date.today().isoformat()
