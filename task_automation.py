#Project Name: Task Automation with Python scripts
#File Organizer
#Language: Python

import os

# Function to create a folder if it does not exist
def createIfNotExists(folder):
    if not os.path.exists(folder):
        os.makedirs(folder)

# Function to move files to a specified folder
def move(foldername, files):
    for file in files:
        os.replace(file, f"{foldername}/{file}")

# Get the list of files in the current directory
files = os.listdir()

# Remove the script file itself from the list
files.remove("task_automation.py")
print(files)

# Create necessary folders if they do not exist
createIfNotExists("Images")
createIfNotExists("Document")
createIfNotExists("code_file")
createIfNotExists("Media")
createIfNotExists("Others")

# Define file extensions for each category
imgExts = [".png", ".jpg", ".jpeg"]
docExts = [".docx", ".pdf", ".txt", ".doc"]
codeExts = [".html", ".css", ".js", ".c", ".cpp"]
mediaExts = [".mp4", ".mp3"]

# Initialize lists to store files for each category
images = [file for file in files if os.path.splitext(file)[1].lower() in imgExts]
doc = [file for file in files if os.path.splitext(file)[1].lower() in docExts]
code = [file for file in files if os.path.splitext(file)[1].lower() in codeExts]
media = [file for file in files if os.path.splitext(file)[1].lower() in mediaExts]

# Initialize a list to store files categorized as 'Others'
others = []
for file in files:
    ext = os.path.splitext(file)[1].lower()
    # Check if the file has an extension not covered by other categories and is a regular file
    if (ext not in mediaExts) and (ext not in codeExts) and (ext not in docExts) and (ext not in imgExts) and os.path.isfile(file):
        others.append(file)


# Move files to their respective folders
move("Media", media)
move("Document", doc)
move("Images", images)
move("code_file", code)
move("Others", others)
