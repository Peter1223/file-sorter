from pathlib import Path
import shutil

# Specify the source directory (where files are initially located)
source_dir = Path(r'C:\Users\osipc\Downloads')

# Define destination directories for specific file types
destination_dirs = {
    ".exe": Path(r'C:\Users\osipc\Downloads\Executables'),
    ".img": Path(r'C:\Users\osipc\Downloads\Images'),
    ".mp4": Path(r'C:\Users\osipc\Downloads\Videos'),
    ".docx": Path(r'C:\Users\osipc\Downloads\Docs'),
    ".doc": Path(r'C:\Users\osipc\Downloads\Docs'),
    ".pdf": Path(r'C:\Users\osipc\Downloads\Docs'),
    ".zip": Path(r'C:\Users\osipc\Downloads\Zip'),
    ".png": Path(r'C:\Users\osipc\Downloads\Images'),
    ".jpg": Path(r'C:\Users\osipc\Downloads\Images'),
    ".xlsm": Path(r'C:\Users\osipc\Downloads\excel'),
    ".csv": Path(r'C:\Users\osipc\Downloads\excel'),
    ".xlsx": Path(r'C:\Users\osipc\Downloads\excel'),
    ".py": Path(r'C:\Users\osipc\Downloads\Python')
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
