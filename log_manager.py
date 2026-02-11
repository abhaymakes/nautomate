import rich
from rich.console import Console
from rich.text import Text

class Logger(Console):

    def error(self, message: str):
        self.print(f"[bold red][*] {message}[/bold red]")

    def warning(self, message: str):
        self.print(f"[bold yellow][*] {message}[/bold yellow]")

    def info(self, message: str):
        self.print(f"[bold blue_violet][*] {message}[/bold blue_violet]")

    def success(self, message: str):
        self.print(f"[bold green1][*] {message}[/bold green1]")
    


if __name__ == "__main__":
    logger = Logger()

    logger.success("This is a success message.")
    logger.info("This is an informational message.")
    logger.warning("This is a warning message.")
    logger.error("This is an error message.")
