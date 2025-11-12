import requests
from bs4 import BeautifulSoup

def get_raw_data(doc_url_1):
  try:
    response = requests.get(doc_url_1)
    response.raise_for_status()
    return response.text
  except requests.RequestException as e:
    print(f"Error fetching data: {e}")
    return None

# Function to get information from the Google Doc table
# and change it into readable info for the program to
# display in a grid
def parse_data_to_grid_map(html_data):
  if not html_data:
    return None, 0, 0

  soup = BeautifulSoup(html_data, 'html.parser')

  data_table = soup.find('table')

  if not data_table:
    print("Error: Could not find a data table in the Google Doc.")
    return None, 0, 0

  grid_map = {}
  max_x, max_y = 0, 0

  rows = data_table.find_all('tr')[1:]

  for row_num, tr in enumerate(rows):
    cells = tr.find_all('td')
    if len(cells) < 3:
      continue
    try:
      x = int(cells[0].get_text().strip())
      char = cells[1].get_text().strip()
      char = char.replace('\xa0', '').replace('\n', '') # makes sure char is stripped fully
      if not char:
        char = ' '
      y = int(cells[2].get_text().strip())

      if x > max_x: max_x = x
      if y > max_y: max_y = y

      if x not in grid_map:
        grid_map[x] = {}
      grid_map[x][y] = char

    except (ValueError, IndexError):
      print("Error")
      continue

  return grid_map, max_x + 1, max_y + 1

# Function to decode the message in the Google Doc 
def decode_secret_message(doc_url):
  html_data = get_raw_data(doc_url)
  grid_map, grid_width, grid_height = parse_data_to_grid_map(html_data)

  dictionary = {}
  if not grid_map:
    return dictionary

  for y in range(grid_height -1, -1, -1): # grid altered to align letter correctly
    line = []
    for x in range(grid_width):
      if x in grid_map and y in grid_map[x]:
        char = grid_map[x][y]
        line.append(char)
      else:
        line.append(' ')
    print("".join(line))

# Sample Doc used as the argument
decode_secret_message("https://docs.google.com/document/d/e/2PACX-1vQiVT_Jj04V35C-YRzvoqyEYYzdXHcRyMUZCVQRYCu6gQJX7hbNhJ5eFCMuoX47cAsDW2ZBYppUQITr/pub")

