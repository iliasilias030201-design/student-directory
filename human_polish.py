with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()

# Add smooth fade-out CSS and live counter style
polish_css = """
        /* Human-crafted Polish Additions */
        @keyframes fadeInScale {
            from { opacity: 0; transform: scale(0.95); }
            to { opacity: 1; transform: scale(1); }
        }
        @keyframes fadeOutScale {
            from { opacity: 1; transform: scale(1); }
            to { opacity: 0; transform: scale(0.95); }
        }
        .welcome-content { animation: fadeInScale 0.3s cubic-bezier(0.16, 1, 0.3, 1) forwards; }
        .welcome-modal.closing .welcome-content { animation: fadeOutScale 0.2s ease-in forwards; }
        .live-badge { display: inline-flex; align-items: center; gap: 6px; background: rgba(34, 197, 94, 0.1); color: #22c55e; padding: 4px 10px; border-radius: 20px; font-size: 0.75rem; font-weight: 600; border: 1px solid rgba(34, 197, 94, 0.2); margin-bottom: 1rem; }
        .live-dot { width: 6px; height: 6px; background: #22c55e; border-radius: 50%; box-shadow: 0 0 8px #22c55e; animation: pulse 2s infinite; }
        @keyframes pulse { 0% { opacity: 1; } 50% { opacity: 0.4; } 100% { opacity: 1; } }
    </style>
"""

html = html.replace("    </style>", polish_css)

# Update welcome modal HTML to include random rotating text & live badge
old_welcome = """    <div id="welcomeModal" class="welcome-modal">
        <div class="welcome-content">
            <h2>Welcome to Student Directory! 🚀</h2>
            <p>Explore 500+ student tools with typo-tolerant search, filter by categories, upvote your favorite resources, toggle dark/light mode, and submit new tools on the fly!</p>
            <button class="welcome-btn" onclick="closeWelcome()">Got it, Let's Go!</button>
        </div>
    </div>"""

new_welcome = """    <div id="welcomeModal" class="welcome-modal">
        <div class="welcome-content">
            <div class="live-badge"><span class="live-dot"></span> Live Student Hub</div>
            <h2 id="welcomeTitle">Hey there! 👋</h2>
            <p id="welcomeDesc">Welcome to your ultimate curated directory. Search through 500+ top-tier tools, drop upvotes on your daily drivers, or submit a missing resource instantly.</p>
            <button class="welcome-btn" onclick="closeWelcome()">Dive In &rarr;</button>
        </div>
    </div>"""

html = html.replace(old_welcome, new_welcome)

# Update closeWelcome to include smooth exit animation and dynamic rotating subtitles
old_js = """        function closeWelcome() {
            document.getElementById("welcomeModal").style.display = "none";
        }"""

new_js = """        // Rotating human-like intro text pool
        const intros = [
            { title: "Hey there! 👋", desc: "Welcome to your ultimate curated directory. Search through 500+ top-tier tools, drop upvotes on your daily drivers, or submit a missing resource instantly." },
            { title: "Looking for a study stack? ⚡", desc: "You're in the right place. Fast typo-tolerant search, clean dark/light mode, and community-ranked utilities built by students, for students." },
            { title: "Quick heads-up! 💡", desc: "Every tool here is indexed for instant access. Hit upvote on the ones you use daily or add your own custom workflow apps directly below." }
        ];
        
        // Pick a random intro on load
        window.addEventListener('DOMContentLoaded', () => {
            const randomIntro = intros[Math.floor(Math.random() * intros.length)];
            document.getElementById("welcomeTitle").innerText = randomIntro.title;
            document.getElementById("welcomeDesc").innerText = randomIntro.desc;
        });

        function closeWelcome() {
            const modal = document.getElementById("welcomeModal");
            modal.classList.add("closing");
            setTimeout(() => {
                modal.style.display = "none";
            }, 200);
        }"""

html = html.replace(old_js, new_js)

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html)

print("Human-crafted polish applied successfully!")
