from enum import Enum


class Results(Enum):
    VALID = "VALID"
    INVALID = "INVALID"
    UNDETERMINED = "UNDETERMINED"
    OUT_OF_RANGE = "OUT OF RANGE"
    ERROR = "ERROR"
    COMMAND = "COMMAND"
    NULL = "NULL"
