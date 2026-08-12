with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()

# Completely remove the welcome modal HTML block so it can never block anything
import re
html = re.sub(r'<div class="welcome-modal"[^>]*>.*?</div>\s*</div>\s*</div>', '', html, flags=re.DOTALL)
html = re.sub(r'<div id="welcomeModal"[^>]*>.*?</div>', '', html, flags=re.DOTALL)

# Clean up CSS for any pointer-event traps
pointer_fix = """
    * { pointer-events: auto !important; }
    body { pointer-events: auto !important; overflow-y: auto !important; }
    .container, .workspace-grid, .assistant-panel, button, input { pointer-events: auto !important; position: relative; z-index: 10; }
</style>
"""
html = html.replace("</style>", pointer_fix)

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html)

print("Completely stripped blocking elements and forced pointer events active!")
