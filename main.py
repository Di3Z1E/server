import tkinter as tk
import subprocess


class Application:
    def __init__(self, master):
        self.master = master
        self.master.geometry("800x600")
        self.master.title("Ping App")

        self.ping_button = tk.Button(master, text="Ping localhost", command=self.ping_localhost)
        self.ping_button.place(relx=0.5, rely=0.1, anchor=tk.N)

        self.ip_button = tk.Button(master, text="Get IP Config", command=self.get_ip_config)
        self.ip_button.place(relx=0.3, rely=0.2, anchor=tk.N)

        self.ls_button = tk.Button(master, text="List Files", command=self.list_files)
        self.ls_button.place(relx=0.7, rely=0.2, anchor=tk.N)

        self.label = tk.Label(master, text="CONSOLE (View Only)")
        self.label.place(relx=0.5, rely=0.63, anchor=tk.N)

        self.console = tk.Text(master, wrap=tk.WORD, bg="black", fg="white", state="disabled")
        self.console.place(relx=0, rely=0.67, relwidth=1, relheight=0.33)

    def ping_localhost(self):
        command = "ping -n 1 localhost"
        self.execute_command(command)

    def get_ip_config(self):
        command = "ipconfig"
        self.execute_command(command)

    def list_files(self):
        command = "dir"
        self.execute_command(command)

    def execute_command(self, command):
        result = subprocess.run(command, shell=True, text=True, capture_output=True)
        output = result.stdout

        self.console.config(state="normal")
        self.console.insert(tk.END, output)
        self.console.config(state="disabled")
        self.console.see(tk.END)


if __name__ == "__main__":
    root = tk.Tk()
    app = Application(root)
    root.mainloop()
