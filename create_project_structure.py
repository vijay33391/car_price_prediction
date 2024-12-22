import os

# Define the corrected project structure with files and folders
project_structure = {
    'data': {
        
    },
    'notebooks': [''],
    'src': {
        'components': ['__init__.py', 'data_ingestion', 'data_preprocessing.py', 'model.py'],
        'pipelines': ['__init__.py', 'test_pipeline.py', 'train_pipeline.py'],
    },
    'tests': ['test_model.py'],
    'utils.py': '',
    'config.yaml': '',
    'requirements.txt': '',
    '.gitignore': '',
    'setup.py': '',
    'README.md': '',  
    'custom_exceptions.py': ''
}

# Function to create directories and files
def create_project_structure(base_path, structure):
    for folder, contents in structure.items():
        folder_path = os.path.join(base_path, folder)
        
        # If the folder path is a dictionary, process it as a subdirectory structure
        if isinstance(contents, dict):
            # Create the folder if it doesn't exist
            if not os.path.exists(folder_path):
                os.makedirs(folder_path, exist_ok=True)
                print(f"Created directory: {folder_path}")
            # Recursively create subdirectories and files
            create_project_structure(folder_path, contents)
        else:
            # If it's a file, check if it exists and create it if not
            if isinstance(contents, list):
                # Create the folder if it doesn't exist
                if not os.path.exists(folder_path):
                    os.makedirs(folder_path)
                    print(f"Created directory: {folder_path}")
                # Now, create the files inside the directory
                for file_name in contents:
                    file_path = os.path.join(folder_path, file_name)
                    if not os.path.exists(file_path):
                        with open(file_path, 'w') as f:
                            if file_name == '__init__.py':  # Special case for init files
                                f.write("# This is an init file for the package\n")
                            else:
                                f.write(f"# Placeholder content for {file_name}\n")
                        print(f"Created file: {file_path}")
            else:
                # Directly create a file in the base directory
                file_path = os.path.join(base_path, folder)
                if not os.path.exists(file_path):
                    with open(file_path, 'w') as f:
                        f.write(f"# Placeholder content for {folder}\n")
                    print(f"Created file: {file_path}")

# Set the base path for your project (current working directory)
base_dir = os.getcwd()  # Get the current working directory

# Create the project structure
create_project_structure(base_dir, project_structure)

# Inform the user that the structure has been processed
print(f"Project structure for 'Car Price Prediction' has been processed at {base_dir}")
