from htmlnode import LeafNode


text_type_text: str = "text"
text_type_bold: str = "bold"
text_type_italic: str = "italic"
text_type_code: str = "code"
text_type_link: str = "link"
text_type_image: str = "img"



class TextNode():
    def __init__(self, text: str, text_type: str, url: str = None) -> None:
        self.text: str = text
        self.text_type: str = text_type
        self.url: str = url

    def __eq__(self, __value: object) -> bool:
        if (
            self.text == __value.text and
            self.text_type == __value.text_type and
            self.url == __value.url
        ):
            return True
        else:
            return False

    def __repr__(self) -> str:
        return f"TextNode({self.text}, {self.text_type}, {self.url})"
    
def text_node_to_html_node(text_node: TextNode) -> LeafNode:
    if text_node.text_type == text_type_text:
        return LeafNode(None, text_node.text)
    elif text_node.text_type == text_type_bold:
        return LeafNode("b", text_node.text_type)
    elif text_node.text_type == text_type_italic:
        return LeafNode("i", text_node.text)
    elif text_node.text_type == text_type_code:
        return LeafNode("code", text_node.text)
    elif text_node.text_type == text_type_link:
        return LeafNode("a", text_node.text, {"href": text_node.url})
    elif text_node.text_type == text_type_image:
        return LeafNode("img", "", {
                "src": text_node.url,
                "alt": text_node.text
                })
    else:
        raise ValueError(f"Text type unsupported: {text_node.text_type}")