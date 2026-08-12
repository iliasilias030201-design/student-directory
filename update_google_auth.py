with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()

# Add Google GIS script to <head>
google_script_tag = '<script src="https://accounts.google.com/gsi/client" async defer></script>\n</head>'
html = html.replace("</head>", google_script_tag)

# Update the Auth container HTML to include the Google Sign-In button container
old_auth = """        <!-- User Authentication Section -->
        <div class="auth-container" id="authSection">
            <div id="loggedOutView">
                <h3 style="margin-top:0; font-size:1.1rem; color:var(--text);">Student Account Access</h3>
                <p style="font-size:0.85rem; color:var(--meta); margin-bottom:10px;">Sign up or log in to create and save your own tools.</p>
                <input type="text" id="authUsername" class="auth-input" placeholder="Enter your username...">
                <button class="auth-btn" onclick="handleAuth()">Sign Up / Login</button>
            </div>
            <div id="loggedInView" style="display:none;">
                <p style="margin:0; font-weight:bold; color:var(--text);" id="userGreeting"></p>
                <button class="auth-btn logout-btn" onclick="handleLogout()">Log Out</button>
            </div>
        </div>"""

new_auth = """        <!-- User Authentication Section (Google One-Tap / Account Selection) -->
        <div class="auth-container" id="authSection">
            <div id="loggedOutView">
                <h3 style="margin-top:0; font-size:1.1rem; color:var(--text);">Student Account Access</h3>
                <p style="font-size:0.85rem; color:var(--meta); margin-bottom:12px;">Sign in instantly with your Google account (No password required).</p>
                <!-- Google Sign-In Button Element -->
                <div id="g_id_onload"
                     data-client_id="YOUR_GOOGLE_CLIENT_ID.apps.googleusercontent.com"
                     data-callback="handleGoogleLogin"
                     data-auto_prompt="false">
                </div>
                <div class="g_id_signin"
                     data-type="standard"
                     data-size="large"
                     data-theme="outline"
                     data-text="sign_in_with"
                     data-shape="rectangular"
                     data-logo_alignment="center">
                </div>
            </div>
            <div id="loggedInView" style="display:none;">
                <p style="margin:0 0 8px 0; font-weight:bold; color:var(--text);" id="userGreeting"></p>
                <p style="font-size:0.75rem; color:var(--meta); margin:0 0 10px 0;">Your custom tools are securely saved to your local browser storage.</p>
                <button class="auth-btn logout-btn" onclick="handleLogout()">Log Out</button>
            </div>
        </div>"""

html = html.replace(old_auth, new_auth)

# Update JavaScript logic for decoding Google Credential JWT and managing session state
old_js_auth = """        let userTools = JSON.parse(localStorage.getItem('student_user_tools') || '[]');
        let currentUser = localStorage.getItem('student_current_user') || '';

        function checkAuth() {
            if (currentUser) {
                document.getElementById('loggedOutView').style.display = 'none';
                document.getElementById('loggedInView').style.display = 'block';
                document.getElementById('userGreeting').innerText = 'Logged in as: ' + currentUser;
                document.getElementById('submitSection').style.display = 'block';
            } else {
                document.getElementById('loggedOutView').style.display = 'block';
                document.getElementById('loggedInView').style.display = 'none';
                document.getElementById('submitSection').style.display = 'none';
            }
        }

        function handleAuth() {
            let uname = document.getElementById('authUsername').value.trim();
            if(!uname) return;
            currentUser = uname;
            localStorage.setItem('student_current_user', currentUser);
            document.getElementById('authUsername').value = '';
            checkAuth();
        }

        function handleLogout() {
            currentUser = '';
            localStorage.removeItem('student_current_user');
            checkAuth();
        }"""

new_js_auth = """        let userTools = JSON.parse(localStorage.getItem('student_user_tools') || '[]');
        let currentUser = localStorage.getItem('student_current_user') || '';

        function checkAuth() {
            if (currentUser) {
                document.getElementById('loggedOutView').style.display = 'none';
                document.getElementById('loggedInView').style.display = 'block';
                document.getElementById('userGreeting').innerText = 'Welcome back, ' + currentUser + '! 👋';
                document.getElementById('submitSection').style.display = 'block';
            } else {
                document.getElementById('loggedOutView').style.display = 'block';
                document.getElementById('loggedInView').style.display = 'none';
                document.getElementById('submitSection').style.display = 'none';
            }
        }

        // Decode Google JWT payload safely on client side
        function parseJwt(token) {
            try {
                let base64Url = token.split('.')[1];
                let base64 = base64Url.replace(/-/g, '+').replace(/_/g, '/');
                let jsonPayload = decodeURIComponent(atob(base64).split('').map(function(c) {
                    return '%' + ('00' + c.charCodeAt(0).toString(16)).slice(-2);
                }).join(''));
                return JSON.parse(jsonPayload);
            } catch (e) {
                return null;
            }
        }

        function handleGoogleLogin(response) {
            let responsePayload = parseJwt(response.credential);
            if (responsePayload) {
                currentUser = responsePayload.name || responsePayload.email;
                localStorage.setItem('student_current_user', currentUser);
                checkAuth();
            }
        }

        function handleLogout() {
            currentUser = '';
            localStorage.removeItem('student_current_user');
            // Note: userTools in localStorage remain preserved locally for your workflow convenience
            checkAuth();
        }"""

html = html.replace(old_js_auth, new_js_auth)

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html)

print("Google Auth and robust session persistence integrated!")
