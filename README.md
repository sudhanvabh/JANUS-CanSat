# Live Data Simulation and Visualization for CanSat

## Task 1

This project simulates incoming live data from a sensor and visualizes it in real-time using Python. It is designed to mimic the data acquisition process of a CanSat, focusing on temperature and altitude monitoring.

### Project Overview

The project consists of two primary components:
1. **Data Simulation**: Simulates live sensor data and writes it to a CSV file.
2. **Data Visualization**: Reads the simulated data from the CSV file and dynamically updates plots to visualize temperature and altitude in real-time.

### File Descriptions

### `run.py`
This script simulates the incoming data from a sensor and writes it to a CSV file (`live_data_sim.csv`). It performs the following functions:

- Simulates the receipt of live data every second.
- Opens a separate Python script (`TempAltTracker.py`) to visualize the data in real-time.
- Reads data from an existing CSV file (`Simulation_Data_CanSat_24.csv`) and filters out invalid data.
- Continuously appends valid data to the `live_data_sim.csv` file, which is used by the visualization script.

### `TempAltTracker.py`
This script is responsible for visualizing the simulated data:

- Checks for the existence of `live_data_sim.csv` and creates it if not found.
- Initializes the CSV file with headers: `Temperature` and `GPS_ALTITUDE`.
- Uses Matplotlib and Seaborn to create two subplots for temperature and altitude.
- Animates the plots to update every second, displaying the most recent 20 seconds of data.
- Provides a user interface to visualize the live data in real-time.

## Task 2
This project is a temperature monitoring system implemented using an Arduino. The system reads temperature data from a sensor, compares it to predefined safe, maximum, and critical temperature thresholds, and triggers indicators (LEDs and buzzer) based on the temperature readings.

## Circuit Components
- **Arduino Uno**
- **Temperature Sensor** (connected to analog pin A0)
- **Green LED** (connected to digital pin 13) - Indicates safe temperature range
- **Red LED** (connected to digital pin 12) - Indicates temperature out of safe range
- **Buzzer** (connected to digital pin 4) - Activates when temperature reaches a critical level

## C++ Code Explanation

### Variables
- `min_safe_temp`: Minimum safe temperature threshold (20°C).
- `max_safe_temp`: Maximum safe temperature threshold (40°C).
- `critical_temp`: Critical temperature threshold (55°C).
- `current_temp`: Variable to store the current temperature reading.

The `loop()` function continuously reads the temperature data, converts the analog reading to a temperature value, and then:
1. Turns on the green LED if the temperature is within the safe range.
2. Turns on the red LED if the temperature is outside the safe range.
3. Activates the buzzer if the temperature reaches or exceeds the critical level.


