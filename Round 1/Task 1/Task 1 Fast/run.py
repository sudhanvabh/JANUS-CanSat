# This program simulates data as if its incoming live from a sensor every second
# and creates a csv file for the same

import csv
import time
import subprocess

def is_number(value): # For error management
    try:
        float(value)
        return True
    except ValueError:
        return False

# input("Press ENTER to start live-feed simulation")

# Opening Grapher file
subprocess.run(['start', 'cmd', '/k', 'python', 'TempAltTracker.py'], shell=True)

print('Receiving live-feed')
for i in range(1,5):
    time.sleep(1)
    print(i)

# Opening the source file to read the simulation data
with open('Simulation_Data_CanSat_24.csv', 'r') as source_file:
    source_reader = csv.reader(source_file)

    next(source_reader)

    with open('live_data_sim.csv', 'a', newline='') as data_file:
        data_writer = csv.writer(data_file)
        for row in source_reader:
            if all(is_number(entry) for entry in row): # Ignoring values with errors
                data_writer.writerow(row)
                print(row)
            else:
                print(f"Skipped invalid row: {row}") # Removed values if they have an error
            data_file.flush() # saving file so that the program can read
            time.sleep(0.25)