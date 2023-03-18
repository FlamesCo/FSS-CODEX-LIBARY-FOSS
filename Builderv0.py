import tkinter as tk
import os
from tkinter import messagebox

class FlamestopiaApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Flamestopia Standard Software 0.X.A - FT CODEX Builder")
        self.geometry("500x300")  # Set the window size
        self.resizable(False, False)  # Disable resizing of the window
        self.backup_button = tk.Button(self, text="Backup OS", command=self.backup)
        self.backup_button.pack(pady=20)

        # Add additional buttons and functionality to resemble Pinguy Builder here

    def backup(self):
        os.system("tar -cvpzf backup.tar.gz --exclude=/backup.tar.gz --exclude=/proc --exclude=/tmp --exclude=/mnt --exclude=/dev --exclude=/sys /")  # Create a backup of the entire OS
        messagebox.showinfo("Backup Complete", "The OS has been successfully backed up.")
        
    # Add additional methods for the other functionality to resemble Pinguy Builder

if __name__ == '__main__':
    app = FlamestopiaApp()
    app.mainloop()
