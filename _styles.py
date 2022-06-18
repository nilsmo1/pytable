from __future__ import annotations
from typing import Optional, Dict
from enum import Enum, auto

class Charset:
    styles = {
            "bold"    : "━┃┏┓┗┛┣┫┳┻╋",
            "double"  : "═║╔╗╚╝╠╣╦╩╬",
            "regular" : "─│┌┐└┘├┤┬┴┼"
            }

    def __init__(self, *, style: Optional[str]=None) -> None:
        self.style = "regular" if style is None or style not in Charset.styles else style
        self.hbar  = Charset.styles[self.style][0 ] # horizontal bar
        self.vbar  = Charset.styles[self.style][1 ] # vertical bar
        self.ulc   = Charset.styles[self.style][2 ] # upper left corner
        self.urc   = Charset.styles[self.style][3 ] # upper right corner
        self.llc   = Charset.styles[self.style][4 ] # lower left corner
        self.lrc   = Charset.styles[self.style][5 ] # lower right corner
        self.vrbar = Charset.styles[self.style][6 ] # vertical bar + right bar
        self.vlbar = Charset.styles[self.style][7 ] # vertical bar + left bar
        self.hdbar = Charset.styles[self.style][8 ] # horizontal bar + down bar
        self.hubar = Charset.styles[self.style][9 ] # horizontal bar + up bar
        self.vhbar = Charset.styles[self.style][10] # vertical bar + horizontal bar


class Justify(Enum):
    CENTER = auto()
    LEFT   = auto()
    RIGHT  = auto()
    
    @staticmethod
    def string_reps() -> Dict[str, Justify]:
        return {"center" : Justify.CENTER,
                "left"   : Justify.LEFT,
                "right"  : Justify.RIGHT}
