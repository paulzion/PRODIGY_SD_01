import tkinter as tk
from tkinter import ttk

def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def celsius_to_kelvin(celsius):
    return celsius + 273.15

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def fahrenheit_to_kelvin(fahrenheit):
    return (fahrenheit + 459.67) * 5/9

def kelvin_to_celsius(kelvin):
    return kelvin - 273.15

def kelvin_to_fahrenheit(kelvin):
    return (kelvin * 9/5) - 459.67

class TemperatureConverter(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Temperature Converter")
        self.geometry("300x200")
        
        # Create and place widgets
        self.create_widgets()
        
    def create_widgets(self):
        self.label_input = ttk.Label(self, text="Enter Temperature:")
        self.label_input.grid(column=0, row=0, padx=10, pady=10)
        
        self.temp_input = ttk.Entry(self)
        self.temp_input.grid(column=1, row=0, padx=10, pady=10)
        
        self.unit_var = tk.StringVar(value="Celsius")
        self.unit_menu = ttk.Combobox(self, textvariable=self.unit_var, values=["Celsius", "Fahrenheit", "Kelvin"])
        self.unit_menu.grid(column=1, row=1, padx=10, pady=10)
        
        self.convert_button = ttk.Button(self, text="Convert", command=self.convert_temp)
        self.convert_button.grid(column=1, row=2, padx=10, pady=10)
        
        self.result_label = ttk.Label(self, text="")
        self.result_label.grid(column=0, row=3, columnspan=2, padx=10, pady=10)
        
    def convert_temp(self):
        try:
            temp = float(self.temp_input.get())
            unit = self.unit_var.get()
            if unit == "Celsius":
                fahrenheit = celsius_to_fahrenheit(temp)
                kelvin = celsius_to_kelvin(temp)
                result = f"{temp} °C = {fahrenheit:.2f} °F = {kelvin:.2f} K"
            elif unit == "Fahrenheit":
                celsius = fahrenheit_to_celsius(temp)
                kelvin = fahrenheit_to_kelvin(temp)
                result = f"{temp} °F = {celsius:.2f} °C = {kelvin:.2f} K"
            else:  # Kelvin
                celsius = kelvin_to_celsius(temp)
                fahrenheit = kelvin_to_fahrenheit(temp)
                result = f"{temp} K = {celsius:.2f} °C = {fahrenheit:.2f} °F"
            self.result_label.config(text=result)
        except ValueError:
            self.result_label.config(text="Invalid input. Please enter a number.")

if __name__ == "__main__":
    app = TemperatureConverter()
    app.mainloop()
