import socket
import threading

# Some example DIDs and data for demonstration.
DID_DATA = {
    0xF190: b'\x00\x01\x23',   # Example "Software Version"
    0xF191: b'\xAA\xBB\xCC',   # Example "Hardware Version"
}

def handle_uds_request(data: bytes) -> bytes:
    """
    Parse an incoming UDS request and generate a UDS response.
    Supports:
      - Diagnostic Session Control (0x10)
      - ECU Reset (0x11)
      - Read Data By Identifier (0x22)
      - Write Data By Identifier (0x2E)
      - Routine Control (0x31)
    """
    if not data:
        # No data => no response
        return b''

    sid = data[0]

    if sid == 0x10:
        # Diagnostic Session Control
        # Positive response = SID+0x40 => 0x50
        return b'\x50' + data[1:]

    elif sid == 0x11:
        # ECU Reset
        # Positive response = 0x51
        return b'\x51' + data[1:]

    elif sid == 0x22:
        # Read Data By Identifier
        if len(data) < 3:
            return b'\x7F\x22\x13'  # Incorrect Length

        did_high = data[1]
        did_low = data[2]
        did = (did_high << 8) + did_low

        if did in DID_DATA:
            # Positive response = 0x62
            return b'\x62' + data[1:] + DID_DATA[did]
        else:
            # DID not supported
            return b'\x7F\x22\x31'  # Request Out Of Range

    elif sid == 0x2E:
        # Write Data By Identifier
        if len(data) < 4:
            return b'\x7F\x2E\x13'  # Incorrect Length

        did_high = data[1]
        did_low = data[2]
        did = (did_high << 8) + did_low
        payload = data[3:]
        # Store in DID_DATA
        DID_DATA[did] = payload

        # Positive response = 0x6E
        return b'\x6E' + data[1:]

    elif sid == 0x31:
        # Routine Control
        # Simplified => always positive
        return b'\x71' + data[1:]

    else:
        # Unknown SID => Negative Response
        return b'\x7F' + bytes([sid]) + b'\x11'  # NRC 0x11 = Service Not Supported

def client_handler(conn: socket.socket, addr):
    """
    Handle UDS requests from a single client in a loop until they disconnect.
    We also log each request/response in hex to simulate "ECU logging".
    """
    print(f"[+] Client connected: {addr}")
    with conn:
        while True:
            data = conn.recv(1024)
            if not data:
                print(f"[-] Client disconnected: {addr}")
                break

            # Log the request in hex
            req_hex = ' '.join(f'{b:02X}' for b in data)
            print(f"[{addr}] Received UDS Request: {req_hex}")

            # Process the request
            response = handle_uds_request(data)

            # Log the response in hex
            resp_hex = ' '.join(f'{b:02X}' for b in response)
            print(f"[{addr}] Sending UDS Response: {resp_hex}")

            # Send the response back
            conn.sendall(response)

def run_server(host='127.0.0.1', port=5555):
    """
    UDS server that stays awake indefinitely, accepts multiple client connections,
    and logs each request and response.
    """
    print(f"UDS Server listening on {host}:{port}...\n")
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_sock:
        # Allows quick rebinding after a crash or close
        server_sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        server_sock.bind((host, port))
        server_sock.listen()

        while True:
            conn, addr = server_sock.accept()
            thread = threading.Thread(
                target=client_handler,
                args=(conn, addr),
                daemon=True
            )
            thread.start()

if __name__ == '__main__':
    run_server()
