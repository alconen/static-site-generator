from textnode import (
    TextNode,
    text_type_text,
    text_type_bold,
    text_type_italic,
    text_type_code,
    text_type_image,
    text_type_link
)

import re

def extract_markdown_images(text: str) -> list[tuple]:
    return re.findall(r"!\[(.*?)\]\((.*?)\)", text)

def extract_markdown_links(text: str) -> list[tuple]:
    return re.findall(r"\[(.*?)\]\((.*?)\)", text)

def split_nodes_image(old_nodes: list[TextNode]) -> list[TextNode]:
    new_nodes: list[TextNode] = []
    for i in old_nodes:
        if i.text_type is not text_type_text:
            new_nodes.append(i)
        else:
            images = extract_markdown_images(i.text)
            split_nodes: list[TextNode] = []
            text = i.text
            for j in images:
                split_text: list[str] = text.split(f"![{j[0]}]({j[1]})", 1)
                if len(split_text) != 2:
                    raise ValueError("Invalid Syntax: Image not closed")
                if split_text[0] != "":
                    split_nodes.append(TextNode(split_text[0], text_type_text))
                split_text.pop(0)
                split_nodes.append(TextNode(j[0], text_type_image, j[1]))
                text = split_text[0]
            if text != "":
                split_nodes.append(TextNode(text, text_type_text))
            new_nodes.extend(split_nodes)
    return new_nodes

def split_nodes_link(old_nodes: list[TextNode]) -> list[TextNode]:
    new_nodes: list[TextNode] = []
    for i in old_nodes:
        if i.text_type is not text_type_text:
            new_nodes.append(i)
        else:
            links = extract_markdown_links(i.text)
            split_nodes: list[TextNode] = []
            text = i.text
            for j in links:
                split_text: list[str] = text.split(f"[{j[0]}]({j[1]})", 1)
                if len(split_text) != 2:
                    raise ValueError("Invalid Syntax: Link not closed")
                if split_text[0] != "":
                    split_nodes.append(TextNode(split_text[0], text_type_text))
                split_text.pop(0)
                split_nodes.append(TextNode(j[0], text_type_link, j[1]))
                text = split_text[0]
            if text != "":
                split_nodes.append(TextNode(text, text_type_text))
            new_nodes.extend(split_nodes)
    return new_nodes

def split_nodes_delimiter(old_nodes: list[TextNode], delimiter: str, text_type: str) -> list[TextNode]:
    new_nodes: list[TextNode] = []
    for i in old_nodes:
        if i.text_type is not text_type_text:
            new_nodes.append(i)
        elif i.text.count(delimiter) % 2 != 0:
            raise Exception("Invalid Syntax: Delimiter not closed")
        else:
            split_nodes: list[TextNode] = []       
            split_text: list[str] = i.text.split(delimiter, 1)
            while delimiter not in split_text[0] and len(split_text) > 1:
                if split_text[0] != "":
                    split_nodes.append(TextNode(split_text[0], text_type_text))
                split_text.pop(0)
                split_text = split_text[0].split(delimiter, 1)
                split_nodes.append(TextNode(split_text.pop(0), text_type))
                split_text = split_text[0].split(delimiter, 1)
            if split_text[0] != "":
                split_nodes.append(TextNode(split_text[0], text_type_text))
            new_nodes.extend(split_nodes)
    return new_nodes

        
def text_to_textnodes(text: str) -> list[TextNode]:
    nodes = [TextNode(text, text_type_text)]
    nodes = split_nodes_delimiter(nodes, "**", text_type_bold)
    nodes = split_nodes_delimiter(nodes, "*", text_type_italic)
    nodes = split_nodes_delimiter(nodes, "`", text_type_code)
    nodes = split_nodes_image(nodes)
    nodes = split_nodes_link(nodes)
    return nodes