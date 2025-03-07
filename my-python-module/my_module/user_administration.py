import os
import socket
import psutil

with open("my_file.txt", "r") as file:
    content = file.read()
    print(content)

def print_os_info():
    """Prints information about the operating system, CPU threads, and available RAM."""
    print("Operating system: ", os.name)
    print("Number of CPU threads: ", os.cpu_count())
    print("Available RAM: ", round(psutil.virtual_memory().total / (1024**3), 2), "GB")

