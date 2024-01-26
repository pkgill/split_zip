import os

def join_files(start_part_path):

    """Joins files split by the split_file script."""
    # Extract the base file name
    base_file_name = start_part_path.rsplit('_part_', 1)[0]

    # Check if the first part file exists
    if not os.path.exists(start_part_path):
        print(f"File {start_part_path} not found.")
        return

    # Start joining files
    with open(base_file_name + '_rejoined', 'wb') as output_file:
        part_number = 1
        while True:
            part_file_name = f"{base_file_name}_part_{part_number}"
            if not os.path.exists(part_file_name):
                break  # No more parts exist

            with open(part_file_name, 'rb') as part_file:
                output_file.write(part_file.read())

            part_number += 1

    print(f"Files joined into {base_file_name}_rejoined.")

# Example usage
start_part_path = input("Enter the path of the first part: ")

join_files(start_part_path)
