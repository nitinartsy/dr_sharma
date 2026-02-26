import re
import os

files_to_update = [
    'about-us.html',
    'contactus.html',
    'services.html',
    'gallery.html',
    'blog.html',
    'service-kidney-cancer.html',
    'service-bladder-cancer.html',
    'service-testicular-cancer.html',
    'service-prostate-cancer.html',
    'service-penile-cancer.html'
]

# Read index.html to extract the new header and footer
with open('index.html', 'r', encoding='utf-8') as f:
    index_content = f.read()

# Extract header
header_match = re.search(r'(<header class="site-header">.*?</header>)', index_content, re.DOTALL)
new_header = header_match.group(1) if header_match else None

# Extract footer
footer_match = re.search(r'(<footer class="site-footer.*?</footer>)', index_content, re.DOTALL)
new_footer = footer_match.group(1) if footer_match else None

if not new_header or not new_footer:
    print("Could not extract new header or footer from index.html")
    exit(1)

for filename in files_to_update:
    if not os.path.exists(filename):
        print(f"File {filename} not found. Skipping.")
        continue
        
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Replace header: look for old header tag and its contents
    content = re.sub(r'<header[^>]*>.*?</header>', new_header, content, flags=re.DOTALL)
    
    # Replace footer
    content = re.sub(r'<footer[^>]*>.*?</footer>', new_footer, content, flags=re.DOTALL)
    
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"Updated {filename}")

print("Done updating components.")
