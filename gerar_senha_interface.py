import tkinter as tk
import secrets
import string


def generatePswd():
    size_pswd = int(input_size_pswd.get())
    items = string.ascii_letters + string.digits
    pswd = ''.join(secrets.choice(items) for _ in range(size_pswd))
    text_pswd.config(text=pswd)  # Update the label's text


window = tk.Tk()
window.geometry("500x400")

text_size_pswd = tk.Label(window, text="What password length do you want?", font=("Arial", 20))
text_size_pswd.pack(padx=10, pady=10)

input_size_pswd = tk.Entry(window, width=100, font=("Arial", 12))
input_size_pswd.pack(padx=10, pady=10)

button = tk.Button(window, text="Generate", width=100, font=("Arial", 16), command=generatePswd)
button.pack(padx=10, pady=10)

text_pswd = tk.Label(window, text='', font=("Arial", 16))
text_pswd.pack(padx=10, pady=10)

window.mainloop()
