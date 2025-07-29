from flask import Flask, request, redirect, session, jsonify
from google.auth.transport import requests
from google.oauth2 import id_token
from google_auth_oauthlib.flow import Flow
import os
import threading
from firebase_admin import auth

app = Flask(__name__)
app.secret_key = 'theSecret'  # Set a secret key for session management

# Google OAuth2 configuration
GOOGLE_CLIENT_ID = "235399780285-cjvelvv1aa3khgfm387f6eulph87ipa0.apps.googleusercontent.com"  # Replace with your actual client ID
GOOGLE_CLIENT_SECRET = "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"  # Replace with your actual client secret
REDIRECT_URI = "http://localhost:5000/callback"

# OAuth2 flow configuration
os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"  # Allow HTTP for local development

# Global variables to store authentication result
auth_result = {"status": "pending", "user": None, "error": None}
server_shutdown = False

def create_flow():
    """Create OAuth2 flow"""
    flow = Flow.from_client_config({
        "web": {
            "client_id": GOOGLE_CLIENT_ID,
            "client_secret": GOOGLE_CLIENT_SECRET,
            "auth_uri": "https://accounts.google.com/o/oauth2/auth",
            "token_uri": "https://oauth2.googleapis.com/token",
            "redirect_uris": [REDIRECT_URI]
        }
    }, scopes=[
        "https://www.googleapis.com/auth/userinfo.email",
        "https://www.googleapis.com/auth/userinfo.profile", 
        "openid"
    ])
    flow.redirect_uri = REDIRECT_URI
    return flow

@app.route('/')
def index():
    """Main route - redirect to Google OAuth"""
    flow = create_flow()
    authorization_url, state = flow.authorization_url(
        access_type='offline',
        include_granted_scopes='true'
    )
    session['state'] = state
    return redirect(authorization_url)

@app.route('/callback')
def callback():
    """Handle OAuth callback from Google"""
    global auth_result, server_shutdown
    
    try:
        # Verify state parameter
        if request.args.get('state') != session.get('state'):
            auth_result = {"status": "error", "user": None, "error": "Invalid state parameter"}
            return "Authentication failed: Invalid state parameter"
        
        # Exchange authorization code for tokens
        flow = create_flow()
        flow.fetch_token(authorization_response=request.url)
        
        # Get user info from Google
        credentials = flow.credentials
        request_session = requests.Request()

        # Use the access token to get user info from Google's userinfo endpoint
        import urllib.request
        import json as json_module
        
        try:
            # Get user info using the access token
            userinfo_url = f"https://www.googleapis.com/oauth2/v2/userinfo?access_token={credentials.token}"
            with urllib.request.urlopen(userinfo_url) as response:
                user_data = json_module.loads(response.read().decode())
            
            # Extract user information
            user_info = {
                "email": user_data.get("email"),
                "name": user_data.get("name"),
                "picture": user_data.get("picture"),
                "sub": user_data.get("id"),  # Google user ID
                "access_token": credentials.token
            }
            
        except Exception as userinfo_error:
            # Fallback: try to get ID token if available
            id_token_jwt = getattr(credentials, 'id_token', None)
            if id_token_jwt:
                # Verify the ID token
                id_info = id_token.verify_oauth2_token(
                    id_token_jwt, request_session, GOOGLE_CLIENT_ID
                )
                
                user_info = {
                    "email": id_info.get("email"),
                    "name": id_info.get("name"),
                    "picture": id_info.get("picture"),
                    "sub": id_info.get("sub"),
                    "id_token": id_token_jwt
                }
            else:
                raise Exception(f"Could not get user info: {str(userinfo_error)}")
        
        # Try to create/get Firebase user
        try:
            # Check if user exists in Firebase
            firebase_user = auth.get_user_by_email(user_info["email"])
        except auth.UserNotFoundError:
            # User doesn't exist, create them
            firebase_user = auth.create_user(
                email=user_info["email"],
                display_name=user_info["name"],
                photo_url=user_info["picture"]
            )
        
        # Create custom token for Firebase authentication
        custom_token = auth.create_custom_token(firebase_user.uid)
        
        auth_result = {
            "status": "success",
            "user": {
                "email": user_info["email"],
                "name": user_info["name"],
                "picture": user_info["picture"],
                "uid": firebase_user.uid,
                "custom_token": custom_token.decode('utf-8'),
                "id_token": user_info.get("id_token", ""),
                "access_token": user_info.get("access_token", "")
            },
            "error": None
        }
        
        # Schedule server shutdown
        threading.Timer(2.0, shutdown_server).start()
        
        return """
        <html>
            <body>
                <h2>Authentication Successful!</h2>
                <p>You have been successfully authenticated with Google.</p>
                <p>You can now close this window and return to the application.</p>
                <script>
                    setTimeout(function() {
                        window.close();
                    }, 2000);
                </script>
            </body>
        </html>
        """
        
    except Exception as e:
        auth_result = {"status": "error", "user": None, "error": str(e)}
        return f"Authentication failed: {str(e)}"

@app.route('/status')
def status():
    """Check authentication status"""
    return jsonify(auth_result)

@app.route('/shutdown')
def shutdown():
    """Manually shutdown the server"""
    shutdown_server()
    return "Server shutting down..."

def shutdown_server():
    """Shutdown the Flask server"""
    global server_shutdown
    server_shutdown = True
    func = request.environ.get('werkzeug.server.shutdown')
    if func is None:
        raise RuntimeError('Not running with the Werkzeug Server')
    func()

def get_auth_result():
    """Get the current authentication result"""
    return auth_result

def reset_auth_result():
    """Reset the authentication result"""
    global auth_result
    auth_result = {"status": "pending", "user": None, "error": None}

def run_server(host='localhost', port=5000, debug=False):
    """Run the Flask server"""
    app.run(host=host, port=port, debug=debug, use_reloader=False)

if __name__ == '__main__':
    run_server(debug=True)
