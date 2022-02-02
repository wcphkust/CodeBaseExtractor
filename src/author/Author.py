from enum import Enum


class AuthorType(Enum):
    OWNER = 1
    OUTER_CONTRIBUTOR = 2
    STAR_OWNER = 3
    FORK_OWNER = 4


class Author:
    id = None
    type = None

    def __init__(self, p_id, p_type):
        self.id = p_id
        self.type = p_type
