import os
import glob
import re

base_dir = "/home/nils/Projekte/cheat-sheets"
html_files = glob.glob(os.path.join(base_dir, "*.html"))

for file_path in html_files:
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()

    # 1. Update Title
    if os.path.basename(file_path) == "index.html":
        content = content.replace("<title>Dev Cheat Sheets — Index</title>", "<title>TheLayer0Guide</title>")
    else:
        # e.g., <title>Bash Cheat Sheet</title> -> <title>Bash - TheLayer0Guide</title>
        content = re.sub(r"<title>(.*?) Cheat Sheet</title>", r"<title>\1 - TheLayer0Guide</title>", content)

    # 2. Update H1
    if os.path.basename(file_path) == "index.html":
        content = content.replace('<span class="h1-accent">Cheat Sheet</span><br>Index', '<span class="h1-accent">TheLayer0</span><br>Guide')
    else:
        # e.g., <br>Cheat Sheet</h1>
        content = content.replace("<br>Cheat Sheet</h1>", "<br>TheLayer0Guide</h1>")

    # 3. Update Footer
    content = content.replace("Dev Cheat Sheet Collection", "TheLayer0Guide")

    with open(file_path, "w", encoding="utf-8") as f:
        f.write(content)

print("Renaming to TheLayer0Guide complete!")
