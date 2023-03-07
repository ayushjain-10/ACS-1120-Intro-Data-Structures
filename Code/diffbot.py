import requests

# Your Diffbot API key
API_KEY = "08e6488ea4ed2f3067da75b9180d1f0f"

# The URL of the Diffbot Article API endpoint
ARTICLE_API_URL = "https://api.diffbot.com/v3/article"

# The name of the input file
INPUT_FILE = "pages.txt"

# The name of the output file
OUTPUT_FILE = "output.txt"

# Open the input file and read the URLs
with open(INPUT_FILE, "r") as input_file:
    urls = input_file.readlines()

# Open the output file for writing
with open(OUTPUT_FILE, "w") as output_file:

    # Loop through the URLs
    for url in urls:
        # Strip any whitespace from the URL
        url = url.strip()

        # Build the API request
        payload = {
            "token": API_KEY,
            "url": url
        }

        # Send the API request
        response = requests.get(ARTICLE_API_URL, params=payload)

        # If the response was successful (status code 200)
        if response.status_code == 200:
            # Extract the article text from the response
            data = response.json()
            text = data["objects"][0]["text"]

            # Write the text to the output file
            output_file.write(text)

        # If the response was not successful
        else:
            # Print an error message
            print("Error:", response.status_code, response.text)
