from pathlib import Path
import shutil

# Specify the source directory (where files are initially located)
source_dir = Path("Add Path to file you want to sort files in)

# Define destination directories for specific file types
destination_dirs = {
    ".exe": Path(Put in Path to the folder where you want the specific file type to go to),
    ".img": Path(etc.),
    ".mp4": Path(etc.),
    ".docx": Path(etc.)
}

# Iterate through each file inside the source directory
for entry in source_dir.iterdir():
    if entry.is_file():  # Check if the entry is a file
        # Get the file extension (e.g., ".exe", ".img")
        file_extension = entry.suffix.lower()

        # Check if the file extension corresponds to a destination directory
        if file_extension in destination_dirs:
            # Move the file to the corresponding destination directory
            destination_dir = destination_dirs[file_extension]
            destination_dir.mkdir(parents=True, exist_ok=True)  # Ensure the destination directory exists
            shutil.move(entry, destination_dir / entry.name)
            print(f"Moved '{entry.name}' to '{destination_dir}'")
