import os
import shutil
from copystatic import copy_dir
from textnode import TextNode
from htmlnode import HTMLNode
from htmlnode import LeafNode

sourcePath = "./static"
targetPath = "./public"    

def main():
    print(f"Wiping {targetPath}")
    if os.path.exists(targetPath):
        shutil.rmtree(targetPath)
    os.mkdir(targetPath)
    print(f"Copying files from {sourcePath} to {targetPath}")
    copy_dir(sourcePath, targetPath)

main()