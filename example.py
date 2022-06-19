if __name__ == "__main__":
    from pytable.table import Table
    table = Table(title="Example table", padding=2)
    table.add_row("example", "example 2", "ex", bold=True, italic=True)
    table.add_row("e", "e", "e", justify=["left", "center", "right"])
    table.add_row(entry_count=3)
    table.add_row("hello")
    table.display(style="double")

