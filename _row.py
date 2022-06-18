from typing import Optional, List, Iterator, Union
from _styles import Justify

class Row:
    def __init__(self, 
                 *entries: str, 
                 entry_count: Optional[int]=None,
                 justify: Union[List[str], str]="left") -> None:
        self.entry_count = entry_count if entry_count is not None else len(entries)
        self.entries = list(entries) if entries else ["" for _ in range(entry_count)] 
        jstf_dict = Justify.string_reps()
        if isinstance(justify, str):
            self.justify = [jstf_dict[justify.lower()] if justify.lower() in jstf_dict else Justify.LEFT]
        else:
            self.justify = [jstf_dict[j.lower()] if j.lower() in jstf_dict else Justify.LEFT for j in justify]
        for _ in range(len(self.entries)-len(self.justify)): self.justify.append(Justify.LEFT)
    
    def __len__(self) -> int:
        return self.entry_count

    def __iter__(self) -> Iterator[str]:
        return iter(self.entries)

    def get_entries(self) -> List[str]:
        return self.entries

    def get_width(self, *, col: Optional[int]=None) -> Union[List[int], int]:
        bold_len = len("\033[1m\033[0m")
        if col is not None:
            if "\033[1m" in self.entries[col]: 
                print("col", len(self.entries[col])-bold_len)
                return len(self.entries[col])-bold_len
            return len(self.entries[col])
        widths = []
        for entry in self.entries:
            if "\033[1m" in entry:
                widths.append(len(entry)-bold_len)
            else: widths.append(len(entry))
        print(widths)
        return widths
