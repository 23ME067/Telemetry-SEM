import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import pandas as pd

# Load the data from the file
data = pd.read_csv('speed_vs_time.csv', parse_dates=['timestamp'])

# Create the plot
fig, ax = plt.subplots()
ax.plot(data['timestamp'], data['speed'])

# Format the x-axis to display dates
ax.xaxis.set_major_locator(mdates.SecondLocator())
ax.xaxis.set_major_formatter(mdates.DateFormatter('%H:%M:%S'))

# Set the title and labels
ax.set_title('Speed vs Time')
ax.set_xlabel('Time')
ax.set_ylabel('Speed (km/h)')

# Show the plot
plt.show()