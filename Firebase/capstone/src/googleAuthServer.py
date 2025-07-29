import threading
import time
import webbrowser
import requests
from googleAuthHelper import run_server, reset_auth_result

def start_auth_flow(host='localhost', port=5000):
    """Start the Google authentication flow"""
    baseURL = f"http://{host}:{port}"
    reset_auth_result()
    
    
    server_thread = threading.Thread(
        target=run_server,
        kwargs={'host': host, 'port': port, 'debug': False},
        daemon=True
    )
    server_thread.start()
    
    # Waiting for Server Start
    time.sleep(1)
    
    
    webbrowser.open(baseURL)
    
    # Wait for authentication to complete
    return wait_for_auth_result(baseURL)

def wait_for_auth_result(baseURL, timeout=120):
    """Wait for authentication result with timeout"""
    startTime = time.time()
    
    while time.time() - startTime < timeout:
        try:
            # Check authentication status
            response = requests.get(f"{baseURL}/status", timeout=5)
            if response.status_code == 200:
                result = response.json()
                
                return result
                
            # Still pending, wait a bit more
            time.sleep(1)
            
        except requests.exceptions.RequestException:
            # Server might be shutting down or not responding
            time.sleep(1)
            continue
    
    # Timeout reached
    return {"status": "error", "user": None, "error": "Authentication timeout"}

def shutdown_server(base_url):
    """Manually shutdown the server"""
    try:
        requests.get(f"{base_url}/shutdown", timeout=5)
    except requests.exceptions.RequestException:
        pass  # Server might already be down

def google_login():
    """Simplified function to perform Google login"""
    result = start_auth_flow()
    
    if result["status"] == "success":
        return result["user"]
    else:
        print(f"Authentication failed: {result.get('error', 'Unknown error')}")
        return None
