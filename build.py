# build.py
import os
from datetime import datetime
from jinja2 import Environment, FileSystemLoader

# Set up Jinja2 to look in the /templates folder
env = Environment(loader=FileSystemLoader('templates'))

# Create the public directory if it doesn't exist
os.makedirs('public', exist_ok=True)

# Define the pages you want to build
pages = ['main.jinja', 'about.jinja', 'svr.jinja']

# Get today's date for the footer
today = datetime.now().strftime("%B %d, %Y")

for page in pages:
    # Load the template (it looks for the .jinja file)
    template = env.get_template(page)
    
    # Render it with the dynamic date variable
    html_content = template.render(last_modified=today)
    
    # Get the filename without the .jinja extension
    # Example: 'main.jinja' becomes 'main'
    base_name = os.path.splitext(page)[0]
    
    # Save the output to the /public folder as an .html file
    output_filename = f"{base_name}.html"
    
    with open(os.path.join('public', output_filename), 'w') as f:
        f.write(html_content)

print("Build complete! .jinja templates converted to .html in /public.")