import datetime
import csv

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

def extract_gga_data(nmea_data):
  """
  Extracts timestamps and altitudes from GGA NMEA strings.

  Args:
      nmea_data: A string containing NMEA data.

  Returns:
      A list of dictionaries containing extracted data:
          - timestamp: Formatted timestamp (YYYY/MM/DD HH:MM:SS+ZZ)
          - altitude: Altitude value (meters)
  """
  data = []
  lines = nmea_data.splitlines()
  for line in lines:
    if line.startswith("$GPGGA"):
      fields = line.split(",")
      # Extract timestamp and convert to desired format (YYYY/MM/DD HH:MM:SS+ZZ)
      timestamp_utc = datetime.datetime.strptime(fields[1], "%H%M%S.%f")  # UTC time
      offset_str = str(timestamp_utc.utcoffset()).replace(":", "")  # Extract offset string

      # Format timestamp with +00 if offset is missing
      timestamp_formatted = timestamp_utc.strftime("%Y/%m/%d %H:%M:%S") + "+00"

      altitude = float(fields[9])  # Altitude in meters
      data.append({"time": timestamp_formatted, "alt": altitude})
  return data

def save_to_csv(data, filename):
  """
  Saves extracted data to a CSV file.

  Args:
      data: A list of dictionaries containing extracted data.
      filename: Path to the output CSV file.
  """
  with open(filename, 'w', newline='') as csvfile:
    fieldnames = ["time", "alt"]
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for row in data:
      writer.writerow(row)

# Specify the path to your NMEA data file
nmea_filepath = "test.txt"  # Replace with your actual path

# Read NMEA data from the file
nmea_data = read_nmea_data(nmea_filepath)

# Extract timestamps and altitudes from GGA strings
extracted_data = extract_gga_data(nmea_data)

# Save extracted data to CSV file
save_to_csv(extracted_data, "gga_data.csv")

print("GGA data extracted and saved to gga_data.csv")
