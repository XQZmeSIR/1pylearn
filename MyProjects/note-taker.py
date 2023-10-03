import tkinter as tk
from tkinter import messagebox

def save_note():
    note = text.get("1.0", "end-1c")  # Get the text from the text widget
    with open("notes.txt", "a") as file:
        file.write(note + "\n")
    messagebox.showinfo("Note Saved", "Your note has been saved successfully.")

app = tk.Tk()
app.title("Note-taking App")

text = tk.Text(app, wrap=tk.WORD, height=10, width=40)
text.pack()

save_button = tk.Button(app, text="Save Note", command=save_note)
save_button.pack()

app.mainloop()
