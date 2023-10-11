import tkinter as tk
from tkinter import messagebox

class AppointmentSetterApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Jiffy Lube Appointment Setter")
        self.current_module = 0
        self.time_choices = ["9:00 AM", "11:00 AM", "1:00 PM", "3:00 PM", "5:00 PM"]
        self.create_title_screen()

    def create_title_screen(self):
        self.title_label = tk.Label(self.root, text="Jiffy Lube Appointment Setter", font=("Helvetica", 20))
        self.title_label.pack(pady=20)
        
        self.instruction_label = tk.Label(self.root, text="Please choose an available time to set an appointment")
        self.instruction_label.pack(pady=10)

        self.time_var = tk.StringVar()
        self.time_var.set(None)

        for time_choice in self.time_choices:
            rb = tk.Radiobutton(self.root, text=time_choice, variable=self.time_var, value=time_choice)
            rb.pack()

        self.set_appointment_button = tk.Button(self.root, text="Set Appointment", command=self.show_next_module)
        self.set_appointment_button.pack(pady=20)

    def show_next_module(self):
        if self.current_module == 0:
            selected_time = self.time_var.get()
            if not selected_time:
                messagebox.showwarning("Warning", "Please select an appointment time.")
                return

            self.title_label.destroy()
            self.instruction_label.destroy()
            self.set_appointment_button.destroy()
            self.create_describe_problems_module()
            self.current_module = 1
        elif self.current_module == 1:
            self.describe_problems.destroy()
            self.next_button.destroy()
            self.create_contact_information_module()
            self.current_module = 2
        elif self.current_module == 2:
            self.email_label.destroy()
            self.phone_label.destroy()
            self.email_entry.destroy()
            self.phone_entry.destroy()
            self.submit_button.destroy()
            self.show_success_message()

    def create_describe_problems_module(self):
        self.instruction_label = tk.Label(self.root, text="Describe the Car's Problems")
        self.instruction_label.pack(pady=20)
        
        self.describe_problems = tk.Text(self.root, height=5, width=40)
        self.describe_problems.pack(pady=10)
        
        self.next_button = tk.Button(self.root, text="Next", command=self.show_next_module)
        self.next_button.pack(pady=10)

    def create_contact_information_module(self):
        self.email_label = tk.Label(self.root, text="Email:")
        self.email_label.pack(pady=5)
        self.email_entry = tk.Entry(self.root)
        self.email_entry.pack(pady=5)

        self.phone_label = tk.Label(self.root, text="Phone Number:")
        self.phone_label.pack(pady=5)
        self.phone_entry = tk.Entry(self.root)
        self.phone_entry.pack(pady=5)

        self.submit_button = tk.Button(self.root, text="Submit Information", command=self.show_next_module)
        self.submit_button.pack(pady=20)

    def show_success_message(self):
        messagebox.showinfo("Success", "Appointment Successfully Set")

if __name__ == "__main__":
    root = tk.Tk()
    app = AppointmentSetterApp(root)
    root.mainloop()
