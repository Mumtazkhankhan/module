from pathlib import Path

# All file operations stay inside this dedicated folder beside the script.
ROOT = Path(__file__).resolve().parent / "demo_files"
ROOT.mkdir(exist_ok=True)

def safe_path(name):
    # Accept only a simple filename; prevent paths outside the demo folder.
    if not name or name in {".", ".."} or "/" in name or "\\" in name:
        raise ValueError("Enter a simple file name, not a path.")
    return ROOT / name

def menu():
    while True:
        print(f"\nDEMO FILE SYSTEM: {ROOT}")
        print("1. List files")
        print("2. Create/write a text file")
        print("3. Read a text file")
        print("4. Rename a file")
        print("5. Delete a file")
        print("0. Exit")
        choice = input("Choose: ").strip()

        try:
            if choice == "1":
                items = list(ROOT.iterdir())
                if not items:
                    print("Folder is empty.")
                for item in items:
                    print(("[FILE] " if item.is_file() else "[DIR]  ") + item.name)

            elif choice == "2":
                name = input("New filename (e.g. notes.txt): ").strip()
                path = safe_path(name)
                if path.exists():
                    print("That file already exists; choose another name.")
                    continue
                content = input("Text to save: ")
                path.write_text(content, encoding="utf-8")
                print("File created.")

            elif choice == "3":
                path = safe_path(input("Filename to read: ").strip())
                if path.is_file():
                    print(path.read_text(encoding="utf-8"))
                else:
                    print("File not found.")

            elif choice == "4":
                old = safe_path(input("Current filename: ").strip())
                new = safe_path(input("New filename: ").strip())
                if not old.is_file():
                    print("Source file not found.")
                elif new.exists():
                    print("Destination already exists.")
                else:
                    old.rename(new)
                    print("File renamed.")

            elif choice == "5":
                path = safe_path(input("Filename to delete: ").strip())
                if not path.is_file():
                    print("File not found.")
                elif input(f"Type DELETE to remove {path.name}: ") == "DELETE":
                    path.unlink()
                    print("File deleted.")
                else:
                    print("Cancelled.")

            elif choice == "0":
                break
            else:
                print("Invalid choice.")
        except (OSError, ValueError) as error:
            print("Operation failed:", error)

if __name__ == "__main__":
    print("This demo manages only files inside its own demo_files folder.")
    menu()
