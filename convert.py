import tkinter as tk
from tkinter import filedialog, messagebox
import subprocess
import os

def show_exe_location(exe_file_path):
    messagebox.showinfo("Exe File Location", f"The exe file is located at:\n{exe_file_path}")

def browse_file():
    file_path = filedialog.askopenfilename(title="Select a Python file", filetypes=[("Python files", "*.py")])
    entry_path.delete(0, tk.END)
    entry_path.insert(0, file_path)

def browse_icon():
    icon_path = filedialog.askopenfilename(title="Select an icon file", filetypes=[("Icon files", "*.ico")])
    entry_icon.delete(0, tk.END)
    entry_icon.insert(0, icon_path)

def convert_to_exe():
    python_file_path = entry_path.get()
    icon_file_path = entry_icon.get()

    if python_file_path and python_file_path.endswith(".py"):
        cmd = ['pyinstaller', '--onefile', '--noconsole']

        if icon_file_path and icon_file_path.endswith(".ico"):
            cmd.extend(['--icon', icon_file_path])

        cmd.append(python_file_path)

        subprocess.run(cmd)

        exe_file_path = os.path.join('dist', os.path.basename(python_file_path).replace('.py', '.exe'))

        if os.path.exists(exe_file_path):
            output_label.config(text=f"Conversion completed. Exe file: {exe_file_path}", fg="green")
            show_exe_location(exe_file_path)  # แสดงตำแหน่งของไฟล์ exe

            # เปิดโฟลเดอร์หลังจากการแปลงไฟล์เสร็จสมบูรณ์
            subprocess.run(['explorer', '/select,', exe_file_path])
        else:
            output_label.config(text="Error in creating the exe file", fg="red")
    else:
        output_label.config(text="Please select a valid Python file.", fg="red")

def install_pyinstaller():
    subprocess.run(['pip', 'install', '-U', 'pyinstaller'])
    output_label.config(text="PyInstaller installed successfully.", fg="green")

# สร้างหน้าต่างหลัก
root = tk.Tk()
root.title("Python to Exe Converter")

# สร้างคอมโพเนนต์ของ GUI
label_path = tk.Label(root, text="Select a Python file:")
entry_path = tk.Entry(root, width=50)
button_browse = tk.Button(root, text="Browse", command=browse_file)

label_icon = tk.Label(root, text="Select an icon file (optional):")
entry_icon = tk.Entry(root, width=50)
button_browse_icon = tk.Button(root, text="Browse", command=browse_icon)

button_convert = tk.Button(root, text="Convert to Exe", command=convert_to_exe)
button_install_pyinstaller = tk.Button(root, text="Install PyInstaller", command=install_pyinstaller)
output_label = tk.Label(root, text="", fg="black")

# จัดวางคอมโพเนนต์ในหน้าต่าง
label_path.grid(row=0, column=0, padx=10, pady=10, sticky=tk.E)
entry_path.grid(row=0, column=1, padx=10, pady=10)
button_browse.grid(row=0, column=2, padx=10, pady=10)

label_icon.grid(row=1, column=0, padx=10, pady=10, sticky=tk.E)
entry_icon.grid(row=1, column=1, padx=10, pady=10)
button_browse_icon.grid(row=1, column=2, padx=10, pady=10)

button_convert.grid(row=2, column=0, columnspan=3, pady=10)
button_install_pyinstaller.grid(row=3, column=0, columnspan=3, pady=10)
output_label.grid(row=4, column=0, columnspan=3, pady=10)

# เริ่มการทำงานของโปรแกรมหลัก
root.mainloop()
