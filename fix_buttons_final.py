with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()

# Clean up any broken script blocks and append a fully robust script implementation
script_start_marker = "let userTools = JSON.parse("
idx = html.find(script_start_marker)

new_robust_script = """let userTools = JSON.parse(localStorage.getItem('student_user_tools') || '[]');
        let currentUser = localStorage.getItem('student_current_user') || '';

        document.addEventListener('DOMContentLoaded', () => {
            checkAuth();
            if(typeof filterTools === 'function') filterTools();

            // Bind authentication buttons safely
            const loginBtn = document.getElementById('loginBtn');
            if(loginBtn) loginBtn.addEventListener('click', handleSimpleLogin);

            const authInput = document.getElementById('authNameInput');
            if(authInput) {
                authInput.addEventListener('keypress', (e) => {
                    if(e.key === 'Enter') handleSimpleLogin();
                });
            }

            const logoutBtn = document.getElementById('logoutBtn');
            if(logoutBtn) logoutBtn.addEventListener('click', handleLogout);

            // Bind assistant send button
            const sendBtn = document.getElementById('assistantSendBtn');
            if(sendBtn) sendBtn.addEventListener('click', askAssistant);

            const assistantInput = document.getElementById('assistantPrompt');
            if(assistantInput) {
                assistantInput.addEventListener('keypress', (e) => {
                    if(e.key === 'Enter') askAssistant();
                });
            }
        });

        function checkAuth() {
            const loggedOut = document.getElementById('loggedOutView');
            const loggedIn = document.getElementById('loggedInView');
            const greeting = document.getElementById('userGreeting');
            const submitSec = document.getElementById('submitSection');

            if (currentUser) {
                if(loggedOut) loggedOut.style.display = 'none';
                if(loggedIn) loggedIn.style.display = 'block';
                if(greeting) greeting.innerText = 'Welcome back, ' + currentUser + '! 👋';
                if(submitSec) submitSec.style.display = 'block';
            } else {
                if(loggedOut) loggedOut.style.display = 'block';
                if(loggedIn) loggedIn.style.display = 'none';
                if(submitSec) submitSec.style.display = 'none';
            }
        }

        function handleSimpleLogin() {
            const nameInput = document.getElementById('authNameInput');
            if(!nameInput) return;
            let uname = nameInput.value.trim();
            if(!uname) return;
            currentUser = uname;
            localStorage.setItem('student_current_user', currentUser);
            nameInput.value = '';
            checkAuth();
        }

        function handleLogout() {
            currentUser = '';
            localStorage.removeItem('student_current_user');
            checkAuth();
        }

        function askAssistant() {
            const inputField = document.getElementById('assistantPrompt');
            if(!inputField) return;
            let prompt = inputField.value.trim();
            if(!prompt) return;
            
            const chatLog = document.getElementById('assistantChatLog');
            if(!chatLog) return;

            chatLog.innerHTML += `<br><br><strong>You:</strong> ${prompt}`;
            inputField.value = '';
            chatLog.scrollTop = chatLog.scrollHeight;

            let loadingId = "load_" + Date.now();
            chatLog.innerHTML += `<br><br><strong id="${loadingId}">Assistant:</strong> Analyzing request...`;
            chatLog.scrollTop = chatLog.scrollHeight;

            setTimeout(() => {
                let loadEl = document.getElementById(loadingId);
                if(loadEl) loadEl.innerText = "Assistant:";
                
                chatLog.innerHTML += ` I've reviewed your note on "${prompt}". Look through the active categories above to find the optimal resources for your study workflow!`;
                chatLog.scrollTop = chatLog.scrollHeight;
            }, 400);
        }"""

# Also ensure the HTML input and button IDs match our robust script listeners
old_auth_html = """                <div class="auth-input-row">
                    <input type="text" id="authNameInput" class="auth-input" placeholder="Your full name..." onkeydown="if(event.key==='Enter') handleSimpleLogin()">
                    <button class="auth-btn" onclick="handleSimpleLogin()">Sign In</button>
                </div>"""

new_auth_html = """                <div class="auth-input-row">
                    <input type="text" id="authNameInput" class="auth-input" placeholder="Your full name...">
                    <button class="auth-btn" id="loginBtn">Sign In</button>
                </div>"""

old_logout_html = """<button class="auth-btn logout-btn" onclick="handleLogout()">Log Out</button>"""
new_logout_html = """<button class="auth-btn logout-btn" id="logoutBtn">Log Out</button>"""

old_assistant_html = """            <div class="assistant-input-row">
                <input type="text" id="assistantPrompt" placeholder="Ask for study help or tool advice..." onkeydown="if(event.key==='Enter') askAssistant()">
                <button class="assistant-send-btn" onclick="askAssistant()">Send</button>
            </div>"""

new_assistant_html = """            <div class="assistant-input-row">
                <input type="text" id="assistantPrompt" placeholder="Ask for study help or tool advice...">
                <button class="assistant-send-btn" id="assistantSendBtn">Send</button>
            </div>"""

html = html.replace(old_auth_html, new_auth_html)
html = html.replace(old_logout_html, new_logout_html)
html = html.replace(old_assistant_html, new_assistant_html)

if idx != -1:
    html = html[:idx] + new_robust_script + "\n    </script>\n</body>\n</html>"

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html)

print("Buttons completely re-wired and fixed!")
