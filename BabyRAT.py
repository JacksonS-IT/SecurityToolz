# Remote Access Tool

import socket
import threading
import os
import platform
import tkinter as tk
from tkinter import messagebox

class RemoteAccessTool:
    def __init__(self, master):
        self.master = master
        self.master.title("Remote Access Tool")
        self.master.geometry("400x300")

        self.label = tk.Label(master, text="Enter IP Address:")
        self.label.pack()

        self.ip_entry = tk.Entry(master)
        self.ip_entry.pack()

        self.connect_button = tk.Button(master, text="Connect", command=self.connect)
        self.connect_button.pack()

    def connect(self):
        ip_address = self.ip_entry.get()
        if self.validate_ip(ip_address):
            threading.Thread(target=self.remote_access, args=(ip_address,)).start()
        else:
            messagebox.showerror("Error", "Invalid IP Address")

    def validate_ip(self, ip):
        parts = ip.split('.')
        if len(parts) != 4:
            return False
        for part in parts:
            if not part.isdigit() or not 0 <= int(part) <= 255:
                return False
        return True

    def remote_access(self, ip_address):
        # Placeholder for remote access logic
        print(f"Connecting to {ip_address}...")

        # Example of platform-specific commands
        if platform.system() == "Windows":
            os.system(f"start cmd /k ping {ip_address}")
        elif platform.system() == "Linux":
            os.system(f"gnome-terminal -- ping {ip_address}")
        elif platform.system() == "Darwin":
            os.system(f"open -a Terminal ping {ip_address}")

if __name__ == "__main__":
    root = tk.Tk()
    app = RemoteAccessTool(root)
    root.mainloop()
