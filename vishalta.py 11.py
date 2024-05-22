import requests

class CountryData:
    def _init_(self, url):
        self.url = url

    def fetch_data(self):
        response = requests.get(self.url)
        if response.status_code == 200:
            return response.json()
        else:
            print("Failed to fetch data.")
            return None

    def display_country_info(self, data):
        print("Country Information:")
        for country in data:
            print(f"Country: {country['name']['common']}")
            print(f"Currency: {', '.join(country['currencies'].keys())}")
            print(f"Currency Symbol: {', '.join(country['currencies'].values())}")
            print("")

    def countries_with_dollar_currency(self, data):
        print("Countries with Dollar Currency:")
        for country in data:
            if 'USD' in country['currencies']:
                print(country['name']['common'])

    def countries_with_euro_currency(self, data):
        print("Countries with Euro Currency:")
        for country in data:
            if 'EUR' in country['currencies']:
                print(country['name']['common'])

# Usage example:
url = "https://restcountries.com/v3.1/all"
country_data = CountryData(url)
data = country_data.fetch_data()
if data:
    country_data.display_country_info(data)
    country_data.countries_with_dollar_currency(data)
    country_data.countries_with_euro_currency(data)

    import requests

# API endpoint URL with state filter parameter
base_url = "https://api.openbrewerydb.org/v1/breweries?by_state="

# States to search (replace with your desired states)
states = ["Alaska", "Maine", "New York"]

# Function to fetch breweries by state
def get_breweries_by_state(state):
  url = base_url + state
  response = requests.get(url)
  if response.status_code == 200:
    return response.json()
  else:
    print(f"Error fetching breweries for {state}: {response.status_code}")
    return []

# Function to count breweries with websites
def count_breweries_with_website(breweries):
  website_count = 0
  for brewery in breweries:
    if "website" in brewery and brewery["website"] != "":
      website_count += 1
  return website_count

# Main program logic
for state in states:
  # Fetch breweries for the current state
  breweries = get_breweries_by_state(state)

  # List brewery names
  print(f"\nBreweries in {state}:")
  for brewery in breweries:
    print(brewery["name"])

  # Count breweries
  brewery_count = len(breweries)
  print(f"\nTotal breweries in {state}: {brewery_count}")

  # City and brewery type counts (requires additional logic)
  # This section needs further development to handle city and brewery type counts.
  # You'll likely need to group breweries by city and type and then count them.

  # Count breweries with website
  website_count = count_breweries_with_website(breweries)
  print(f"\nBreweries with website in {state}: {website_count}")

  print("\n------------------------\n")
