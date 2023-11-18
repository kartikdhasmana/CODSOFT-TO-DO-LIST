import tkinter as tk

def add_task():
    task = entry.get()
    if task:
        listbox.insert(tk.END, task)
        entry.delete(0, tk.END)

def delete_task():
    try:
        task_index = listbox.curselection()[0]
        listbox.delete(task_index)
    except IndexError:
        pass

root = tk.Tk()
root.title("To-Do List")

#Changing background color to yellow
root.configure(bg='#FFFF99') # Use hex color code (light yellow)

frame = tk.Frame(root, bg='#FFFF99')  # Use hex color code(light yellow)
frame.pack(padx=10, pady=10)

listbox = tk.Listbox(frame, width=30, height=10, bg='#FFFFCC')  # Use hex color code(lighter yellow)
listbox.pack(side=tk.LEFT, padx=10)

scrollbar = tk.Scrollbar(frame, orient=tk.VERTICAL)
scrollbar.config(command=listbox.yview)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

listbox.config(yscrollcommand=scrollbar.set)

entry = tk.Entry(root, width=40)
entry.pack(padx=10, pady=5)

# Changing button colors to match the light yellow theme
add_button = tk.Button(root, text="Add Task", width=10, command=add_task, bg='#FFCC00')  # Use hex color code(yellow)
add_button.pack(padx=10, pady=5)

delete_button = tk.Button(root, text="Delete Task", width=10, command=delete_task, bg='#FF3300')  # Use hex color code(red-orange)
delete_button.pack(padx=10, pady=5)

root.mainloop()
