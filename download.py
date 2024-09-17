import csv
import requests
import os

# Define the folder where images will be saved
folder_name = 'downloaded_images'

# Create the directory if it doesn't exist
if not os.path.exists(folder_name):
    os.makedirs(folder_name)

# Open the CSV file
with open('dataset/sample_test.csv', 'r') as file:
    # Create a CSV reader object
    reader = csv.DictReader(file)
    
    # Iterate over each row in the CSV file
    for row in reader:
        # Get the image URL and file name from the row
        image_url = row['image_link']
        file_name = image_url.split('/')[-1]
        
        # Create the full path for saving the image
        file_path = os.path.join(folder_name, file_name)
        
        # Send a GET request to the image URL
        response = requests.get(image_url)
        
        # Check if the request was successful
        if response.status_code == 200:
            # Save the image to the specified folder
            with open(file_path, 'wb') as image_file:
                image_file.write(response.content)
            print(f"Downloaded {file_name} to {folder_name}")
        else:
            print(f"Failed to download {file_name}. Status code: {response.status_code}")
