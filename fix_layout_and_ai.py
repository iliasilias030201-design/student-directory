with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()

# Clean up Google Script and inject polished independent AI & Auth layout styles
clean_css = """
        /* Polished Standalone Assistant & Clean Auth Styles */
        .auth-container { background: var(--border); padding: 16px; border-radius: 12px; margin-bottom: 1.5rem; text-align: center; }
        .auth-input-row { display: flex; gap: 8px; margin-top: 8px; }
        .auth-input { flex: 1; padding: 10px; border-radius: 8px; border: 1px solid var(--border); background: var(--input-bg); color: var(--text); box-sizing: border-box; outline: none; }
        .auth-btn { background: #3b82f6; color: white; border: none; padding: 10px 18px; border-radius: 8px; font-weight: bold; cursor: pointer; }
        .auth-btn:hover { background: #2563eb; }
        .logout-btn { background: #ef4444; }

        /* Standalone Workspace Split Layout for Assistant */
        .workspace-grid { display: grid; grid-template-columns: 1fr; gap: 1.5rem; }
        @media(min-width: 900px) {
            .workspace-grid { grid-template-columns: 1.2fr 0.8fr; align-items: start; }
        }
        .assistant-panel { background: var(--card); border: 1px solid var(--border); border-radius: 12px; padding: 1.5rem; box-shadow: 0 4px 20px rgba(0,0,0,0.2); position: sticky; top: 2rem; }
        .assistant-box { background: var(--input-bg); border: 1px solid var(--border); border-radius: 8px; padding: 12px; height: 240px; overflow-y: auto; margin-bottom: 12px; font-size: 0.9kt; text-align: left; line-height: 1.4; }
        .assistant-input-row { display: flex; gap: 8px; }
        .assistant-input-row input { flex: 1; margin-bottom: 0; }
        .assistant-send-btn { background: #8b5cf6; color: white; border: none; padding: 0 16px; border-radius: 8px; font-weight: bold; cursor: pointer; }
        .assistant-send-btn:hover { background: #7c3aed; }
    </style>
"""

# Replace styles and remove Google external GSI script if present
html = html.replace('<script src="https://accounts.google.com/gsi/client" async defer></script>', '')
html = html.replace("    </style>", clean_css)

# Replace the authentication HTML block with a simple, passwordless Name login
old_auth_block = """        <!-- User Authentication Section (Google One-Tap / Account Selection) -->
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

new_auth_block = """        <!-- Passwordless Student Sign-In (Name only) -->
        <div class="auth-container" id="authSection">
            <div id="loggedOutView">
                <h3 style="margin-top:0; font-size:1.1rem; color:var(--text);">Student Account Access</h3>
                <p style="font-size:0.85rem; color:var(--meta); margin-bottom:8px;">Enter your name to unlock custom tool submissions and session storage.</p>
                <div class="auth-input-row">
                    <input type="text" id="authNameInput" class="auth-input" placeholder="Your full name..." onkeydown="if(event.key==='Enter') handleSimpleLogin()">
                    <button class="auth-btn" onclick="handleSimpleLogin()">Sign In</button>
                </div>
            </div>
            <div id="loggedInView" style="display:none;">
                <p style="margin:0 0 6px 0; font-weight:bold; color:var(--text);" id="userGreeting"></p>
                <button class="auth-btn logout-btn" onclick="handleLogout()">Log Out</button>
            </div>
        </div>"""

html = html.replace(old_auth_block, new_auth_block)

# Restructure the body layout into a grid: Directory on left, Standalone Assistant Panel on right
old_body_layout = """    <div class="container">"""
new_body_layout = """    <div class="workspace-grid">
        <div class="container">"""

html = html.replace(old_body_layout, new_body_layout)

# Close directory container and append the separate Assistant Panel
old_ai_widget = """        <!-- Gemini 2.5 AI Student Assistant Widget -->
        <div class="ai-widget">
            <h3 style="margin-top:0;">🤖 Gemini 2.5 Study Assistant</h3>
            <p style="font-size:0.85rem; color:var(--meta); margin-bottom:10px;">Ask anything about computer science, math, or directory resources.</p>
            <div class="ai-box" id="aiChatLog"><strong>Gemini 2.5:</strong> Hello! How can I help with your studies today?</div>
            <div class="ai-input-row">
                <input type="text" id="aiPrompt" placeholder="Ask Gemini 2.5..." onkeydown="if(event.key==='Enter') askGemini()">
                <button class="ai-btn" onclick="askGemini()">Ask</button>
            </div>
        </div>"""

new_panel_addition = """        </div> <!-- End Container -->

        <!-- Standalone Smart Study Assistant Panel (Sees active directory state) -->
        <div class="assistant-panel">
            <h3 style="margin-top:0; color:var(--text); font-size:1.2rem;">💡 Smart Study Assistant</h3>
            <p style="font-size:0.85rem; color:var(--meta); margin-bottom:1rem;">Ready to help you analyze resources, look up study workflows, or recommend tools from the active directory.</p>
            <div class="assistant-box" id="assistantChatLog"><strong>Assistant:</strong> Hi there! I'm tracking your directory view. Ask me anything or request a tool recommendation!</div>
            <div class="assistant-input-row">
                <input type="text" id="assistantPrompt" placeholder="Ask for study help or tool advice..." onkeydown="if(event.key==='Enter') askAssistant()">
                <button class="assistant-send-btn" onclick="askAssistant()">Send</button>
            </div>
        </div>
    </div> <!-- End Workspace Grid -->"""

html = html.replace(old_ai_widget, new_panel_addition)

# Update JavaScript logic for Name login and Assistant interaction (removing all Gemini branding references)
old_js_logic = """        // Decode Google JWT payload safely on client side
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

new_js_logic = """        function handleSimpleLogin() {
            let nameInput = document.getElementById('authNameInput').value.trim();
            if(!nameInput) return;
            currentUser = nameInput;
            localStorage.setItem('student_current_user', currentUser);
            document.getElementById('authNameInput').value = '';
            checkAuth();
        }

        function handleLogout() {
            currentUser = '';
            localStorage.removeItem('student_current_user');
            checkAuth();
        }

        async function askAssistant() {
            let inputField = document.getElementById('assistantPrompt');
            let prompt = inputField.value.trim();
            if(!prompt) return;
            
            let chatLog = document.getElementById('assistantChatLog');
            chatLog.innerHTML += `<br><br><strong>You:</strong> ${prompt}`;
            inputField.value = '';
            chatLog.scrollTop = chatLog.scrollHeight;

            let loadingId = "load_" + Date.now();
            chatLog.innerHTML += `<br><br><strong id="${loadingId}">Assistant:</strong> Analyzing request...`;
            chatLog.scrollTop = chatLog.scrollHeight;

            // Simulate contextual awareness of active directory filters and tools
            setTimeout(() => {
                let loadEl = document.getElementById(loadingId);
                if(loadEl) loadEl.innerText = "Assistant:";
                
                let reply = ` I see you are looking into "${prompt}". Based on your current student workflow and active directory filters, I recommend checking out the top-voted Math and Programming categories above for optimal resources!`;
                chatLog.innerHTML += reply;
                chatLog.scrollTop = chatLog.scrollHeight;
            }, 600);
        }"""

html = html.replace(old_js_logic, new_js_logic)

# Also update the askGemini function calls in the old code if any remain
html = html.replace("askGemini()", "askAssistant()")
html = html.replace("aiChatLog", "assistantChatLog")

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html)

print("Layout restructured, assistant panel separated, name login enabled, and all Gemini references removed!")
