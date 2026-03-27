import os
import glob

base_dir = "/home/nils/Projekte/cheat-sheets"
html_files = glob.glob(os.path.join(base_dir, "*.html"))

old_zero = '<span style="color: #a371f7;">0</span>'
# Add JetBrains Mono for the slashed/dotted zero, increase size, and override gradient text-fill
new_zero = '<span style="color: #a371f7; font-family: \'JetBrains Mono\', monospace; font-size: 1.25em; -webkit-text-fill-color: #a371f7;">0</span>'

for file_path in html_files:
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()

    # Perform exactly the replacement of the spanned 0
    content = content.replace(old_zero, new_zero)

    with open(file_path, "w", encoding="utf-8") as f:
        f.write(content)

print("Font fixes applied successfully!")
