import sys

def main():
    try:
        print("Starting the script...")
        # Simulate some process
        result = perform_task()
        
        if not result:
            print("Task failed, exiting with status 1.")
            sys.exit(1)  # Exit with failure
        
        print("Task succeeded, exiting with status 0.")
        sys.exit(0)  # Exit with success

    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        sys.exit(1)  # Exit with failure on error

def perform_task():
    # Simulate a task that may fail
    # Change this to False to trigger sys.exit(1)
    return false  # Simulates failure; change to True for success

if __name__ == "__main__":
    main()
