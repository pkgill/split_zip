import sys
import os


def split_file(file_path, size_mb):
    """Splits a file into multiple parts with a given size."""
    if not os.path.isfile(file_path):
        print(f"The file {file_path} does not exist.")
        return

    size_bytes = size_mb * 1024 * 1024
    part_number = 1
    file_base_name = os.path.basename(file_path)

    with open(file_path, 'rb') as f:
        chunk = f.read(size_bytes)
        while chunk:
            part_file_name = f"{file_path}_part_{part_number}"
            with open(part_file_name, 'wb') as part_file:
                part_file.write(chunk)

            print(f"Created {part_file_name}")
            part_number += 1
            chunk = f.read(size_bytes)

    print(f"File split into {part_number - 1} parts.")


# Example usage
if len(sys.argv) > 1:
    file_path = sys.argv[1]
    size_mb = 4  # You can change this to your desired default size
    split_file(file_path, size_mb)
else:
    print("No file provided. Please drag and drop a file onto the script.")
