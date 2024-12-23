import threading
import time
import tkinter as tk
from tkinter import messagebox

from plyer import notification


def countdown(t, label, root):
    if t >= 0:
        mins, secs = divmod(t, 60)
        timer = f"{mins:02d}:{secs:02d}"
        label.config(text=timer)
        root.after(1000, countdown, t-1, label, root)
    
    # Notification to let user know timer is done
    else:
        notification.notify(
            title="Timer completed",
            message="Your countdown timer has ended!",
            timeout=10
        )
        messagebox.showinfo("Timer completed", "Your countdown has ended!")
        
def start_timer(entry, label, root):
    try:
        t = int(entry.get())
        entry.delete(0, tk.END)
        countdown(t, label, root)
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid numeber.")

def on_enter_key(event, entry, label, root):
    start_timer(entry, label, root)

#Create the gui here
def timer_gui():
    root = tk.Tk()
    root.title("Countdown Timer")
    root.geometry("600x300")
    
    tk.Label(root, text="Enter time in seconds:", font=("Helvetica", 20)).pack(pady=10)
    entry = tk.Entry(root, width=15, font=("Helvetica", 24))
    entry.pack()
    
    label = tk.Label(root, text="00:00", font=("Helvetica", 60))
    label.pack(pady=20)
    
    start_button = tk.Button(root, width=15, height=2, text="Start Timer", command=lambda: start_timer(entry, label, root))
    start_button.pack()
    
    root.bind('<Return>', lambda event: on_enter_key(event, entry, label, root))
    
    
    root.mainloop()
    
if __name__ == "__main__":
    timer_gui()