# table-py
A simple table generator for terminal use, written in python.
***
## Files
| Filename | Description |
| :--- | :--- |
| __table.py__ | The main file containing the `Table` class. |
| __\_styles.py__ | A file containing the different border styles and justifications. Classes `Justify` and `Charset` are in this file. |
| __\_row.py__ | A file containing the `Row` class used in the table. |
| __example.py__ | A quick example of a table. |

## Download and usage
```bash
$ git clone https://github.com/nilsmo1/table-py.git
$ cd table-py/
$ python3 example.py
```
```py
from table-py.table import Table
table = Table(title="Example table", padding=2)
table.add_row("example", "example 2", "ex")
table.add_row("e", "e", "e", justify=["left", "center", "right"])
table.add_row(entry_count=3)
table.add_row("hello")
table.display(style="bold")
```

## Classes
`Table`
| Parameter | Type | Description |
| :--- | :--- | :--- | 
| __title__ | Optional[str]=None | The title of the table, justified center. || __padding__ | int=1 | How many spaces the cells are padded with to the left and right. |

| Method | Parameters | Return type | Description |
| :--- | :--- | :--- | :--- |
| __pad__ | entry: str | None | Pads a cell with padding specified at the initialisation of the class. |
| __add_row__ | \*entries: str, entry_count: Optional[int]=None, justify: Union[List[str], str]="left" | None | Adds row with specified entries and justification. __entry_count__ can be used to create empty rows. |
| __init_table__ | style: Optional[str]=None | None | Initialises the layout of the table. |
| __display__ | style: Optional[str]=None | None | Prints the table. |

`Row`
| Parameter | Type | Description |
| :--- | :--- | :--- | 
| __\*entries__ | str | The text for each cell. |
| __entry_count__ | Optional[int]=None | How many colums the row should have. |
| __justify__ | Union[List[str], str]="left" | How the elements should formatted - left, right or center. |

| Method | Parameters | Return type | Description |
| :--- | :--- | :--- | :--- |
| __\_\_len\_\___ | - | int | Returns the entry count. |
| __\_\_iter\_\___ | - | Iterator[str] | Returns a iterator over the entries. |
| __get_entries__ | - | List[str] | Returns a list of the entries. |
| __get_width__ | col: Optional[int]=None | Union[List[int], int] | Returns the width of a cell if `col` is specified, otherwise return the widths of the entries. |

`Charset`
| Parameter | Type | Description |
| :--- | :--- | :--- | 
| style | Optional[str]=None | Choose the set style you want the table to be - "regular", "bold" or "double". Defaults to "regular". |

`Justify(Enum)`
| Method | Parameters | Return type | Description |
| :--- | :--- | :--- | :--- |
| __string_reps__ | - | Dict[str, Justify] | (Staticmethod) Return the string representations of the justifications. |
