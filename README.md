# pytable
A simple table generator for terminal use, written in python.
***
## Files
| __Filename__ | __Description__ |
| :--- | :--- |
| [__table.py__](https://github.com/nilsmo1/pytable/blob/main/pytable/table.py) | The main file containing the `Table` class. |
| [__\_styles.py__](https://github.com/nilsmo1/pytable/blob/main/pytable/_styles.py) | A file containing the different border styles and justifications. Classes `Justify` and `Charset` are in this file. |
| [__\_row.py__](https://github.com/nilsmo1/pytable/blob/main/pytable/_row.py) | A file containing the `Row` class used in the table. |
| [__example.py__](https://github.com/nilsmo1/pytable/blob/main/example.py) | A quick example of a table. |

## Download and usage
```bash
$ git clone https://github.com/nilsmo1/pytable.git
$ cd pytable/
$ python3 example.py
```
```py
from pytable.table import Table
table = Table(title="Example table", padding=2)
table.add_row("example", "example 2", "ex", bold=True, italic=True)
table.add_row("e", "e", "e", justify=["left", "center", "right"])
table.add_row(entry_count=3)
table.add_row("hello")
table.display(style="double")
```
This code results in the following, the bold text does not show up here however.
```
          Example table           
╔═══════════╦═════════════╦══════╗
║  example  ║  example 2  ║  ex  ║
╠═══════════╬═════════════╬══════╣
║  e        ║      e      ║   e  ║
╠═══════════╬═════════════╬══════╣
║           ║             ║      ║
╠═══════════╬═════════════╬══════╣
║  hello    ║             ║      ║
╚═══════════╩═════════════╩══════╝
```

## Classes
### `Table`
| __Parameter__ | __Type__ | __Description__ |
| :--- | :--- | :--- | 
| __title__ | Optional[str]=None | The title of the table, justified center. || __padding__ | int=1 | How many spaces the cells are padded with to the left and right. |

| __Method__ | __Parameters__ | __Return type__ | __Description__ |
| :--- | :--- | :--- | :--- |
| __pad__ | entry: str | None | Pads a cell with padding specified at the initialisation of the class. |
| __format__ | entries: List[str], bold: bool,<br />bold_cells: Optional[List[int]],<br />italic: bool,<br />italic_cells: Optional[List[int]] | List[str] | Bolden and italicize given cells or all entries in the row if only `bold` and `italic` are given. |
| __add_row__ | \*entries: str,<br />entry_count: Optional[int]=None,<br />justify: Union[List[str], str]="left",<br />bold: bool=False,<br />bold_cells: Optional[List[int]]=None | None | Adds row with specified entries and justification. __entry_count__ can be used to create empty rows. If `bold` is `True` and `bold_cells` is not specified, all the entries in the row become bold. If `bold_cells` is specified, only the specified cells in the row become bold. |
| __init_table__ | style: Optional[str]=None | None | Initialises the layout of the table. |
| __display__ | style: Optional[str]=None | None | Prints the table. |

### `Row`
| __Parameter__ | __Type__ | __Description__ |
| :--- | :--- | :--- | 
| __\*entries__ | str | The text for each cell. |
| __entry_count__ | Optional[int]=None | How many colums the row should have. |
| __justify__ | Union[List[str], str]="left" | How the elements should formatted - left, right or center. |

| __Method__ | __Parameters__ | __Return type__ | __Description__ |
| :--- | :--- | :--- | :--- |
| __\_\_len\_\___ | - | int | Returns the entry count. |
| __\_\_iter\_\___ | - | Iterator[str] | Returns a iterator over the entries. |
| __get_entries__ | - | List[str] | Returns a list of the entries. |
| __get_width__ | col: Optional[int]=None | Union[List[int], int] | Returns the width of a cell if `col` is specified, otherwise return the widths of the entries. |

### `Charset`
| __Parameter__ | __Type__ | __Description__ |
| :--- | :--- | :--- | 
| style | Optional[str]=None | Choose the set style you want the table to be - "regular", "bold" or "double". Defaults to "regular". |

### `Justify(Enum)`
| __Method__ | __Parameters__ | __Return type__ | __Description__ |
| :--- | :--- | :--- | :--- |
| __string_reps__ | - | Dict[str, Justify] | (Staticmethod) Return the string representations of the justifications. |
