with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()

# Make sure the welcome modal has pointer-events set correctly and closes on click reliably
old_modal_css = """        /* Welcome Guide Popup Styles */
        .welcome-modal { display: flex; position: fixed; z-index: 200; left: 0; top: 0; width: 100%; height: 100%; background: rgba(0,0,0,0.7); align-items: center; justify-content: center; }"""

new_modal_css = """        /* Welcome Guide Popup Styles */
        .welcome-modal { display: flex; position: fixed; z-index: 9999; left: 0; top: 0; width: 100%; height: 100%; background: rgba(0,0,0,0.7); align-items: center; justify-content: center; pointer-events: auto; }
        .welcome-modal.hidden { display: none; pointer-events: none; }"""

html = html.replace(old_modal_css, new_modal_css)

# Ensure the button calls closeWelcome explicitly and cleanly
old_btn = 'onclick="closeWelcome()"'
new_btn = 'id="diveInBtn" onclick="closeWelcome()"'
html = html.replace(old_btn, new_btn)

# Ensure closeWelcome function completely hides and removes the blocking element
old_close = """        function closeWelcome() {
            const modal = document.getElementById("welcomeModal");
            modal.classList.add("closing");
            setTimeout(() => {
                modal.style.display = "none";
            }, 200);
        }"""

new_close = """        function closeWelcome() {
            const modal = document.getElementById("welcomeModal");
            if(modal) {
                modal.style.display = "none";
                modal.classList.add("hidden");
            }
        }"""

html = html.replace(old_close, new_close)

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html)

print("Modal blocking issue fixed!")
