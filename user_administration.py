import os
import socket
import psutil

with open("my_file.txt", "r") as file:
  file.read()

def print_os_info():
  print("operating system: ", os.name)
  print("number of cpu threads: ", os.cpu_count())
  print("Available RAM: ", round(psutil.virtual_memory().total / (1024**3), 2), "GB")