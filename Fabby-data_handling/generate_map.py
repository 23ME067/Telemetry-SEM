import folium
import csv
import math  # Import the math module

def read_data(filename):
  """
  Reads latitude and longitude data from a CSV file.

  Args:
      filename: The path to the CSV file.

  Returns:
      A list of tuples containing latitude and longitude coordinates.
  """
  data = []
  with open(filename, 'r') as csvfile:
    reader = csv.reader(csvfile)
    next(reader) # Skip header row
    for row in reader:
      lon, lat = float(row[0]), float(row[1])
      data.append((lat, lon))  # Latitude first for folium
  return data

def calculate_distance(data):
  """
  Calculates the total distance between data points using the Haversine formula.

  Args:
      data: A list of tuples containing latitude and longitude coordinates.

  Returns:
      The total distance in kilometers.
  """
  total_distance = 0
  earth_radius = 6371  # Earth radius in kilometers

  for i in range(1, len(data)):
    lat1, lon1 = data[i-1]
    lat2, lon2 = data[i]

    # Convert degrees to radians
    lat1_rad = lat1 * math.pi / 180
    lon1_rad = lon1 * math.pi / 180
    lat2_rad = lat2 * math.pi / 180
    lon2_rad = lon2 * math.pi / 180

    dlon = lon2_rad - lon1_rad
    dlat = lat2_rad - lat1_rad

    a = math.sin(dlat / 2) * math.sin(dlat / 2) + math.cos(lat1_rad) * math.cos(lat2_rad) * math.sin(dlon / 2) * math.sin(dlon / 2)
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

    distance = earth_radius * c  # Distance in kilometers

    total_distance += distance

  return total_distance

def create_map(data, center_coords, zoom_start):
  """
  Creates a folium map with a polyline and displays the total distance.

  Args:
      data: A list of tuples containing latitude and longitude coordinates.
      center_coords: A tuple containing the center coordinates for the map.
      zoom_start: The initial zoom level for the map.
  """
  m = folium.Map(location=center_coords, zoom_start=zoom_start)
  folium.PolyLine(locations=data, color='blue', weight=2).add_to(m)
  
  # Calculate and display total distance
  total_distance = calculate_distance(data)
  folium.Marker(location=center_coords, popup=f"Total Distance: {total_distance:.2f} km").add_to(m)

  return m

if __name__ == '__main__':
  filename = 'ramu.csv'  # Replace with your CSV file name
  center_coords = [9.8109, 76.456]  # Example center coordinates (San Francisco)
  zoom_start = 12  # Initial zoom level

  data = read_data(filename)
  map = create_map(data, center_coords, zoom_start)

  # Save map as HTML file (optional)
  map.save('trip_map.html')

  print("Map created! Check trip_map.html (if saved) or open the map object in your browser.")