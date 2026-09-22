# Unit 6 Discussion: Dictionaries as Hash Tables

## Overview

This assignment uses Python dictionaries to demonstrate hash table behavior.

This program demonstrates how a Python dictionary can be used as a hash table to store and retrieve data
using key-value pairs. Each patient ID is used as a unique key, while the patient's name is stored as 
the value associated with that key.

The program demonstrates insert, lookup, update, and delete operations. It also tests edge cases 
involving keys that do not exist in the dictionary.

### How the Structure Works

A Python dictionary uses a hash table to organize key-value pairs. When a key is added to the dictionary,
Python uses the key's hash to help determine where its associated value is stored. This allows a value to
be retrieved directly by its key instead of searching through every element one at a time.

The program begins with an empty dictionary and adds five patient records. The patient IDs 100 through 104
are used as keys, and the patient names are stored as their corresponding values.

## Learning Objectives

- Insert key-value pairs
- Retrieve values efficiently
- Update existing values
- Remove entries
- Understand hashing concepts

## Requirements

1. Create and populate a dictionary.
2. Demonstrate lookup operations.
3. Demonstrate update operations.
4. Demonstrate delete operations.
5. Test edge cases.
6. Create a real-world scenario.

## Program Output

The **insert** operation adds five patient records to the dictionary. The lookup operations use patient IDs 101 and 104 
to retrieve the corresponding patient names.

The **update** operation changes the value associated with patient ID 100 from "Duke" to "Duke Wilkens". Because the key
already exists, assigning a new value replaces the previous value instead of creating a duplicate key.

The **delete** operation removes patient ID 102 and its associated value from the dictionary. The program also tests 
two edge cases using the missing patient ID 105. The "get()" methods safely handles a lookup for the missing key, 
while the "pop()" method, with a default value, safely handles an attempt to delete the missing key. Both operations
avoid causing a KeyError.

## Real-World Use Case

A veterinary hospital could use a dictionary to associate unique patient IDs with patient information. For example, a 
patient's ID could serve as the key while the patient's information is stored as the associated value. Using these 
unique IDs allows the program to locate a particular patient's information without having to search through every 
patient record individually.

This type of structure is useful when information needs to be inserted, retrieved, updated, or removed using a unique 
identifier.

