# Phone Number Tracking Using Python:

### In Baby Steps:

```markdown
# Phone Number Geolocation Project

This project uses Python to parse phone numbers and retrieve their geolocation information.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

The project requires the following Python libraries:

- [phonenumbers](^17^): A library for parsing, formatting, storing, and validating international phone numbers.
- [opencage](^1^): A library for geocoding using the OpenCage API.
- [folium](^8^): A library for creating interactive maps.

You can install these libraries using pip:

```bash
pip install phonenumbers opencage folium
```

### Installing

Clone the repository to your local machine:

```bash
git clone https://github.com/Engr-Jalal-Saleem/Phone-Number-Tracking-Using-Python
```

### Usage

The main script is `main.py`. You can run it with Python:

```bash
python main.py
```

## OpenCage API Key

The script requires an API key from OpenCage. You can sign up for a free API key on the [OpenCage website](^1^). Once you have the API key, replace `"Paste your API key here"` in the script with your actual API key.

## How It Works

The script parses a phone number, retrieves the location description for the parsed phone number, and then uses the OpenCage API to geocode the location description. The geocoding results are used to create an interactive map with a marker at the specified latitude and longitude. The map is saved as an HTML file.

## Contributing

Please read CONTRIBUTING.md for details on our code of conduct, and the process for submitting pull requests to us.

## License

This project is licensed under the MIT License - see the LICENSE.md file for details

```
 Also, remember to replace `"Paste your API key here"` in your script with your actual OpenCage API key. You can get the API key by signing up on the [OpenCage website](^1^)¹³.
```
