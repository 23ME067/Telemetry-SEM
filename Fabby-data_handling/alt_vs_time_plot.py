import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import pandas as pd

# Load the data from the file
data = pd.read_csv('gga_data.csv', parse_dates=['time'])

# Convert the time column to a datetime format
data['time'] = pd.to_datetime(data['time'])

# Create the plot
fig, ax = plt.subplots()
ax.plot(data['time'], data['alt'])

# Format the x-axis to display dates
ax.xaxis.set_major_locator(mdates.SecondLocator())
ax.xaxis.set_major_formatter(mdates.DateFormatter('%H:%M:%S'))

# Set the title and labels
ax.set_title('Altitude vs Time')
ax.set_xlabel('Time')
ax.set_ylabel('Altitude (m)')

# Show the plot
plt.show()