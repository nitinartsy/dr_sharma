import re
import os

blog_file = "/Users/shivangigautam/Desktop/doctor-personal 2/blog.html"
content_file = "/tmp/all_content.txt"

with open(content_file, 'r', encoding='utf-8') as f:
    text = f.read()

# Extract sections based on the Headers
def get_section(start_marker, end_marker=None):
    start = text.find(start_marker)
    if start == -1: return ""
    start = text.find("\n", start) + 1 # skip header line
    if end_marker:
        end = text.find(end_marker, start)
        return text[start:end].strip()
    return text[start:].strip()

rarc_text = get_section("===== /Users/shivangigautam/Downloads/OneDrive_1_24-02-2026/Blogs/RARC Description.docx =====", "===== /Users/shivangigautam/Downloads/OneDrive_1_24-02-2026/Blogs/Medanta blogs")
medanta_text = get_section("===== /Users/shivangigautam/Downloads/OneDrive_1_24-02-2026/Blogs/Medanta blogs with link.docx =====", "===== /Users/shivangigautam/Downloads/OneDrive_1_24-02-2026/Blogs/RPLND.docx =====")
rplnd_text = get_section("===== /Users/shivangigautam/Downloads/OneDrive_1_24-02-2026/Blogs/RPLND.docx =====", "===== /Users/shivangigautam/Downloads/OneDrive_1_24-02-2026/Blogs/RAPN Blog.docx =====")
rapn_text = get_section("===== /Users/shivangigautam/Downloads/OneDrive_1_24-02-2026/Blogs/RAPN Blog.docx =====", "===== /Users/shivangigautam/Downloads/OneDrive_1_24-02-2026/Blogs/RARP description.docx =====")
rarp_text = get_section("===== /Users/shivangigautam/Downloads/OneDrive_1_24-02-2026/Blogs/RARP description.docx =====", "===== /Users/shivangigautam/Downloads/OneDrive_1_24-02-2026/Blogs/RRN.docx =====")
rrn_text = get_section("===== /Users/shivangigautam/Downloads/OneDrive_1_24-02-2026/Blogs/RRN.docx =====", "===== /Users/shivangigautam/Downloads/OneDrive_1_24-02-2026/Contact/Contact.docx =====")

def format_html(title, category, raw_text, is_links=False):
    html = f"""
                                    <div class="post_header entry-header">
                                        <div class="post_category">
                                            <div class="post_meta"><span class="post_meta_item post_categories cat_sep"><a href="#" rel="category tag">{category}</a></span></div>
                                        </div>
                                        <h3 class="post_title entry-title"><a href="#" rel="bookmark">{title}</a></h3>
                                    </div>
                                    <div class="post_meta"><span class="post_meta_item post_date"><a href="#">Dec 25, 2025</a></span></div>
                                    <div class="post_content entry-content">
                                        <div class="post_content_inner">
"""
    if is_links:
        html += "<ul>\n"
        for line in raw_text.split('\n'):
            line = line.strip()
            if line.startswith('http'):
                html += f'<li><a href="{line}" target="_blank">{line}</a></li>\n'
        html += "</ul>\n"
    else:
        for line in raw_text.split('\n'):
            line = line.strip()
            if not line: continue
            if '•\t' in line or '- ' in line:
                line = line.replace('•\t', '').replace('- ', '').strip()
                html += f"<ul><li>{line}</li></ul>\n"
            elif any(line.startswith(x) for x in ['Part ', 'Step ', '1.', '2.', '3.', 'A.', 'B.', 'Early Complications', 'Late Complications']):
                html += f"<h4>{line}</h4>\n"
            else:
                html += f"<p>{line}</p>\n"
        
        # fix adjacent uls
        html = html.replace('</ul>\n<ul>', '\n')

    html += """                                        </div>
                                    </div>"""
    return html

posts = [
    ("Robotic Radical Cystectomy with Ileal Conduit", "Bladder Cancer", rarc_text, False),
    ("Patient Guide: Robotic Retroperitoneal Lymph Node Dissection", "Testicular Cancer", rplnd_text, False),
    ("Patient Guide: Robotic Partial Nephrectomy", "Kidney Cancer", rapn_text, False),
    ("Patient Guide: Robotic Radical Prostatectomy", "Prostate Cancer", rarp_text, False),
    ("Robotic Radical Nephrectomy", "Kidney Cancer", rrn_text, False),
    ("Medanta Patient Education Blogs", "Education", medanta_text, True),
]

with open(blog_file, 'r', encoding='utf-8') as f:
    blog_html = f.read()

# Replace articles
# blog_html has <article id="post-970" ... > ... </article>
for i, post_id in enumerate(["post-970", "post-969", "post-968", "post-967", "post-966", "post-965"]):
    if i >= len(posts): break
    title, category, raw_text, is_links = posts[i]
    new_content = format_html(title, category, raw_text, is_links)
    
    # Regex to find the <div class="post_header entry-header"> up to the end of <div class="post_content_inner">...</div></div>
    pattern = r'(<article id="' + post_id + r'".*?>\s*<div class="post_featured.*?</div>\s*)(<div class="post_header entry-header">.*?<div class="post_content entry-content">\s*<div class="post_content_inner">.*?</div>\s*</div>)'
    
    def replacer(match):
        return match.group(1) + new_content
    
    blog_html = re.sub(pattern, replacer, blog_html, flags=re.DOTALL)

with open(blog_file, 'w', encoding='utf-8') as f:
    f.write(blog_html)

print("Blog updated successfully!")
