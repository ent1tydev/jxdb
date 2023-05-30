# JsonDB

JsonDB provides secure data storage using AES encryption. All data stored in the database is automatically encrypted before being saved and decrypted when read. This ensures that data is protected from unauthorized access.

## Installation

You can install JsonDB using pip:

pip install jsondb

## Usage

from jxdb import JsonDB

# Create a new instance of JsonDB
db = JsonDB()

# Open an existing JSON database file
db.open('data.json', 'File_Security_Password')

# Get the value for a specific key
value = db.get('key')

# Set a new key-value pair
db.set('new_key', 'new_value')

# Delete a key-value pair
db.delete('key_to_delete')

# Find all values that contain a specific data
result = db.concept('data')

# Get a list of all keys
keys = db.keys()

# Get a list of all values
values = db.values()

# Get a list of all key-value pairs
items = db.items()

# Clear the entire database
db.clear()

# Get the count of key-value pairs
count = db.count()

# Delete all fields that contain a specific data
db.delete_by_value('data')

# Delete all fields that contain a specific key
db.delete_by_key('key')

# Save the changes to the JSON database file
db.save('data.json', 'Your_Password')
