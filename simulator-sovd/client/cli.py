# client/cli.py

import argparse
from app.api import AuthenticatedSOVDClient
from app.utils import print_table
import getpass

def main():
    client = AuthenticatedSOVDClient()
    parser = argparse.ArgumentParser(description="SOVD Client CLI for Automotive Diagnostics")
    subparsers = parser.add_subparsers(dest='command', help='Available commands')
    
    # Authenticate
    auth_parser = subparsers.add_parser('auth', help='Authenticate with the SOVD server')
    auth_parser.add_argument('username', help='Username for authentication')
    # Password will be prompted securely
    
    # List Components
    subparsers.add_parser('list', help='List all components')
    
    # Fetch Faults
    faults_parser = subparsers.add_parser('faults', help='Fetch faults for a component')
    faults_parser.add_argument('component_id', help='ID of the component')
    faults_parser.add_argument('--severity', help='Filter faults by severity', choices=['low', 'medium', 'high'])
    faults_parser.add_argument('--status', help='Filter faults by status', choices=['open', 'cleared'])
    
    # Fetch Identification Data
    ident_parser = subparsers.add_parser('ident', help='Fetch identification data for a component')
    ident_parser.add_argument('component_id', help='ID of the component')
    
    # Execute Operation
    op_parser = subparsers.add_parser('operate', help='Execute operation on a component')
    op_parser.add_argument('component_id', help='ID of the component')
    op_parser.add_argument('operation', help='Operation to execute', choices=['reset', 'lock', 'unlock'])
    
    # Clear Fault Code
    clear_parser = subparsers.add_parser('clear', help='Clear a fault code from a component')
    clear_parser.add_argument('component_id', help='ID of the component')
    clear_parser.add_argument('fault_code', help='Fault code to clear')
    
    args = parser.parse_args()
    
    try:
        if args.command == 'auth':
            password = getpass.getpass(prompt='Password: ')
            client.authenticate(username=args.username, password=password)
            print("Authentication successful. Token acquired.")
        elif args.command == 'list':
            data = client.list_components()
            print_table(data['items'], headers=['ID', 'Name'])
        elif args.command == 'faults':
            data = client.fetch_faults(args.component_id, args.severity, args.status)
            if data['items']:
                print_table(data['items'], headers=['ID', 'Code', 'Description', 'Severity', 'Status'])
            else:
                print(f"No faults found for component '{args.component_id}'.")
        elif args.command == 'ident':
            data = client.fetch_ident_data(args.component_id)
            ident_data = data.get('identData', [])
            print_table(ident_data, headers=['ID', 'Value'])
        elif args.command == 'operate':
            data = client.execute_operation(args.component_id, args.operation)
            print(data.get('message', 'Operation executed successfully.'))
        elif args.command == 'clear':
            data = client.clear_fault_code(args.component_id, args.fault_code)
            print(data.get('message', 'Fault cleared successfully.'))
        else:
            parser.print_help()
    except requests.exceptions.HTTPError as http_err:
        error_message = http_err.response.json().get('error', '')
        print(f"HTTP error occurred: {http_err} - {error_message}")
    except requests.exceptions.RequestException as err:
        print(f"Error: {err}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()


import argparse
from app.api import AuthenticatedSOVDClient
from app.utils import print_table
import getpass
import time
import threading

def monitor_component(client, component_id, interval=5):
    try:
        while True:
            data = client.fetch_ident_data(component_id)
            ident_data = data.get('identData', [])
            operational_data = client.fetch_operational_data(component_id)
            print("\n--- Real-Time Data ---")
            print_table(ident_data, headers=['ID', 'Value'])
            print_table(operational_data.get('operationalData', []), headers=['ID', 'Value'])
            time.sleep(interval)
    except KeyboardInterrupt:
        print("\nStopped real-time monitoring.")

def main():
    client = AuthenticatedSOVDClient()
    parser = argparse.ArgumentParser(description="SOVD Client CLI for Automotive Diagnostics")
    subparsers = parser.add_subparsers(dest='command', help='Available commands')
    
    # Existing parsers...
    
    # Monitor Component
    monitor_parser = subparsers.add_parser('monitor', help='Monitor real-time data for a component')
    monitor_parser.add_argument('component_id', help='ID of the component')
    monitor_parser.add_argument('--interval', type=int, default=5, help='Update interval in seconds')
    
    args = parser.parse_args()
    
    try:
        if args.command == 'auth':
            password = getpass.getpass(prompt='Password: ')
            client.authenticate(username=args.username, password=password)
            print("Authentication successful. Token acquired.")
        elif args.command == 'list':
            data = client.list_components()
            print_table(data['items'], headers=['ID', 'Name'])
        elif args.command == 'faults':
            data = client.fetch_faults(args.component_id, args.severity, args.status)
            if data['items']:
                print_table(data['items'], headers=['ID', 'Code', 'Description', 'Severity', 'Status'])
            else:
                print(f"No faults found for component '{args.component_id}'.")
        elif args.command == 'ident':
            data = client.fetch_ident_data(args.component_id)
            ident_data = data.get('identData', [])
            print_table(ident_data, headers=['ID', 'Value'])
        elif args.command == 'operate':
            data = client.execute_operation(args.component_id, args.operation)
            print(data.get('message', 'Operation executed successfully.'))
        elif args.command == 'clear':
            data = client.clear_fault_code(args.component_id, args.fault_code)
            print(data.get('message', 'Fault cleared successfully.'))
        elif args.command == 'monitor':
            print(f"Starting real-time monitoring for component '{args.component_id}' every {args.interval} seconds. Press Ctrl+C to stop.")
            monitor_component(client, args.component_id, args.interval)
        else:
            parser.print_help()
    except requests.exceptions.HTTPError as http_err:
        error_message = http_err.response.json().get('error', '')
        print(f"HTTP error occurred: {http_err} - {error_message}")
    except requests.exceptions.RequestException as err:
        print(f"Error: {err}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
