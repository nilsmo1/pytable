from typing import Optional, List, Union
from _row import Row
from _styles import Charset, Justify

class Table:
    def __init__(self, *, title: Optional[str]=None, padding: int=1) -> None:
        self.title = title
        self.row_count = 0
        self.col_count = 0
        self.no_title = title is None
        self.rows = []
        self.layout: List[str]=[]
        self.padding = padding
    
    def pad(self, entry: str) -> None:
        return ' '*self.padding + entry + ' '*self.padding 

    def add_row(self, 
                *entries: str, 
                entry_count: Optional[int]=None, 
                justify: Union[List[str], str]="left") -> None:
        entries = list(entries) if entry_count is None or entries else [""]*entry_count
        if self.rows:
            cols = self.rows[0].get_entries()
            if len(entries) < len(cols):
                for _ in range(len(cols)-len(entries)):
                    entries.append("")
        entries = [self.pad(entry) for entry in entries]
        row = Row(*entries, entry_count=entry_count, justify=justify)
        self.rows.append(row)
        self.row_count += 1
        if not self.col_count: 
            self.col_count = len(entries)
        else:
            self.col_count = max(len(entries), self.col_count)

    def init_table(self, *, style: Optional[str]=None) -> None:
        cs = Charset(style=style)
        ws = []
        
        ws = [max(row.get_width(col=col) for row in self.rows) 
              for col in range(len(self.rows[0]))]
        
        layout = []

        # Title
        if not self.no_title:
            layout.append(f"{self.title:^{sum(ws)+self.col_count+1}}")

        # Top
        layout.append(cs.ulc + cs.hbar*ws[0])
        for w in ws[1:]:
            layout[-1] += cs.hdbar + cs.hbar*w
        layout[-1] += cs.urc
        
        # Rows and separators
        for j, row in enumerate(self.rows):
            layout.append("")
            for i, entry in enumerate(row.get_entries()):
                rj = row.justify[i]
                if rj == Justify.CENTER:
                    layout[-1] += f"{cs.vbar}{entry:^{ws[i]}}"

                elif rj == Justify.LEFT:
                    layout[-1] += f"{cs.vbar}{entry:<{ws[i]}}"

                elif rj == Justify.RIGHT:
                    layout[-1] += f"{cs.vbar}{entry:>{ws[i]}}"
            layout[-1] += cs.vbar
            if j != len(self.rows)-1: 
                layout.append(f"{cs.vrbar}{cs.hbar*ws[0]}")
                for w in ws[1:]:
                    layout[-1] += cs.vhbar + cs.hbar*w
                layout[-1] += cs.vlbar

        # Bottom
        layout.append(cs.llc + cs.hbar*ws[0])
        for w in ws[1:]:
            layout[-1] += cs.hubar + cs.hbar*w
        layout[-1] += cs.lrc

        self.layout = layout

    def display(self, *, style: Optional[str]=None) -> None:
        if not self.layout: self.init_table(style=style)
        for row in self.layout: print(row)

