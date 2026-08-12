with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()

# Insert the full student tools directory container right below the login card
directory_html = """
        </div> <!-- End First Card -->

        <!-- Full Student Tools Directory & Submission Card -->
        <div class="card" style="grid-column: 1 / -1;">
            <h2>📚 Curated Tools Directory</h2>
            <input type="text" id="searchInput" placeholder="Search tools or resources..." oninput="filterTools()" style="margin-bottom: 15px;">
            <div id="toolsList" style="display: grid; grid-template-columns: repeat(auto-fill, minmax(280px, 1fr)); gap: 15px; margin-top: 15px;">
                <!-- Dynamically populated tools -->
            </div>
        </div>
"""

# Place it before the right column (Study Assistant)
html = html.replace('<!-- Right Column: AI Assistant Panel -->', directory_html + '\n        <!-- Right Column: AI Assistant Panel -->')

# Add directory script logic before the ending script tag
directory_script = """
        // Full Student Directory Dataset & Logic
        const defaultTools = [
            { title: "Python Documentation", category: "Programming", desc: "Official Python language reference and tutorials.", url: "https://docs.python.org" },
            { title: "Wolfram|Alpha", category: "Math", desc: "Computational knowledge engine for complex equations and calculus.", url: "https://www.wolframalpha.com" },
            { title: "GitHub", category: "Programming", desc: "Host code, manage repositories, and collaborate on projects.", url: "https://github.com" },
            { title: "Notion", category: "Productivity", desc: "All-in-one workspace for notes, tasks, and study planning.", url: "https://www.notion.so" }
        ];

        let userTools = JSON.parse(localStorage.getItem('student_user_tools') || '[]');

        function filterTools() {
            let query = document.getElementById('searchInput').value.toLowerCase();
            let allTools = [...defaultTools, ...userTools];
            let container = document.getElementById('toolsList');
            if(!container) return;

            container.innerHTML = '';
            let filtered = allTools.filter(t => t.title.toLowerCase().includes(query) || t.desc.toLowerCase().includes(query) || t.category.toLowerCase().includes(query));

            if(filtered.length === 0) {
                container.innerHTML = '<p style="color: var(--meta); grid-column: 1/-1;">No matching tools found.</p>';
                return;
            }

            filtered.forEach(tool => {
                container.innerHTML += `
                    <div style="background: #0f172a; border: 1px solid var(--border); border-radius: 8px; padding: 15px; display: flex; flex-direction: column; justify-content: space-between;">
                        <div>
                            <span style="font-size: 0.75rem; background: var(--primary); padding: 2px 8px; border-radius: 4px; font-weight: bold;">${tool.category}</span>
                            <h3 style="margin: 10px 0 5px 0; font-size: 1.1rem;">${tool.title}</h3>
                            <p style="font-size: 0.85rem; color: var(--meta); margin: 0 0 15px 0;">${tool.desc}</p>
                        </div>
                        <a href="${tool.url}" target="_blank" style="background: var(--border); color: var(--text); text-align: center; padding: 8px; border-radius: 6px; text-decoration: none; font-size: 0.9rem; font-weight: bold;">Open Resource →</a>
                    </div>
                `;
            });
        }

        // Run filter on load
        filterTools();
"""

html = html.replace('updateUI();', 'updateUI();\n        filterTools();')
html = html.replace('// Initialize view on load', directory_script + '\n        // Initialize view on load')

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html)

print("Full directory restored successfully!")
