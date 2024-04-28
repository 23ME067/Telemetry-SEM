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


def extract_nmea_data(nmea_data):
  """
  Extracts desired data from RMC NMEA strings.

  Args:
      nmea_data: A string containing NMEA data.

  Returns:
      A list of dictionaries containing combined data for each valid entry.
  """
  combined_data = []

  for line in nmea_data.splitlines():
    if line.startswith("$GPRMC"):
      fields = line.split(",")

      # Extract timestamp (assuming valid format)
      timestamp_utc = fields[1]
      try:
        datetime_utc = datetime.datetime.strptime(timestamp_utc, "%H%M%S.%f")
        timestamp_formatted = datetime_utc.strftime("%Y/%m/%d %H:%M:%S+00")
      except ValueError:
        print(f"Error: Invalid timestamp format in line: {line}")
        timestamp_formatted = None

      # Extract other data (assuming valid format)
      latitude = float(fields[3]) / 100  # Remove leading zero from latitude
      longitude = float(fields[5]) / 100  # Remove leading zero from longitude
      speed_knots = float(fields[7])  # Ground speed in knots

      # Convert speed from knots to km/h, round to 3 decimal places
      speed_kmh = speed_knots * 1.852
      speed_kmh_rounded = round(speed_kmh, 3)

      # Append data to dictionary (only if timestamp is valid)
      if timestamp_formatted:
        data = {
          "lon": longitude,
          "lat": latitude,
          "Speed (knots)": speed_knots,
          "speed": speed_kmh_rounded,
          "timestamp": timestamp_formatted
        }
        combined_data.append(data)

  return combined_data


# Specify the path to your NMEA data file
nmea_filepath = "test.txt"  # Replace with your actual path

# Read NMEA data from the file
nmea_data = read_nmea_data(nmea_filepath)

# Extract data from RMC strings
extracted_data = extract_nmea_data(nmea_data)

# Save extracted data to CSV file (if any data was extracted)
if extracted_data:
  with open("time_coordinate_speed.csv", 'w', newline='') as csvfile:
    fieldnames = ["lon", "lat", "Speed (knots)", "speed", "timestamp"]
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for row in extracted_data:
      writer.writerow(row)
  print("NMEA data parsed and saved to time_coordinate_speed.csv")
else:
  print("No valid data found in NMEA file.")
