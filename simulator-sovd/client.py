import requests
import json

BASE_URL = "http://127.0.0.1:5000"

def list_components():
    """List all available components."""
    try:
        response = requests.get(f"{BASE_URL}/components")
        response.raise_for_status()
        components = response.json().get("items", [])
        print("\nAvailable Components:")
        for comp in components:
            print(f" - ID: {comp['id']}, Name: {comp['name']}")
    except requests.exceptions.RequestException as e:
        print(f"Error fetching components: {e}")

def fetch_faults(component_id):
    """Fetch faults for a specific component."""
    try:
        response = requests.get(f"{BASE_URL}/components/{component_id}/faults")
        response.raise_for_status()
        faults = response.json().get("items", [])
        if faults:
            print(f"\nFaults for '{component_id}':")
            for fault in faults:
                print(f" - Code: {fault['code']}, Description: {fault['description']}")
        else:
            print(f"\nNo faults found for '{component_id}'.")
    except requests.exceptions.HTTPError as http_err:
        if response.status_code == 404:
            print(f"Component '{component_id}' not found.")
        else:
            print(f"HTTP error occurred: {http_err}")
    except requests.exceptions.RequestException as e:
        print(f"Error fetching faults: {e}")

def fetch_ident_data(component_id):
    """Fetch identification data for a specific component."""
    try:
        response = requests.get(f"{BASE_URL}/components/{component_id}/data?categories=identData")
        response.raise_for_status()
        ident_data = response.json().get("identData", [])
        print(f"\nIdentification Data for '{component_id}':")
        for data in ident_data:
            print(f" - {data['id'].upper()}: {data['value']}")
    except requests.exceptions.HTTPError as http_err:
        if response.status_code == 404:
            print(f"Component '{component_id}' not found.")
        else:
            print(f"HTTP error occurred: {http_err}")
    except requests.exceptions.RequestException as e:
        print(f"Error fetching identification data: {e}")

def execute_reset_operation(component_id):
    """Execute a reset operation on a specific component."""
    try:
        payload = {"operation": "reset"}
        response = requests.post(f"{BASE_URL}/components/{component_id}/operations", json=payload)
        response.raise_for_status()
        message = response.json().get("message", "Operation executed successfully.")
        print(f"\n{message}")
    except requests.exceptions.HTTPError as http_err:
        if response.status_code == 404:
            print(f"Component '{component_id}' not found.")
        elif response.status_code == 400:
            error = response.json().get("error", "Bad Request")
            print(f"Operation failed: {error}")
        else:
            print(f"HTTP error occurred: {http_err}")
    except requests.exceptions.RequestException as e:
        print(f"Error executing operation: {e}")

def clear_fault_code(component_id, fault_code):
    """Clear a specific fault code from a component."""
    try:
        response = requests.delete(f"{BASE_URL}/components/{component_id}/faults", params={"code": fault_code})
        response.raise_for_status()
        message = response.json().get("message", "Fault cleared successfully.")
        print(f"\n{message}")
    except requests.exceptions.HTTPError as http_err:
        if response.status_code == 404:
            error = response.json().get("error", "Component or fault code not found.")
            print(f"Error: {error}")
        elif response.status_code == 400:
            error = response.json().get("error", "Bad Request")
            print(f"Error: {error}")
        else:
            print(f"HTTP error occurred: {http_err}")
    except requests.exceptions.RequestException as e:
        print(f"Error clearing fault: {e}")

def main_menu():
    """Display the main menu and handle user input."""
    while True:
        print("\n--- SOVD Client Menu ---")
        print("1. List Components")
        print("2. Fetch Faults")
        print("3. Fetch Identification Data")
        print("4. Execute Reset Operation")
        print("5. Clear Fault Code")
        print("6. Exit")
        
        choice = input("Select an option (1-6): ").strip()
        
        if choice == "1":
            list_components()
        elif choice == "2":
            component_id = input("Enter Component ID: ").strip()
            fetch_faults(component_id)
        elif choice == "3":
            component_id = input("Enter Component ID: ").strip()
            fetch_ident_data(component_id)
        elif choice == "4":
            component_id = input("Enter Component ID: ").strip()
            execute_reset_operation(component_id)
        elif choice == "5":
            component_id = input("Enter Component ID: ").strip()
            fault_code = input("Enter Fault Code to Clear: ").strip()
            clear_fault_code(component_id, fault_code)
        elif choice == "6":
            print("Exiting SOVD Client. Goodbye!")
            break
        else:
            print("Invalid selection. Please choose a number between 1 and 6.")

if __name__ == "__main__":
    main_menu()
