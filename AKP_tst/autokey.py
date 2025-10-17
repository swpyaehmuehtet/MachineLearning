import tkinter as tk
import threading
import time
from pynput import keyboard
from pynput.keyboard import Key, Controller

class AutoPressApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Auto Key Presser")
        self.root.geometry("200x100")
        self.root.configure(bg='black')
        self.root.attributes('-topmost', True)
        self.root.overrideredirect(True)
        
        # Position window (adjust as needed)
        self.root.geometry(f"+{self.root.winfo_screenwidth() - 220}+10")
        
        # State variables
        self.active = False
        self.listener = None
        self.controller = Controller()
        
        # Create GUI elements
        self.status_label = tk.Label(
            root, 
            text="OFF", 
            font=("Arial", 24, "bold"), 
            fg="red", 
            bg="black"
        )
        self.status_label.pack(expand=True)
        
        # Toggle button
        self.toggle_btn = tk.Button(
            root, 
            text="TOGGLE", 
            command=self.toggle,
            bg="gray",
            fg="white",
            font=("Arial", 12)
        )
        self.toggle_btn.pack(fill="x")
        
        # Start key listener
        self.start_listener()
        
    def start_listener(self):
        self.listener = keyboard.Listener(on_press=self.on_press)
        self.listener.start()
        
    def on_press(self, key):
        try:
            if key.char == '`':  # Toggle with tilde key
                self.toggle()
        except AttributeError:
            if key == Key.esc:  # Stop with Escape key
                self.stop()
    
    def toggle(self):
        self.active = not self.active
        if self.active:
            self.status_label.config(text="ON", fg="green")
            self.toggle_btn.config(bg="green")
            threading.Thread(target=self.auto_press, daemon=True).start()
        else:
            self.status_label.config(text="OFF", fg="red")
            self.toggle_btn.config(bg="gray")
    
    def auto_press(self):
        while self.active:
            # Press Q twice
            self.controller.press('q')
            self.controller.release('q')
            time.sleep(0.1)
            self.controller.press('q')
            self.controller.release('q')
            
            time.sleep(1)  # Wait 1.5 seconds
            
            # Press F twice
            self.controller.press('f')
            self.controller.release('f')
            time.sleep(0.5)
            self.controller.press('f')
            self.controller.release('f')
            self.controller.press('f')
            self.controller.release('f')
            time.sleep(0.5)
            self.controller.press('f')
            self.controller.release('f')
            self.controller.press('f')
            self.controller.release('f')
            time.sleep(0.5)
            self.controller.press('f')
            self.controller.release('f')
            
            time.sleep(0.1)  # Small delay before next cycle
    
    def stop(self):
        self.active = False
        if self.listener:
            self.listener.stop()
        self.root.quit()

if __name__ == "__main__":
    root = tk.Tk()
    app = AutoPressApp(root)
    root.mainloop()