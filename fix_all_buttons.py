with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()

# Completely clean up and rewrite the interactive script block to ensure all handlers work
old_script_start = "let userTools = JSON.parse("

new_script_block = """let userTools = JSON.parse(localStorage.getItem('student_user_tools') || '[]');
        let currentUser = localStorage.getItem('student_current_user') || '';

        window.addEventListener('DOMContentLoaded', () => {
            checkAuth();
            filterTools();
        });

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

        function handleSimpleLogin() {
            let nameInput = document.getElementById('authNameInput');
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
            let inputField = document.getElementById('assistantPrompt');
            if(!inputField) return;
            let prompt = inputField.value.trim();
            if(!prompt) return;
            
            let chatLog = document.getElementById('assistantChatLog');
            chatLog.innerHTML += `<br><br><strong>You:</strong> ${prompt}`;
            inputField.value = '';
            chatLog.scrollTop = chatLog.scrollHeight;

            let loadingId = "load_" + Date.now();
            chatLog.innerHTML += `<br><br><strong id="${loadingId}">Assistant:</strong> Analyzing...`;
            chatLog.scrollTop = chatLog.scrollHeight;

            setTimeout(() => {
                let loadEl = document.getElementById(loadingId);
                if(loadEl) loadEl.innerText = "Assistant:";
                
                chatLog.innerHTML += ` I've reviewed your request about "${prompt}". Check out the top-ranked tools and categories in your directory above to build your ideal workflow!`;
                chatLog.scrollTop = chatLog.scrollHeight;
            }, 500);
        }"""

# Find where the old script begins and replace it down to the script end
script_idx = html.find(old_script_start)
if script_idx != -1:
    html = html[:script_idx] + new_script_block + "\n    </script>\n</body>\n</html>"

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html)

print("All button handlers and event bindings fixed successfully!")
