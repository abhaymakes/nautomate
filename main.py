# Styling
from rich.console import Console
from rich_gradient import Text
from rich.prompt import Prompt

# Internal
import texts as text
from log_manager import Logger

# Scanners
from scans import host_discovery


console = Console()
log = Logger()

logo = """
░█▀█░█▀█░█░█░▀█▀░█▀█░█▄█░█▀█░▀█▀░█▀▀
░█░█░█▀█░█░█░░█░░█░█░█░█░█▀█░░█░░█▀▀
░▀░▀░▀░▀░▀▀▀░░▀░░▀▀▀░▀░▀░▀░▀░░▀░░▀▀▀                                                 

v1.0 - Made by [link=https://abhaymakes.github.io]abhaymakes[/link]
"""

console.print(
    Text(
        text.banner,
        colors=["#38bdf8", "#a855f7", "#f97316"],
        style="bold",
        justify="center",
    )
)

console.print(text.main_menu)

main_menu_choice = Prompt.ask("Select an option: ", choices=['1', '2', '3', '4', '5', '6', '7', '8', '9'], show_choices=False)

if main_menu_choice == "1":
    target = Prompt.ask("Enter an IP address or a .txt file path: ")
    host_discovery_scan_results = host_discovery(target)

    print(host_discovery_scan_results)

else:
    log.error('Invalid choice!')
