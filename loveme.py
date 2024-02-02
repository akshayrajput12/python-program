import tkinter as tk
from tkinter import messagebox

class LoveApp:
    def __init__(self, master):
        self.master = master
        master.title("ek baaat puchni hai")

        # Get screen width and height
        screen_width = master.winfo_screenwidth()
        screen_height = master.winfo_screenheight()

        # Set window size to full screen
        master.geometry(f"{screen_width}x{screen_height}")

        # Disable window close (X) button
        master.protocol("WM_DELETE_WINDOW", self.on_close)

        # Remove window decorations
        master.overrideredirect(True)

        # Make the window stay on top of others
        master.attributes("-topmost", True)

        self.label = tk.Label(master, text=" hello miss reva kya ek puchu tumse?")
        self.label.pack(pady=10)

        self.button = tk.Button(master, text="Ask", command=self.ask_for_love)
        self.button.pack(pady=10)

        # Disable Alt+F4 and keyboard keys
        master.bind("<Alt-F4>", self.do_nothing)
        master.bind("<Key>", self.do_nothing)

    def ask_for_love(self):
        response = messagebox.askquestion("Love Test", "DO YOU LOVE ME?")

        if response == 'yes':
            messagebox.showinfo("Success", " I LOVE YOU TOO ,aao phir thoda sa ishq karte hai ")
            self.master.destroy()
        else:
            # Call the function recursively to keep asking
            self.ask_for_love()

    def on_close(self):
        # Do nothing when the close button is pressed
        pass

    def do_nothing(self, event):
        # Do nothing when the specified events occur
        pass

if __name__ == "__main__":
    root = tk.Tk()
    app = LoveApp(root)
    root.mainloop()
