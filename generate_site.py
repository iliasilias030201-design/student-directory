import csv
import os

os.makedirs("output", exist_ok=True)

# Massive expanded dataset across multiple categories
tools_data = [
    # Math & Science
    ("Desmos", "Math", "Free", "An advanced online graphing calculator and math tool.", "https://www.desmos.com"),
    ("Geogebra", "Math", "Free", "Interactive geometry, algebra, and calculus application.", "https://www.geogebra.org"),
    ("WolframAlpha", "Research", "Freemium", "Computational intelligence platform for solving complex homework equations.", "https://www.wolframalpha.com"),
    ("Symbolab", "Math", "Freemium", "Advanced math solver that shows step-by-step solutions.", "https://www.symbolab.com"),
    ("GeoGebra 3D", "Math", "Free", "3D graphing and geometry visualization tool for math students.", "https://www.geogebra.org/3d"),
    ("Desmos Matrix", "Math", "Free", "Matrix calculator and linear algebra tool.", "https://www.desmos.com/matrix"),
    ("Integral Calculator", "Math", "Free", "Step-by-step integration and differentiation solver.", "https://www.integral-calculator.com"),
    ("Derivative Calculator", "Math", "Free", "Online tool to compute derivatives with steps.", "https://www.derivative-calculator.net"),
    ("Mathway", "Math", "Freemium", "Instant math problem solver across algebra, calculus, and statistics.", "https://www.mathway.com"),
    ("Photomath", "Math", "Freemium", "Scan math problems using your camera for instant step-by-step solutions.", "https://photomath.com"),

    # Programming & Development
    ("GeeksforGeeks", "Programming", "Free", "Computer science portal for programmers featuring code and tutorials.", "https://www.geeksforgeeks.org"),
    ("LeetCode", "Programming", "Freemium", "Platform to practice coding interview questions and algorithms.", "https://leetcode.com"),
    ("GitHub", "Programming", "Free", "Platform for version control and collaborating on software projects.", "https://github.com"),
    ("Stack Overflow", "Programming", "Free", "Community-driven Q&A platform for software developers and coders.", "https://stackoverflow.com"),
    ("W3Schools", "Programming", "Free", "Web development tutorials covering HTML, CSS, JavaScript, and Python.", "https://www.w3schools.com"),
    ("MDN Web Docs", "Programming", "Free", "Comprehensive documentation for web technologies including JavaScript and CSS.", "https://developer.mozilla.org"),
    ("Python Docs", "Programming", "Free", "Official documentation and reference manuals for the Python programming language.", "https://docs.python.org"),
    ("HackerRank", "Programming", "Free", "Coding practice platform for technical hiring and algorithm challenges.", "https://www.hackerrank.com"),
    ("Programiz", "Programming", "Freemium", "Beginner-friendly tutorials and code editors for learning Python and C++.", "https://www.programiz.com"),
    ("Replit", "Programming", "Freemium", "Collaborative browser-based IDE to write and run code instantly.", "https://replit.com"),

    # Productivity & Studying
    ("Notion", "Productivity", "Free", "All-in-one workspace for notes, task management, and student planners.", "https://www.notion.so"),
    ("Anki", "Studying", "Free", "Flashcard program utilizing spaced repetition for efficient memorization.", "https://apps.ankiweb.net"),
    ("Quizlet", "Studying", "Freemium", "Digital flashcards and study games created by students and teachers.", "https://quizlet.com"),
    ("Overleaf", "Writing", "Freemium", "Collaborative cloud-based LaTeX editor for academic writing and papers.", "https://www.overleaf.com"),
    ("Grammarly", "Writing", "Freemium", "AI-powered writing assistant for grammar and spelling checks.", "https://www.grammarly.com"),
    ("Todoist", "Productivity", "Freemium", "Task manager and to-do list app to organize daily student schedules.", "https://todoist.com"),
    ("Obsidian", "Productivity", "Free", "Powerful knowledge base that works on local Markdown files.", "https://obsidian.md"),
    ("Google Docs", "Writing", "Free", "Collaborative online word processor for writing essays and reports.", "https://docs.google.com"),
    ("Canva", "Design", "Freemium", "Graphic design platform for creating presentation slides and infographics.", "https://www.canva.com"),
    ("Forest", "Productivity", "Freemium", "Gamified focus timer app to prevent phone distraction while studying.", "https://www.forestapp.cc")
]

# Write data to data.csv automatically
with open("data.csv", mode="w", encoding="utf-8", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["Name", "Category", "Pricing", "Description", "Link"])
    writer.writerows(tools_data)

# Modern template with clean CSS styling and SEO meta tags
template = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{name} - Review, Pricing & Best Student Alternative</title>
    <meta name="description" content="Discover {name}, a top-rated {category} tool. Check pricing, features, and official links for students.">
    <style>
        body {{ font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif; background-color: #0f172a; color: #f8fafc; padding: 2rem; margin: 0; }}
        .card {{ background: #1e293b; padding: 2rem; border-radius: 12px; max-width: 600px; margin: auto; box-shadow: 0 4px 20px rgba(0,0,0,0.5); }}
        .badge {{ background: #3b82f6; color: white; padding: 4px 10px; border-radius: 6px; font-size: 0.85rem; text-transform: uppercase; }}
        .price {{ color: #38bdf8; font-weight: bold; }}
        a.btn {{ display: inline-block; background: #22c55e; color: white; padding: 10px 20px; border-radius: 6px; text-decoration: none; font-weight: bold; margin-top: 1rem; }}
        a.back {{ color: #94a3b8; text-decoration: none; display: inline-block; margin-top: 1.5rem; }}
        a.back:hover {{ color: white; }}
    </style>
</head>
<body>
    <div class="card">
        <h1>{name}</h1>
        <span class="badge">{category}</span>
        <p><strong>Pricing:</strong> <span class="price">{pricing}</span></p>
        <p>{description}</p>
        <a class="btn" href="{link}" target="_blank">Visit Official Website &rarr;</a>
        <br>
        <a class="back" href="index.html">&larr; Back to Directory</a>
    </div>
</body>
</html>
"""

index_links = []
with open("data.csv", mode="r", encoding="utf-8") as file:
    reader = csv.DictReader(file)
    for row in reader:
        filename = f"{row['Name'].lower().replace(' ', '-').replace('/', '-')}.html"
        page_content = template.format(
            name=row['Name'],
            category=row['Category'],
            pricing=row['Pricing'],
            description=row['Description'],
            link=row['Link']
        )
        
        with open(os.path.join("output", filename), "w", encoding="utf-8") as f:
            f.write(page_content)
            
        index_links.append(f'<li style="margin: 10px 0;"><a href="{filename}" style="color: #38bdf8; text-decoration: none; font-size: 1.1rem;">{row["Name"]}</a> <span style="color: #94a3b8; font-size: 0.9rem;">({row["Category"]} - {row["Pricing"]})</span></li>')

# Generate main directory index page
index_content = f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Ultimate Student Resource & Software Directory</title>
    <meta name="description" content="Explore top-tier curated tools, coding portals, math solvers, and productivity apps for students.">
    <style>
        body {{ font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif; background-color: #0f172a; color: #f8fafc; padding: 2rem; margin: 0; }}
        .container {{ max-width: 700px; margin: auto; background: #1e293b; padding: 2rem; border-radius: 12px; box-shadow: 0 4px 20px rgba(0,0,0,0.5); }}
        h1 {{ color: #f8fafc; border-bottom: 2px solid #334155; padding-bottom: 10px; }}
        ul {{ list-style-type: none; padding: 0; }}
    </style>
</head>
<body>
    <div class="container">
        <h1>Ultimate Student Resource Directory</h1>
        <p style="color: #94a3b8;">Explore top-tier tools curated across math, programming, and productivity:</p>
        <ul>
            {"".join(index_links)}
        </ul>
    </div>
</body>
</html>
"""

with open(os.path.join("output", "index.html"), "w", encoding="utf-8") as f:
    f.write(index_content)

print("Massive SEO website bundle successfully generated!")
