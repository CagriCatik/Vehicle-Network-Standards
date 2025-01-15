import socket

def parse_hex_string_to_bytes(input_str: str) -> bytes:
    """
    Given a string like "22 F1 90", convert it to bytes b'\x22\xF1\x90'.
    Raises ValueError if something is invalid.
    """
    tokens = [t for t in input_str.strip().split(' ') if t]
    try:
        values = [int(token, 16) for token in tokens]
    except ValueError:
        raise ValueError("Invalid hex input. Enter bytes in hex, e.g. '22 F1 90'")
    return bytes(values)

def run_client(host='127.0.0.1', port=5555):
    """
    Interactive UDS client that connects to the server,
    allows user to type commands, and prints responses in hex.
    """
    print(f"Connecting to UDS server at {host}:{port}...")
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_sock:
        client_sock.connect((host, port))
        print("[+] Connected to server.")

        print("\nEnter UDS commands in hex, e.g.:\n  22 F1 90  => Read Data By Identifier (DID=F190)\n"
              "Type 'q' or 'quit' to exit.\n")

        while True:
            user_input = input("UDS> ")

            if user_input.lower() in ['q', 'quit']:
                print("Exiting client.")
                break

            try:
                uds_request = parse_hex_string_to_bytes(user_input)
            except ValueError as e:
                print(f"Error: {e}")
                continue

            client_sock.sendall(uds_request)
            response = client_sock.recv(1024)
            if not response:
                print("[-] Server disconnected.")
                break

            response_hex = " ".join(f"{byte:02X}" for byte in response)
            print(f"Response: {response_hex}")

if __name__ == '__main__':
    run_client()
