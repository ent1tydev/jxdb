# JXDB - JSON Database Library

You can find JXDB, a powerful JSON database library, on PyPI (Python Package Index) at [pypi.org/project/jxdb](https://pypi.org/project/jxdb). JXDB allows you to easily store and manipulate JSON data in your Python projects.

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

# JsonDB

JsonDB is a simple JSON-based database that provides methods for managing key-value data and performing operations like encryption and decryption.

## Methods

### `open(filename, password)`

Opens the database from a file with the specified filename and password. It decrypts the data and loads it into memory.

### `save(filename, password)`

Saves the database to a file with the specified filename and password. It encrypts the data and writes it to the file.

### `get(key)`

Retrieves the value associated with the specified key from the database.

### `set(key, value)`

Sets the value for the specified key in the database.

### `delete(key)`

Deletes the value associated with the specified key from the database.

### `concept(data)`

Searches for values that contain the specified data in their keys and returns a list of matching values.

### `keyconcept(data)`

Searches for keys that contain the specified data and returns a list of matching keys.

### `keys()`

Returns a list of all keys in the database.

### `values()`

Returns a list of all values in the database.

### `items()`

Returns a list of all items (key-value pairs) in the database.

### `clear()`

Clears the entire database, removing all key-value pairs.

### `count()`

Returns the number of items in the database.

### `delete_by_value(data)`

Deletes values that contain the specified data from the database.

### `delete_by_key(key)`

Deletes values associated with keys that contain the specified key from the database.

## Usage

```python
# Example usage of JsonDB

# Create an instance of JsonDB
db = JsonDB()

# Open the database from a file
db.open("data.json", "password")

# Perform operations on the database
value = db.get("key")
db.set("new_key", "new_value")
db.delete("key")
concept_results = db.concept("data")
keyconcept_results = db.keyconcept("key")
keys = db.keys()
values = db.values()
items = db.items()
db.clear()
count = db.count()
db.delete_by_value("data")
db.delete_by_key("key")

# Save the database to a file
db.save("new_data.json", "password")
