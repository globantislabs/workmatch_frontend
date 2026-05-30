import os
import re

# Files to update
files_to_update = [
    'company-overview.html',
    'careers.html', 
    'clients.html',
    'talent-solutions.html',
    'custom-software-engineering.html',
    'cloud-solutions.html',
    'data-ai-solutions.html',
    'cms-solutions.html',
    'managed-services.html',
    'accounting-as-a-service.html',
    'bfsi.html',
    'healthcare.html',
    'retail-ecommerce.html',
    'manufacturing.html',
    'saas-startups.html',
    'blog.html',
    'blog-details.html',
    'hire-talent.html',
    'contact.html',
    'partner-with-us.html',
    'skills-listing.html'
]

# Read index.html to get the correct header and footer
with open('index.html', 'r', encoding='utf-8') as f:
    index_content = f.read()

# Extract mobile menu section
mobile_menu_match = re.search(r'(<div id="mobile-menu".*?</nav>\s*</div>)', index_content, re.DOTALL)
mobile_menu = mobile_menu_match.group(1) if mobile_menu_match else ''

# Extract header section
header_match = re.search(r'(<header class="fixed.*?</header>)', index_content, re.DOTALL)
header = header_match.group(1) if header_match else ''

# Extract footer section
footer_match = re.search(r'(<footer class="bg-gray-900.*?</footer>)', index_content, re.DOTALL)
footer = footer_match.group(1) if footer_match else ''

# Extract scroll to top button
scroll_btn_match = re.search(r'(<button id="scroll-top".*?</button>)', index_content, re.DOTALL)
scroll_btn = scroll_btn_match.group(1) if scroll_btn_match else ''

# Extract JavaScript for mobile menu
js_match = re.search(r'(<script>\s*// Mobile menu toggle.*?</script>)', index_content, re.DOTALL)
js_script = js_match.group(1) if js_match else ''

print(f'Mobile menu length: {len(mobile_menu)}')
print(f'Header length: {len(header)}')
print(f'Footer length: {len(footer)}')
print(f'Scroll button length: {len(scroll_btn)}')
print(f'JS script length: {len(js_script)}')

# Process each file
for filename in files_to_update:
    if not os.path.exists(filename):
        print(f'File not found: {filename}')
        continue
    
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original_content = content
    
    # Replace mobile menu
    content = re.sub(
        r'<div id="mobile-menu".*?</nav>\s*</div>',
        mobile_menu,
        content,
        flags=re.DOTALL
    )
    
    # Replace header
    content = re.sub(
        r'<header class="fixed.*?</header>',
        header,
        content,
        flags=re.DOTALL
    )
    
    # Replace footer
    content = re.sub(
        r'<footer class="bg-gray-900.*?</footer>',
        footer,
        content,
        flags=re.DOTALL
    )
    
    # Add scroll to top button before the script if not present
    if 'id="scroll-top"' not in content:
        content = re.sub(
            r'(</footer>\s*)(<script)',
            r'\1' + scroll_btn + r'\n\n  \2',
            content
        )
    
    # Update mobile menu JavaScript
    if '// Mobile menu toggle' not in content:
        # Add the script before </body>
        content = content.replace('</body>', js_script + '\n</body>')
    
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f'Updated: {filename}')

print('\nAll files updated successfully!')
