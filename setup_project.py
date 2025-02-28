import os

# Define the project structure
project_structure = {
    "youtube_recommender": {
        "backend": [
            "api.py",           # Backend API (Flask)
            "youtube_api.py",   # Fetch YouTube Data
            "nlp_ranking.py",   # NLP-based ranking
            "config.py",        # Store API keys & settings
            "requirements.txt", # Backend dependencies
            "run.py"            # Start Flask server
        ],
        "frontend": [
            "app.py",           # Streamlit UI
            "requirements.txt"  # Frontend dependencies
        ],
        "docs": [
            "deployment_guide.md"  # Deployment Steps
        ]
    }
}

# Create folders and files
def create_project_structure(base_path, structure):
    for folder, files in structure.items():
        folder_path = os.path.join(base_path, folder)
        os.makedirs(folder_path, exist_ok=True)

        for sub_folder, sub_files in files.items():
            sub_folder_path = os.path.join(folder_path, sub_folder)
            os.makedirs(sub_folder_path, exist_ok=True)

            for file in sub_files:
                file_path = os.path.join(sub_folder_path, file)
                if not os.path.exists(file_path):
                    with open(file_path, "w") as f:
                        f.write(f"# {file} - Auto-generated file\n")

# Run the script
if __name__ == "__main__":
    base_directory = os.getcwd()  # Use the current directory
    create_project_structure(base_directory, project_structure)
    print("✅ Project structure created successfully!")
