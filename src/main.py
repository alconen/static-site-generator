import os
import shutil
from textnode import TextNode
from htmlnode import HTMLNode
from htmlnode import LeafNode
            
def copy_dir(sourcePath: str, targetPath:str):
    if not os.path.exists(sourcePath):
        raise FileNotFoundError("Invalid file path")
    if os.path.exists(targetPath):
        shutil.rmtree(targetPath)
    files: list[str] = os.listdir(sourcePath)
    for i in files:
        if os.path.isfile(os.path.join(sourcePath, i)):
            shutil.copy(os.path.join(sourcePath, i), os.path.join(targetPath, i))

def main():
    copy_dir("./static", "./public")


main()