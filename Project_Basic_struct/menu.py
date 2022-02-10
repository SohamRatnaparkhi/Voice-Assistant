from rich.console import Console
from rich.table import Table

def print_menu():
    table = Table(title="\nI can do the following :- ")

    table.add_column("S. No.", style="cyan", no_wrap=True)
    table.add_column("Task", style="magenta")
    table.add_column("Command", justify="left", style="green")

    table.add_row("1", "Speak Text entered by User", "Speak out the following text")
    table.add_row("2", "Search anything on Google", "Search on Google")
    table.add_row("3", "Search anything on Wikipedia", "Search on Wikipedia")
    table.add_row("4", "Read a MS Word(docx) document", "Read MS Word document")
    table.add_row("5", "Read a PDF document", "Read PDF document")
    table.add_row("6", "Read a book(PDF)", "Read a book ")

    console = Console()
    console.print(table)

print_menu()