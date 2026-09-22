"""
====================================================
UNIT 6 DISCUSSION: Python Dictionaries as Hash Tables
====================================================

INSTRUCTIONS:
In this activity, you will work with Python dictionaries
to simulate the behavior of a hash table.

You will modify the provided starter code to demonstrate
common operations and explain key concepts.

Follow all TODO prompts in the code and ensure your output
clearly communicates what your program is doing at each step.

----------------------------------------------------
"""


def main():
    print("=== UNIT 6: DICTIONARIES AS HASH TABLES ===")

    # ===============================
    # TODO (Student): CREATE A HASH TABLE
    # ===============================
    #
    # Requirements:
    # 1. Create an empty dictionary.
    # 2. Add at least 5 key-value pairs.
    # 3. Add comments explaining how a dictionary
    #    behaves like a hash table.
    # 4. Display the contents of the dictionary.


    print("\n=== INSERT OPERATIONS ===")
    print("TODO: Create a dictionary and add multiple key-value pairs.")

    # Creates an empty dictionary to store patient IDs as keys and patient
    # names as values.
    patient_records = {}

    # Adds five patient records to the dictionary.
    patient_records[100] = "Duke"
    patient_records[101] = "Cody"
    patient_records[102] = "Max"
    patient_records[103] = "Sunny"
    patient_records[104] = "Dakota"

    # A Python dictionary behaves like a hash table by using each key to
    # determine where its associated value is stored. This allows values to
    # usually be inserted and retrieved efficiently by key.
    print("\nPatient Records:", patient_records)

    # ===============================
    # TODO (Student): LOOKUP OPERATIONS
    # ===============================
    #
    # Requirements:
    # 1. Retrieve at least two existing keys.
    # 2. Clearly display the lookup results.
    # 3. Add meaningful comments to explain how the lookup works.

    print("\n=== LOOKUP OPERATIONS ===")
    print("TODO: Demonstrate successful key lookups.\n")

    # Uses the unique patient ID as the key to directly retrieve the value
    # associated with that patient.
    print("Patient 101:", patient_records[101])
    print("Patient 104:", patient_records[104])



    # ===============================
    # TODO (Student): UPDATE OPERATIONS
    # ===============================
    #
    # Requirements:
    # 1. Update the value associated with an existing key.
    # 2. Display the dictionary before and after the update.
    # 3. Use comments to explain what happens when an existing key is assigned
    #    a new value.

    print("\n=== UPDATE OPERATIONS ===")
    print("TODO: Demonstrate updating an existing key.")

    # Displays the dictionary before changing the value.
    print("\nBefore update:", patient_records)

    # Assigns a new value to an existing key, replacing its previous
    # value instead of creating another copy of the key.
    patient_records[100] = "Duke Wilkens"

    # Displays the dictionary after the patient's information is updated.
    print("After update:", patient_records)

    # ===============================
    # TODO (Student): DELETE OPERATIONS
    # ===============================
    #
    # Requirements:
    # 1. Delete at least one key-value pair.
    # 2. Display the dictionary before and after deletion.
    # 3. Use comments to explain what happens when a key is removed.

    print("\n=== DELETE OPERATIONS ===")
    print("TODO: Demonstrate deleting a key-value pair.")

    # Displays all patient records before deletion.
    print("\nBefore deletion:", patient_records)

    # Removes patient ID 102 and its associated value from the dictionary.
    # After deletion, the key can no longer be used to retrieve that patient.
    del patient_records[102]

    # Displays the remaining records after deletion.
    print("After deletion:", patient_records)

    # ===============================
    # TODO (Student): EDGE CASES
    # ===============================
    #
    # Demonstrate at least two edge cases.
    #
    # Example ideas:
    # - Lookup a missing key
    # - Delete a missing key safely
    # - Update a missing key
    # - Use an empty dictionary
    #
    # Explain what happens in each case.

    print("\n=== EDGE CASES ===")
    print("TODO: Demonstrate and explain edge cases.")

    # Edge Case 1: Lookup a missing or absent key.
    # The get() method searches for the key without causing a KeyError.
    # If patient 105 does not exist, "Patient not found" is returned.
    missing_patient = patient_records.get(105, "Patient not found")
    print("\nFind patient 105:", missing_patient)

    # Edge Case 2: Safely delete a missing key.
    # The pop() method can be given a default value so attempting to remove
    # a nonexistent key does not result in an error.
    deleted_patient = patient_records.pop(105, "Patient not found")
    print("Delete patient 105:", deleted_patient)

    # Displays the dictionary to show that attempting to delete the missing
    # key did not affect the existing records.
    print("Patient records after edge cases:", patient_records)


    print("\n=== REAL-WORLD SCENARIO ===\n")

    # A veterinary hospital could use a dictionary to associate a unique
    # patient ID with patient information. The ID serves as the key, allowing
    # a particular patient's information to be retrieved without searching
    # through every patient record.
    patient_id = 100

    if patient_id in patient_records:
        print("Patient ID:", patient_id,
              "belongs to:", patient_records[patient_id])
    else:
        print("Patient ID:", patient_id, "not found.")


if __name__ == "__main__":
    main()