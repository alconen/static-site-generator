import os
from block_markdown import markdown_to_html_node

def extract_title(markdown: str) -> str:
    split = markdown.split("\n")
    for i in split:
        if i.startswith("# "):
            return i[2:]
    raise Exception("Invalid Markdown: No Title")
    
def generate_page(from_path: str, template_path: str, dest_path: str):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    with open(from_path) as f:
        input_markdown = f.read()
    with open(template_path) as f:
        input_template = f.read()
    output_html: str = markdown_to_html_node(input_markdown).to_html()
    title: str = extract_title(input_markdown)
    title_template: str = input_template.replace(r"{{ Title }}", title)
    output_html: str = title_template.replace(r"{{ Content }}", output_html)
    if os.path.dirname(dest_path) != "":
        os.makedirs(os.path.dirname(dest_path),exist_ok=True)
    with open(dest_path, "w") as f:
        f.write(output_html)
    
def generate_pages_recursive(dir_path_content: str, template_path: str, dest_dir_path: str):
    files: list[str] = os.listdir(dir_path_content)
    for i in files:
        sourceFile = os.path.join(dir_path_content, i)
        targetFile = os.path.join(dest_dir_path, i)
        print(f"Generating {sourceFile} from {targetFile}")
        if os.path.isfile(sourceFile):
            md_name = targetFile.replace("md", "html")
            generate_page(sourceFile, template_path, md_name)
        elif os.path.isdir(sourceFile):
            os.mkdir(os.path.join(targetFile))
            generate_pages_recursive(sourceFile, template_path, targetFile)

        