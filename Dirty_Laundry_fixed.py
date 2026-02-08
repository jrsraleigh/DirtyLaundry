import tkinter as tk
from tkinter import Toplevel, Label, PhotoImage, messagebox
import subprocess
import sys
import os
import requests
import tempfile

__version__ = "1.0.1"


# Fix base dir for PyInstaller
def resource_path(relative):
    try:
        base = sys._MEIPASS
    except Exception:
        base = os.path.abspath(".")

    return os.path.join(base, relative)


BASE_DIR = resource_path(".")

TOOLS = {
    "Blackbird": resource_path("blackbird/blackbird.py"),
    "Sherlock": resource_path("sherlock/sherlock.py"),
    "Maigret": resource_path("maigret/maigret.py"),
}

GITHUB_REPO = "jrsraleigh/DirtyLaundry"


def check_for_updates():
    try:
        url = f"https://api.github.com/repos/{GITHUB_REPO}/releases/latest"
        data = requests.get(url, timeout=5).json()
        latest = data.get("tag_name", "").lstrip("v")

        if latest and latest != __version__:
            for a in data.get("assets", []):
                if a["name"].lower().endswith(".exe"):
                    return latest, a["browser_download_url"]

        return None, None

    except Exception:
        return None, None


def run_tool(path):

    if not os.path.exists(path):
        messagebox.showerror("Error", f"Tool not found:\n{path}")
        return

    subprocess.Popen([sys.executable, path], shell=False)


def make_button(root, text, command):

    btn = tk.Button(
        root,
        text=text,
        width=25,
        height=2,
        bg="red",
        fg="white",
        activebackground="darkred",
        font=("Helvetica", 12, "bold"),
        command=command
    )

    btn.bind("<Enter>", lambda e: btn.config(bg="darkred"))
    btn.bind("<Leave>", lambda e: btn.config(bg="red"))

    return btn


def show_splash(root, start_main):

    splash = Toplevel()
    splash.overrideredirect(True)
    splash.configure(bg="black")

    w, h = 420, 320

    x = (root.winfo_screenwidth() - w) // 2
    y = (root.winfo_screenheight() - h) // 2

    splash.geometry(f"{w}x{h}+{x}+{y}")

    try:
        logo = PhotoImage(file=resource_path("logo.png"))
        Label(splash, image=logo, bg="black").pack(pady=20)
        splash.logo = logo
    except:
        pass

    title = Label(
        splash,
        text="Dirty Laundry",
        fg="red",
        bg="black",
        font=("Helvetica", 24, "bold")
    )

    title.pack()


    def pulse(size=24, up=True):

        new = size + (1 if up else -1)
        title.config(font=("Helvetica", new, "bold"))

        if new >= 28:
            splash.after(80, lambda: pulse(new, False))
        elif new <= 24:
            splash.after(80, lambda: pulse(new, True))
        else:
            splash.after(80, lambda: pulse(new, up))


    pulse()

    splash.after(2500, lambda: [splash.destroy(), start_main()])
    splash.mainloop()


def start_gui():

    root = tk.Tk()
    root.title("Dirty Laundry")
    root.geometry("360x460")
    root.configure(bg="black")

    try:
        logo = PhotoImage(file=resource_path("logo.png"))
        Label(root, image=logo, bg="black").pack(pady=10)
        root.logo = logo
    except:
        Label(
            root,
            text="Dirty Laundry",
            fg="red",
            bg="black",
            font=("Helvetica", 22, "bold")
        ).pack(pady=10)


    for name, path in TOOLS.items():
        make_button(root, name, lambda p=path: run_tool(p)).pack(pady=8)


    make_button(root, "Exit", root.quit).pack(pady=15)

    root.mainloop()


if __name__ == "__main__":

    root = tk.Tk()
    root.withdraw()

    show_splash(root, start_gui)
