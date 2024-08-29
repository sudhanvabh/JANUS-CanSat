import csv
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Checking if live_data_sim.csv file exists, and creating one if it doesn't exist
try:
    with open('live_data_sim.csv', 'r'):
        pass
except FileNotFoundError:
    with open('live_data_sim.csv', 'w'):
        pass

# Overwriting the previous simulation and adding suitable headers
with open('live_data_sim.csv', 'w', newline='') as data_file:
    header = ['Temperature', 'GPS_ALTITUDE']
    writer = csv.writer(data_file)
    writer.writerow(header)

sns.set_style('darkgrid')

# Variable to keep track of the maximum time value
max_time = 20  # Start with a max_time of 20 to show the first 20 seconds initially

def animate_plot(i):
    global max_time
    time = 0
    time_x = []
    temp_y1 = []
    alt_y2 = []

    with open('live_data_sim.csv', 'r') as data_file: # Opening incoming data file
        data_reader = csv.DictReader(data_file)

        for row in data_reader:
            time += 1
            time_x.append(time)
            temp_y1.append(float(row['Temperature'])) # Appending Temperature Values
            alt_y2.append(float(row['GPS_ALTITUDE'])) # Appending Altitude values

    plt.clf()

    # Creating Sub-Plots for the two graphs
    temp_graph = plt.subplot(1, 2, 1)
    alt_graph = plt.subplot(1, 2, 2)

    # Parameters for Temp Graph
    temp_graph.plot(time_x, temp_y1, marker='o', linewidth=2, label='Temperature', color='#FF6F61')
    temp_graph.set_title('Temperature live-feed', fontsize=14, fontweight='bold')
    temp_graph.set_xlabel('Time (secs)', fontsize=12)
    temp_graph.set_ylabel('Temperature (°C)', fontsize=12)
    temp_graph.legend(loc='upper left')
    temp_graph.set_ylim(20, 35)
    temp_graph.grid(True, which='both', linestyle='--', linewidth=0.5)

    # Parameters for Alt Graph
    alt_graph.plot(time_x, alt_y2, marker='o', linewidth=2, label='Altitude', color='#6B5B95')
    alt_graph.set_title('GPS Altitude live-feed', fontsize=14, fontweight='bold')
    alt_graph.set_xlabel('Time (secs)', fontsize=12)
    alt_graph.set_ylabel('Altitude (m)', fontsize=12)
    alt_graph.legend(loc='upper left')
    alt_graph.set_ylim(818, 823)
    alt_graph.grid(True, which='both', linestyle='--', linewidth=0.5)

    # Adjusting the x-axis to always show the last 20 seconds
    max_time = max(max_time, time_x[-1] if time_x else 20)
    start_time = max(0, max_time - 20)
    temp_graph.set_xlim(start_time, max_time)
    alt_graph.set_xlim(start_time, max_time)

    temp_graph.patch.set_alpha(0.8)
    alt_graph.patch.set_alpha(0.8)

    plt.tight_layout()

# Set the plot size
fig = plt.figure()
fig.set_size_inches(15, 7)

# Updating the graph, animating
animate = FuncAnimation(plt.gcf(), animate_plot, frames=100, interval=1000)

# Opening the UI/UX window
plt.show()
