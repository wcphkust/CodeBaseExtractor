from enum import Enum
from code.Code import *


class PatchStatus(Enum):
    OPEN = 1
    CLOSE = 2
    MERGE = 3


class Patch:
    id = None
    title = None
    body = None
    status = None
    author_id = None
    open_time = None
    code_changes = None
    comments = None
    close_time = None

    def __init__(self, p_id):
        self.id = p_id
        return

    # TODO
    def setTitle(self, p_title):
        return

    def setBody(self, p_body):
        return

    def setStatus(self, p_status):
        return

    def setAuthor(self, p_author_id):
        return

    def setOpenTime(self, p_open_time):
        return

    def setCodeChanges(self, p_code_changes):
        return

    def setComments(self, p_comments):
        return

    def setCloseTime(self, p_close_time):
        return
