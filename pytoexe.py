import os
import subprocess

def convert_to_exe():
    python_file_dir = r"C:\Users\adity\Desktop\eyecourser.py"
    
    # Check if the directory exists
    if not os.path.exists(python_file_dir):
        print(f"Error: Directory '{python_file_dir}' does not exist.")
        return
    
    # Check if the path is a file
    if not os.path.isfile(python_file_dir):
        print(f"Error: '{python_file_dir}' is not a valid file.")
        return
    
    # Get the base name of the file without the extension
    base_name = os.path.splitext(os.path.basename(python_file_dir))[0]
    
    # Run PyInstaller to convert the Python file to .exe
    cmd = ['pyinstaller', '--onefile', python_file_dir]
    
    try:
        subprocess.check_call(cmd)
        print(f"\nSuccessfully converted '{python_file_dir}' to '{base_name}.exe'.")
    except subprocess.CalledProcessError as e:
        print(f"\nError converting '{python_file_dir}' to .exe: {e}")

if __name__ == "__main__":
    convert_to_exe()
