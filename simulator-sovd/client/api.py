# client/api.py

def fetch_operational_data(self, component_id):
    """Fetch operational data for a specific component."""
    endpoint = f"{self.base_url}/components/{component_id}/data"
    params = {"categories": "operationalData"}
    response = requests.get(endpoint, headers=self.get_headers(), params=params)
    response.raise_for_status()
    return response.json()


class AuthenticatedSOVDClient:
    def __init__(self, base_url=BASE_URL, verify_ssl=VERIFY_SSL):
        self.base_url = base_url
        self.token = None
        self.verify_ssl = verify_ssl
    
    # Modify all requests to include 'verify=self.verify_ssl'
    def authenticate(self, username, password):
        endpoint = f"{self.base_url}/auth/login"
        payload = {"username": username, "password": password}
        response = requests.post(endpoint, json=payload, verify=self.verify_ssl)
        response.raise_for_status()
        self.token = response.json().get("access_token")
    
    def list_components(self):
        endpoint = f"{self.base_url}/components"
        response = requests.get(endpoint, headers=self.get_headers(), verify=self.verify_ssl)
        response.raise_for_status()
        return response.json()
    
    # Similarly, update other methods to include 'verify=self.verify_ssl'
