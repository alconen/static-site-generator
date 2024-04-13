from htmlnode import LeafNode

class TextNode():
    def __init__(self, text: str, text_type: str, url: str = None) -> None:
        self.text = text
        self.text_type = text_type
        self.url = url

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
    match text_node.text_type:
        case "text":
            return LeafNode(None, text_node.text)
        case "bold":
            return LeafNode("b", text_node.text_type)
        case "italic":
            return LeafNode("i", text_node.text)
        case "code":
            return LeafNode("code", text_node.text)
        case "link":
            return LeafNode("a", text_node.text, {"href": text_node.url})
        case "image":
            return LeafNode("img", "", {
                "src": text_node.url,
                "alt": text_node.text
                })
        case _ : 
            raise ValueError(f"Text type unsupported: {text_node.text_type}")