import enum

class MktStatus(enum.Enum):
    PreOpen = 'pre_open'
    Auction = 'auction'
    Open = 'open'
    Close = 'close'