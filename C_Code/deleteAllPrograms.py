import os
import glob

def delete_exe_files():
    """
    Find and delete all .exe files in the current directory
    """
    # Get the current directory
    current_dir = os.getcwd()
    print(f"Searching for .exe files in: {current_dir}")
    
    # Find all .exe files in the current directory
    exe_files = glob.glob("*.exe")
    
    if not exe_files:
        print("No .exe files found in the current directory.")
        return
    
    print(f"Found {len(exe_files)} .exe file(s):")
    for file in exe_files:
        print(f"  - {file}")
    
    # Ask for confirmation before deleting
    response = input("\nDo you want to delete these files? (Y/n): ").strip().lower()
    
    if response in ['y', 'yes', '']:
        deleted_count = 0
        for file in exe_files:
            try:
                os.remove(file)
                print(f"Deleted: {file}")
                deleted_count += 1
            except OSError as e:
                print(f"Error deleting {file}: {e}")
        
        if len(exe_files) == deleted_count:
            print(f"Successfully deleted all {deleted_count} .exe file(s).")
        else:
            print(f"\nSuccessfully deleted {deleted_count} out of {len(exe_files)} .exe files.")
    else:
        print("Operation cancelled. No files were deleted.")

if __name__ == "__main__":
    delete_exe_files()