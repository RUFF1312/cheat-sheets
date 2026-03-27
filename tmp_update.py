import os
import re

base_dir = "/home/nils/Projekte/cheat-sheets"

file_map = {
    "openstack-cheatsheet.html": "openstack.svg",
    "tmux-cheatsheet.html": "tmux.svg",
    "vi-cheatsheet.html": "vim.svg",
    "ansible-cheatsheet.html": "ansible.svg",
    "python-cheatsheet.html": "python.svg",
    "bash-cheatsheet.html": "gnubash.svg",
    "git-cheatsheet.html": "git.svg",
    "powershell-cheatsheet.html": "powershell.svg",
    "proxmox-cheatsheet.html": "proxmox.svg",
}

emoji_map = {
    "☁️": "openstack.svg",
    "🖥": "tmux.svg",
    "📝": "vim.svg",
    "⚙️": "ansible.svg",
    "🐍": "python.svg",
    "🐚": "gnubash.svg",
    "🔀": "git.svg",
    "🔵": "powershell.svg",
    "🖧": "proxmox.svg",
}

# 1. Update index.html
index_path = os.path.join(base_dir, "index.html")
with open(index_path, "r", encoding="utf-8") as f:
    index_content = f.read()

# Replace emojis in index.html with SVG images
for emoji, svg in emoji_map.items():
    index_content = index_content.replace(
        f'<div class="card-icon">{emoji}</div>',
        f'<div class="card-icon"><img src="assets/{svg}" alt="{svg}" style="width:24px;height:24px;"></div>'
    )

# Add generic favicon to index.html (we use gnubash.svg as a fallback or default icon)
if '<link rel="icon"' not in index_content:
    index_content = index_content.replace(
        '</head>',
        '<link rel="icon" type="image/svg+xml" href="assets/gnubash.svg">\n</head>'
    )
with open(index_path, "w", encoding="utf-8") as f:
    f.write(index_content)

# 2. Update all subpages
for html_file, svg_file in file_map.items():
    path = os.path.join(base_dir, html_file)
    if not os.path.exists(path):
        continue
    
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()
    
    changed = False
    
    # Add favicon
    if '<link rel="icon"' not in content:
        content = content.replace(
            '</head>',
            f'<link rel="icon" type="image/svg+xml" href="assets/{svg_file}">\n</head>'
        )
        changed = True
    
    # Add logo to header right before <h1>
    if f'src="assets/{svg_file}"' not in content:
        # Regex to find exactly <h1> and prefix it with the <img> tag
        content, count = re.subn(
            r'(<h1[^>]*>)',
            f'<img src="assets/{svg_file}" alt="Logo" style="width:48px; height:48px; margin-bottom:12px; display:block;">\n\\1',
            content,
            count=1
        )
        if count > 0:
            changed = True
            
    if changed:
        with open(path, "w", encoding="utf-8") as f:
            f.write(content)

print("Update complete!")
