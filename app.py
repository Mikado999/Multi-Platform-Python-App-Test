import tkinter as tk

root = tk.Tk()
root.title("Cross-Platform App")
root.geometry("300x200")

label = tk.Label(root, text="Hello from GitHub Actions!", pady=20)
label.pack()

button = tk.Button(root, text="Close", command=root.destroy)
button.pack()

root.mainloop()
