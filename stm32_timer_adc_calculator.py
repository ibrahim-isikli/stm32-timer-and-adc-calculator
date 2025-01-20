import tkinter as tk
from tkinter import messagebox

def calculate():
    try:
        result_text = ""
        
        # getting input values and setting default values
        clock_freq = float(clock_freq_entry.get()) if clock_freq_entry.get() else None
        prescaler = int(prescaler_entry.get()) if prescaler_entry.get() else None
        arr = int(arr_entry.get()) if arr_entry.get() else None
        ccr = int(ccr_entry.get()) if ccr_entry.get() else None
        adc_value = int(adc_value_entry.get()) if adc_value_entry.get() else None
        v_ref = float(v_ref_entry.get()) if v_ref_entry.get() else None
        resolution = int(resolution_entry.get()) if resolution_entry.get() else None

        # timer frequency calculation
        if clock_freq is not None and prescaler is not None and arr is not None:
            timer_freq = clock_freq / ((prescaler + 1) * (arr + 1))
            result_text += f"Timer Frequency: {timer_freq:.2f} Hz\n"
            if ccr is not None:
                pwm_period = 1 / timer_freq
                pwm_duty_cycle = (ccr / (arr + 1)) * 100
                result_text += f"PWM Period: {pwm_period:.6f} seconds\n"
                result_text += f"PWM Duty Cycle: %{pwm_duty_cycle:.2f}\n"
        
        # adc voltage calculation
        if adc_value is not None and v_ref is not None and resolution is not None:
            max_digital_value = (2 ** resolution) - 1
            adc_voltage = (adc_value * v_ref) / max_digital_value
            result_text += f"ADC Voltage: {adc_voltage:.3f} V\n"
        
        # if no calculation is done
        if not result_text:
            result_text = "Please fill in the required fields to perform a calculation."
        
        # display results in the GUI
        result_label.config(text=result_text)
    except ValueError:
        messagebox.showerror("Error", "Please enter valid values!")

# window
root = tk.Tk()
root.title("STM32 Timer and ADC Calculation Tool")

# input fields and labels
tk.Label(root, text="System Clock Frequency (Hz):").grid(row=0, column=0, sticky="e")
clock_freq_entry = tk.Entry(root)
clock_freq_entry.grid(row=0, column=1)

tk.Label(root, text="Prescaler Value:").grid(row=1, column=0, sticky="e")
prescaler_entry = tk.Entry(root)
prescaler_entry.grid(row=1, column=1)

tk.Label(root, text="ARR Value:").grid(row=2, column=0, sticky="e")
arr_entry = tk.Entry(root)
arr_entry.grid(row=2, column=1)

tk.Label(root, text="CCR Value:").grid(row=3, column=0, sticky="e")
ccr_entry = tk.Entry(root)
ccr_entry.grid(row=3, column=1)

tk.Label(root, text="ADC Digital Value:").grid(row=4, column=0, sticky="e")
adc_value_entry = tk.Entry(root)
adc_value_entry.grid(row=4, column=1)

tk.Label(root, text="Reference Voltage (V):").grid(row=5, column=0, sticky="e")
v_ref_entry = tk.Entry(root)
v_ref_entry.grid(row=5, column=1)

tk.Label(root, text="ADC Resolution:").grid(row=6, column=0, sticky="e")
resolution_entry = tk.Entry(root)
resolution_entry.grid(row=6, column=1)

# calculate button
calculate_button = tk.Button(root, text="Calculate", command=calculate)
calculate_button.grid(row=7, column=0, columnspan=2, pady=10)

# result label
result_label = tk.Label(root, text="", justify="left")
result_label.grid(row=8, column=0, columnspan=2)

# run the window
root.mainloop()
