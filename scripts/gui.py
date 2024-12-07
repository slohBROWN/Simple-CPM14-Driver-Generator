import tkinter as tk
from tkinter import messagebox
from driver import Driver  # Ensure this import is correct

class DriverApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Driver")

        # Rookie Checkbox
        self.is_rookie_var = tk.BooleanVar()
        self.rookie_checkbox = tk.Checkbutton(root, text="Rookie Driver", variable=self.is_rookie_var)
        self.rookie_checkbox.grid(row=0, column=0, pady=10)

        # Create Driver Button
        self.create_driver_button = tk.Button(root, text="Create Driver", command=self.create_driver)
        self.create_driver_button.grid(row=1, columnspan=2, pady=10)

        # Driver Information Display
        self.info_label = tk.Label(root, text="Driver Information:")
        self.info_label.grid(row=2, column=0, columnspan=2, pady=10)

        # Display Driver Details
        self.details_text = tk.Text(root, height=8, width=40)
        self.details_text.grid(row=3, column=0, columnspan=2, padx=10, pady=10)
        self.details_text.config(state=tk.DISABLED)  # Make text field non-editable

    def create_driver(self):
        is_rookie = self.is_rookie_var.get()

        # Create driver instance
        driver = Driver(is_rookie=is_rookie)

        # Prepare driver information text
        driver_info = f"Name: {driver.name}\nCountry: {driver.country}\n"
        driver_info += f"Age: {driver.age}\nPeak: {driver.peak}\nRookie: {driver.is_rookie}\n\n"
        driver_info += "Skills:\n"
        for skill, value in driver.skills.items():
            driver_info += f"{skill}: {value}\n"

        # Display the driver's information in the text field
        self.details_text.config(state=tk.NORMAL)  # Enable text field to edit
        self.details_text.delete(1.0, tk.END)  # Clear any existing text
        self.details_text.insert(tk.END, driver_info)  # Insert the new driver information
        self.details_text.config(state=tk.DISABLED)  # Disable editing again

        # Optional: Show a message box when the driver is created
        messagebox.showinfo("Driver Created", f"Driver {driver.name} has been created!")

# Set up the main Tkinter window
root = tk.Tk()
app = DriverApp(root)

root.mainloop()