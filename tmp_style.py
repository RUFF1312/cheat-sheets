import os
import glob
import re

base_dir = "/home/nils/Projekte/cheat-sheets"
html_files = glob.glob(os.path.join(base_dir, "*.html"))

violet_zero = '<span style="color: #a371f7;">0</span>'

for file_path in html_files:
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()

    # 1. Update index.html H1
    if os.path.basename(file_path) == "index.html":
        content = content.replace(
            '<span class="h1-accent">TheLayer0</span>',
            f'<span class="h1-accent">TheLayer{violet_zero}</span>'
        )
    else:
        # Update subpages H1
        content = content.replace(
            "<br>TheLayer0Guide</h1>",
            f"<br>TheLayer{violet_zero}Guide</h1>"
        )

    # 2. Update Footer
    content = content.replace(
        "TheLayer0Guide",
        f"TheLayer{violet_zero}Guide"
    )

    # Note: We accidentally also replaced <title>, which is invalid HTML
    # Let's fix <title> by removing any span inside it
    content = re.sub(
        r"<title>(.*?)TheLayer<span[^>]*>0</span>Guide(.*?)</title>",
        r"<title>\1TheLayer0Guide\2</title>",
        content
    )

    with open(file_path, "w", encoding="utf-8") as f:
        f.write(content)

print("Violet 0 stylings successfully applied!")
