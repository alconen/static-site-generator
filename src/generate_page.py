import os
from block_markdown import markdown_to_html_node

def extract_title(markdown: str):
    split = markdown.split("\n")
    if not split[0].startswith("# "):
        raise Exception("Invalid Markdown: No Title")
    
def generate_page(from_path: str, template_path: str, dest_path: str):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    with open(from_path) as f:
        input_markdown = f.read()
    with open(template_path) as f:
        input_template = f.read()
    output_html: str = markdown_to_html_node(input_markdown).to_html
    title: str = extract_title(input_markdown)
    title_template: str = input_template.replace(r"{{ Title }}", title)
    output_html: str = title_template.replace(r"{{ Content }}", output_html)
    if os.path.exists(dest_path):
        os.remove(dest_path)
    os.makedirs(dest_path)
    with open(dest_path, "w") as f:
        f.write(output_html)
    
        
    
    
    

        