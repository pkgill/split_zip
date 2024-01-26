import os
def split_file(file_path, size_mb):
    """Splits a file into multiple parts with a given size."""
    # Calculate the size in bytes
    size_bytes = size_mb * 1024 * 1024
    part_number = 1

    with open(file_path, 'rb') as f:
        chunk = f.read(size_bytes)
        while chunk:
            # Create a new file for each part
            part_name = f"{file_path}_part_{part_number}"
            with open(part_name, 'wb') as part_file:
                part_file.write(chunk)

            # Read the next chunk
            chunk = f.read(size_bytes)
            part_number += 1

    print(f"File split into {part_number - 1} parts.")


# Example usage
file_path = input("Enter the path of the file to split: ")
size_mb = int(input("Enter the size of each part in MB: "))

split_file(file_path, size_mb)
