# JXDB - JSON Database Library

You can find JXDB, a powerful JSON database library, on PyPI (Python Package Index) at [pypi.org/jxdb](https://pypi.org/jxdb). JXDB allows you to easily store and manipulate JSON data in your Python projects.

## Features

- Simple and intuitive interface for working with JSON data.
- Supports data encryption using AES for secure storage.
- Provides efficient methods for data retrieval, modification, and deletion.
- Supports searching and filtering based on key-value pairs.
- Lightweight and easy to integrate into your projects.

## License

JXDB is released under the OpenSociety license. You can find the license details at [ccic.eu.org/opensociety.html](https://ccic.eu.org/opensociety.html). The OpenSociety license grants you the freedom to use, modify, and distribute JXDB according to the terms specified in the license.

## Installation

You can install JsonDB using pip:

pip install jxdb

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
