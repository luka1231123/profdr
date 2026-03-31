# build.py
import os
import time
import argparse
from datetime import datetime
from jinja2 import Environment, FileSystemLoader
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

def build():
    """Compiles .jinja templates into .html files."""
    print(f"[{datetime.now().strftime('%H:%M:%S')}] Starting build...")
    
    # Set up Jinja2 to look in the /templates folder
    env = Environment(loader=FileSystemLoader('templates'))

    # Create the public directory if it doesn't exist
    os.makedirs('public', exist_ok=True)

    # Safely get all .jinja files (handles case where dir might not exist yet)
    try:
        pages = [f for f in os.listdir('templates') if f.endswith('.jinja')]
    except FileNotFoundError:
        print("Error: 'templates' directory not found. Please create it.")
        return

    # Get today's date for the footer
    today = datetime.now().strftime("%B %d, %Y")

    for page in pages:
        # Load the template
        template = env.get_template(page)
        
        # Render it with the dynamic date variable
        html_content = template.render(last_modified=today)
        
        # Get the filename without the .jinja extension
        base_name = os.path.splitext(page)[0]
        output_filename = f"{base_name}.html"
        
        # Save the output to the /public folder
        with open(os.path.join('public', output_filename), 'w') as f:
            f.write(html_content)

    print("Build complete! .jinja templates converted to .html in /public.")

class TemplateChangeHandler(FileSystemEventHandler):
    """Listens for changes in the templates directory and triggers a rebuild."""
    def on_modified(self, event):
        # Only rebuild if a file (not a directory) was changed, and it's a .jinja file
        if not event.is_directory and event.src_path.endswith('.jinja'):
            print(f"\nDetected change in: {event.src_path}")
            build()

def main():
    # Set up command-line argument parsing
    parser = argparse.ArgumentParser(description="Build Jinja templates to HTML.")
    parser.add_argument('-c', '--continuous', action='store_true', 
                        help="Watch the templates directory and rebuild on changes.")
    args = parser.parse_args()

    # Always perform an initial build
    build()

    # If the -c flag was passed, start the file watcher
    if args.continuous:
        print("\nWatching for changes in 'templates/'... (Press Ctrl+C to stop)")
        
        event_handler = TemplateChangeHandler()
        observer = Observer()
        
        # Schedule the observer to watch the 'templates' directory
        observer.schedule(event_handler, path='templates', recursive=True)
        observer.start()
        
        try:
            # Keep the main thread alive while the observer runs in the background
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            # Gracefully handle Ctrl+C
            observer.stop()
            print("\nStopped watching.")
        
        observer.join()

if __name__ == "__main__":
    main()