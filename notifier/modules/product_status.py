from enum import Enum

class Status(Enum):
    NOTIFY_STOCK = 1
    NOTHING = 2
    FAIL = 3
    PAGE_CHANGED_SHOULD_NOTIFY = 4
    PAGE_CHANGED = 5
