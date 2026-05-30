import os
import re

def remove_html_extensions(directory):
    for filename in os.listdir(directory):
        if filename.endswith(".html"):
            filepath = os.path.join(directory, filename)
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Replace 'name.html' in href or src, but not the filename itself
            # We want to change href="careers.html" to href="careers"
            # We need to be careful not to match things like "index.html" if we don't want to change it?
            # Actually, user wants no .html anywhere.
            
            # Regex to find .html inside href or src
            new_content = re.sub(r'(href|src)="([^"]+)\.html"', r'\1="\2"', content)
            
            if content != new_content:
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                print(f"Updated: {filename}")

if __name__ == "__main__":
    remove_html_extensions("workmatch_frontend")
