import psutil

def show_processes(limit=25):
    print("\nRUNNING PROCESSES")
    print("-" * 70)
    print(f"{'PID':<10}{'Process Name':<40}{'Status':<15}")
    print("-" * 70)
    count = 0

    for process in psutil.process_iter(["pid", "name", "status"]):
        try:
            info = process.info
            name = (info["name"] or "Unknown")[:39]
            print(f"{info['pid']:<10}{name:<40}{info['status']:<15}")
            count += 1
            if count >= limit:
                break
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            continue

    print(f"\nDisplayed {count} processes.")

if __name__ == "__main__":
    try:
        show_processes()
    except ImportError:
        print("Install the required library with: python -m pip install psutil")
