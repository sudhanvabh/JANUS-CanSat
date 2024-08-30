import tkinter as tk
import subprocess

def run_simulation():
    subprocess.run(["python", "run_simulation.py"])
    root.destroy()

def run_simulation_4x():
    subprocess.run(["python", "run simulation (4x).py"])
    root.destroy()

root = tk.Tk()
root.title( "Simulation Runner")

button1 = tk.Button(root,text="Run simulation", command=run_simulation, padx=20,pady=10)
button2 = tk.Button(root,text="Run simulation (4x speed)",command=run_simulation_4x, padx=20,pady=10)

button1.pack( pady=10)
button2.pack( pady=10)
root.mainloop()
