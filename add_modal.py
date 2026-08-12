with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()

modal_css = """
        /* Welcome Guide Popup Styles */
        .welcome-modal { display: flex; position: fixed; z-index: 200; left: 0; top: 0; width: 100%; height: 100%; background: rgba(0,0,0,0.7); align-items: center; justify-content: center; }
        .welcome-content { background: var(--card); padding: 2.5rem; border-radius: 16px; max-width: 450px; width: 90%; border: 1px solid var(--border); text-align: center; box-shadow: 0 10px 30px rgba(0,0,0,0.4); }
        .welcome-content h2 { margin-top: 0; color: var(--text); }
        .welcome-content p { color: var(--meta); line-height: 1.5; margin-bottom: 1.5rem; }
        .welcome-btn { background: #3b82f6; color: white; border: none; padding: 12px 24px; border-radius: 8px; font-weight: bold; font-size: 1rem; cursor: pointer; width: 100%; }
        .welcome-btn:hover { background: #2563eb; }
    </style>
"""

html = html.replace("    </style>", modal_css)

welcome_html = """
<body>
    <!-- Welcome Guidance Popup -->
    <div id="welcomeModal" class="welcome-modal">
        <div class="welcome-content">
            <h2>Welcome to Student Directory! 🚀</h2>
            <p>Explore 500+ student tools with typo-tolerant search, filter by categories, upvote your favorite resources, toggle dark/light mode, and submit new tools on the fly!</p>
            <button class="welcome-btn" onclick="closeWelcome()">Got it, Let's Go!</button>
        </div>
    </div>
"""

html = html.replace("<body>", welcome_html)

js_code = """
        function closeWelcome() {
            document.getElementById("welcomeModal").style.display = "none";
        }
"""

html = html.replace("<script>", "<script>\n" + js_code)

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html)

print("Successfully patched index.html with the welcome modal!")
