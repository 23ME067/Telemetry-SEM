# Function to read NMEA data from a text file
def read_nmea_data(filepath):
  """
  Reads NMEA data from a text file and returns it as a string.

  Args:
      filepath: Path to the text file containing NMEA data.

  Returns:
      A string containing the NMEA data from the file.
  """
  try:
    with open(filepath, 'r') as file:
      data = file.read()
      return data
  except FileNotFoundError:
    print(f"Error: File not found at {filepath}")
    return ""

# Specify the path to your NMEA data file
nmea_filepath = "test.txt"  # Replace with your actual path

# Read NMEA data from the file
nmea_data = read_nmea_data(nmea_filepath)

# Define empty lists to store extracted data
timestamps = []
latitudes = []
longitudes = []
speeds = []

# Split NMEA data into lines
lines = nmea_data.splitlines()

# Loop through each line
for line in lines:
  # Check if line starts with $GPRMC (RMC sentence)
  if line.startswith("$GPRMC"):
    # Split the sentence into fields
    fields = line.split(",")
    
    # Extract desired data (assuming valid format)
    timestamp = fields[1]
    latitude = fields[3]  # Remove leading zero from latitude (already done)

    # Shift decimal point in latitude two places to the left (multiply by 100)
    latitude = float(latitude) / 100

    longitude = fields[5]  # Remove leading zero from longitude (already done)

    # Shift decimal point in longitude two places to the left (multiply by 100)
    longitude = float(longitude) / 100

    speed = float(fields[7])  # Convert speed to float

    # Convert speed from knots to km/h by multiplying by 1.852
    speed_kmh = speed * 1.852

    # Round speed to 3 decimal places using round("{:.3f}".format(speed_kmh))
    speed_kmh_rounded = round(float("{:.3f}".format(speed_kmh)), 3)  # Convert to float for rounding

    # Append data to lists
    timestamps.append(timestamp)
    latitudes.append(latitude)
    longitudes.append(longitude)
    speeds.append(speed_kmh_rounded)

# Create a dictionary from extracted data
data = {
  "Timestamp": timestamps,
  "lat": latitudes,
  "lon": longitudes,
  "Speed (km/h)": speeds  # Update key name for clarity
}

# Import pandas library
import pandas as pd

# Create a Pandas DataFrame from the dictionary
df = pd.DataFrame(data)

# Save DataFrame to CSV file
df.to_csv("time_coordinate_speed.csv", index=False)

print("NMEA data parsed and saved to time_coordinate_speed.csv")
