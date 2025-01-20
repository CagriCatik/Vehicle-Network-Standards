# client/security.py

import requests
from app.config import BASE_URL

class AuthenticatedSOVDClient:
    def __init__(self, base_url=BASE_URL):
        self.base_url = base_url
        self.token = None
    
    def authenticate(self, username, password):
        """
        Authenticate with the server to obtain a JWT token.
        """
        endpoint = f"{self.base_url}/auth/login"
        payload = {"username": username, "password": password}
        response = requests.post(endpoint, json=payload)
        response.raise_for_status()
        self.token = response.json().get("access_token")
    
    def get_headers(self):
        if not self.token:
            raise Exception("Authentication token not available. Please authenticate first.")
        return {"Authorization": f"Bearer {self.token}"}
    
    # Override existing methods to include headers
    def list_components(self):
        endpoint = f"{self.base_url}/components"
        response = requests.get(endpoint, headers=self.get_headers())
        response.raise_for_status()
        return response.json()
    
    def fetch_faults(self, component_id, severity=None, status=None):
        endpoint = f"{self.base_url}/components/{component_id}/faults"
        params = {}
        if severity:
            params['severity'] = severity
        if status:
            params['status'] = status
        response = requests.get(endpoint, headers=self.get_headers(), params=params)
        response.raise_for_status()
        return response.json()
    
    def fetch_ident_data(self, component_id):
        endpoint = f"{self.base_url}/components/{component_id}/data"
        params = {"categories": "identData"}
        response = requests.get(endpoint, headers=self.get_headers(), params=params)
        response.raise_for_status()
        return response.json()
    
    def execute_operation(self, component_id, operation):
        endpoint = f"{self.base_url}/components/{component_id}/operations"
        payload = {"operation": operation}
        response = requests.post(endpoint, headers=self.get_headers(), json=payload)
        response.raise_for_status()
        return response.json()
    
    def clear_fault_code(self, component_id, fault_code):
        endpoint = f"{self.base_url}/components/{component_id}/faults"
        params = {"code": fault_code}
        response = requests.delete(endpoint, headers=self.get_headers(), params=params)
        response.raise_for_status()
        return response.json()
