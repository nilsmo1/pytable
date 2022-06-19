from typing import Optional, List, Iterator, Union
import _styles
Justify = _styles.Justify

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
        bold            = "\033[1m"
        italic          = "\033[3m"
        bold_italic     = "\033[1;3m"
        end_format      = "\033[0m"
        bold_len        = len(bold+end_format)
        italic_len      = len(italic+end_format)
        bold_italic_len = len(bold_italic+end_format)

        if col is not None:
            entry = self.entries[col]
            entry_len = len(entry)
            if bold in entry:                      return entry_len-bold_len
            elif italic in entry:                  return entry_len-italic_len
            elif bold_italic in self.entries[col]: return entry_len-bold_italic_len
            return entry_len
        widths = []
        for entry in self.entries:
            entry_len = len(entry)
            if bold in entry:          widths.append(entry_len-bold_len)
            elif italic in entry:      widths.append(entry_len-italic_len)
            elif bold_italic in entry: widths.append(entry_len-bold_italic_len)
            else:                      widths.append(entry_len)
        return widths
