#!/usr/bin/python3
import psutil
import socket
import platform
from rich.console import Console
from rich.table import Table
from rich.live import Live
import time

console = Console()

def check_internet():
    """Test di connessione backend usando le socket"""
    try:
        # Tenta di connettersi al DNS di Google sulla porta 53
        # È molto più veloce di un ping perché lavora a basso livello
        socket.create_connection(("8.8.8.8", 53), timeout=1)
        return "[bold green]ONLINE[/bold green]"
    except OSError:
        return "[bold red]OFFLINE[/bold red]"

def get_system_status():
    table = Table(title="Fedora Advanced Monitor 🐧", style="bold blue")
    
    table.add_column("Componente", style="cyan")
    table.add_column("Stato/Utilizzo", justify="right")

    # Dati Sistema
    cpu = psutil.cpu_percent()
    ram = psutil.virtual_memory().percent
    
    # Aggiungiamo le righe
    table.add_row("Internet Status", check_internet())
    table.add_row("CPU Usage", f"{cpu}%")
    table.add_row("RAM Usage", f"{ram}%")
    table.add_row("OS Platform", platform.system())

    return table

# Esecuzione continua
try:
    with Live(get_system_status(), refresh_per_second=1) as live:
        while True:
            time.sleep(1)
            live.update(get_system_status())
except KeyboardInterrupt:
    console.print("\n[bold red]Monitor spento. Sfida completata! 🚀[/bold red]")
