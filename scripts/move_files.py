import os
import shutil
import re


def extract_and_copy_files(source_dir, target_dir, search_char):
    """
    Extract files with specific character in their names from the source directory
    and copy them to the target directory.

    Args:
        source_dir (str): The directory to search for files.
        target_dir (str): The directory to copy the matching files to.
        search_char (str): The character or substring to search for in file names.
    """
    # Ensure the target directory exists
    os.makedirs(target_dir, exist_ok=True)

    # Iterate through the source directory
    for root, _, files in os.walk(source_dir):
        for file in files:
            # Check if the file name contains the search character
            if search_char in file:
                source_path = os.path.join(root, file)
                target_path = os.path.join(target_dir, file)

                # Copy the file to the target directory
                shutil.copy2(source_path, target_path)
                print(f"Copied: {source_path} to {target_path}")


# # Example usage
# source_directory = "/home/galois/dataset/YCB/data3/data/0002"  # Replace with your source directory
# target_directory = "/home/galois/dataset/GS/YCB"  # Replace with your target directory
# character_to_search = "color.jpg"  # Replace with the character or substring to search for
#
# extract_and_copy_files(source_directory, target_directory, character_to_search)


def copy_files_with_character_and_divisible_number(source_dir, target_dir, specific_char, divisible_by):
    """
    Extract files with a specific character in their names and a number divisible by a given value,
    then copy them to the target directory.

    Args:
        source_dir (str): Path to the source directory.
        target_dir (str): Path to the target directory.
        specific_char (str): The character or substring to search for in filenames.
        divisible_by (int): The number by which extracted numbers must be divisible.
    """
    # Check if the source directory exists
    if not os.path.exists(source_dir):
        print(f"Source directory '{source_dir}' does not exist.")
        return

    # Create the target directory if it doesn't exist
    if not os.path.exists(target_dir):
        os.makedirs(target_dir)

    # Iterate over all files in the source directory
    for root, _, files in os.walk(source_dir):
        for file in files:
            # Check if the specific character is in the filename
            if specific_char in file:
                # Extract numbers from the filename using regex
                numbers = re.findall(r'\d+', file)  # Find all numeric sequences in the filename

                if numbers:  # If numbers are found
                    for num in numbers:
                        # Convert to integer to handle leading zeros and check divisibility
                        if int(num) % divisible_by == 0:
                            # Construct full file paths
                            source_file_path = os.path.join(root, file)
                            target_file_path = os.path.join(target_dir, file)

                            # Copy the file to the target directory
                            shutil.copy2(source_file_path, target_file_path)
                            print(f"Copied: {source_file_path} -> {target_file_path}")
                            break  # Avoid copying the same file multiple times

    print("File copying completed.")


# Example usage
source_directory = "/home/galois/dataset/YCB/data3/data/0003"
target_directory = "/home/galois/dataset/GS/YCB/003"
character_to_search = "color.jpg"  # Replace with the character or substring to match
divisible_by_number = 53  # Replace with the number for divisibility check

copy_files_with_character_and_divisible_number(source_directory, target_directory, character_to_search,
                                               divisible_by_number)
