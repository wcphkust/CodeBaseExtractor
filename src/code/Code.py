from enum import Enum


class ChangeMode(Enum):
    ADD = 1
    DELETE = 2
    INSERT = 3


class CodeChange:
    fileName = None
    commit_id = None
    mode = None
    startLine = None
    endLine = None

    def __init__(self, p_fileName, p_commit_id, p_mode, p_startLine, p_endLine):
        self.fileName = p_fileName
        self.commit_id = p_commit_id
        self.mode = p_mode
        self.startLine = p_startLine
        self.endLine = p_endLine
