import re
from htmlnode import (
    HTMLNode,
    ParentNode,
    LeafNode
)
from textnode import (
    TextNode,
    text_node_to_html_node
)
from inline_markdown import text_to_textnodes

block_type_paragraph = "paragraph"
block_type_heading = "heading"
block_type_code = "code"
block_type_quote = "quote"
block_type_unordered_list = "unordered_list"
block_type_ordered_list = "ordered_list"


def markdown_to_blocks(markdown: str) -> list[str]:
    blocks: list[str] = markdown.split("\n\n")
    output: list[str] = []
    for i in blocks:
        if i != "":
            output.append(i.strip())
    return output

def block_to_block_type(block: str) -> str:
    if 2 <= (len(block) - len(block.lstrip("# "))) <= 7:
        return block_type_heading
    elif block[:3] == block[-3:] == "```":
        return block_type_code
    lines: list[str] = block.split("\n")
    if block.startswith(">"):
        for i in lines:
            if not i.startswith(">"):
                return block_type_paragraph
        return block_type_quote
    elif block.startswith("* ") or block.startswith("- "):
        for i in lines:
            if not (i.startswith("* ") or i.startswith("- ")):
                return block_type_paragraph
        return block_type_unordered_list
    elif block.startswith("1. "):
        tracker: int = 1
        for i in lines:
            if not i.startswith(f"{tracker}. "):
                return block_type_paragraph
            tracker += 1
        return block_type_ordered_list
    return block_type_paragraph  

def text_to_children(text: str):
    nodes: list[TextNode] = text_to_textnodes(text)
    children = []
    for i in nodes:
        node = text_node_to_html_node(i)
        children.append(node)
    return children

def paragraph_block_to_html_node(block: str) -> HTMLNode:
    lines: list[str] = block.split("\n")
    text: str = "".join(lines)
    children = text_to_children(text)
    return ParentNode(children, "p")

def heading_block_to_html_node(block: str) -> HTMLNode:
    blocks: list[str] = block.split(" ", 1)
    level: int = len(blocks[0])
    children = text_to_children(blocks[1])
    return ParentNode(children, f"h{level}")

def code_block_to_html_node(block: str) -> HTMLNode:
    block = block.strip("`")
    children = text_to_children(block)
    return ParentNode([
       ParentNode(children, "code")
    ], "pre")

def quote_block_to_html_node(block: str) -> HTMLNode:
    lines: list[str] = block.split("\n")
    for i in lines:
        i = i.lstrip(">")
    block = "".join(lines)
    children = text_to_children(block)
    return ParentNode(children, "blockquote")

def ulist_block_to_html_node(block: str) -> HTMLNode:
    items: list[LeafNode] = []
    lines: list[str] = block.split("\n")
    for i in lines:
        if i.startswith("* "):
            line = i.lstrip("* ")
        elif i.startswith("- "):
            line = i.lstrip("- ")
        children = text_to_children(line)
        items.append(ParentNode(children, "li"))
    return ParentNode(items, "ul")

def olist_block_to_html_node(block: str) -> HTMLNode:
    items: list[LeafNode] = []
    lines: list[str] = block.split("\n")
    for i in lines:
        line = i[2:]
        children = text_to_children(line)
        items.append(ParentNode(children, "li"))
    return ParentNode(items, "ol")

def markdown_to_html_node(markdown: str) -> HTMLNode:
    blocks = markdown_to_blocks(markdown)
    children: list[HTMLNode] = []
    for i in blocks:
        block_type = block_to_block_type(i)
        if block_type == block_type_paragraph:
            children.append(paragraph_block_to_html_node(i))
        elif block_type == block_type_heading:
            children.append(heading_block_to_html_node(i))
        elif block_type == block_type_code:
            children.append(code_block_to_html_node(i))
        elif block_type == block_type_quote:
            children.append(quote_block_to_html_node(i))
        elif block_type == block_type_unordered_list:
            children.append(ulist_block_to_html_node(i))
        elif block_type == block_type_ordered_list:
            children.append(olist_block_to_html_node(i))
    return ParentNode(children, "div")
