import os
import shutil
from copystatic import copy_dir
from textnode import TextNode
from htmlnode import HTMLNode
from htmlnode import LeafNode
from generate_page import generate_pages_recursive

sourcePath = "./static"
targetPath = "./public"    

def main():
    if os.path.exists(targetPath):
        print(f"Wiping {targetPath}")
        shutil.rmtree(targetPath)
    os.mkdir(targetPath)
    print(f"Copying files from {sourcePath} to {targetPath}")
    copy_dir(sourcePath, targetPath)

    generate_pages_recursive("./content", "./template.html", "./public")
    
main()