class HTMLNode():
    def __init__(self, tag: str = None, value: str = None, children: list = None, props: dict = None) -> None:
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
    
    def to_html(self):
        raise NotImplementedError()
    
    def props_to_html(self) -> str:
        if self.props is None:
            return ""
        props = ""
        for k in self.props:
            props += f" {k}=\"{self.props[k]}\""
        return props
    
    def __repr__(self) -> str:
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props}"

class LeafNode(HTMLNode):
    def __init__(self, tag: str = None, value: str = None, props: dict = None) -> None:
        super().__init__(tag, value, [], props)

    def to_html(self):
        html = ""
        if self.value is None:
            raise ValueError()
        if self.tag is None:
            return self.value
        html += f"<{self.tag}"
        if self.props != None:
            html += self.props_to_html()
        html += f">{self.value}</{self.tag}>"
        return html
    
    def __repr__(self) -> str:
        return f"LeafNode({self.tag}, {self.value}, {self.props}"
        
class ParentNode(HTMLNode):
    def __init__(self, children: list, tag: str = None, props: dict = None) -> None:
        self.tag = tag
        self.children = children
        self.props = props

    def to_html(self):
        if self.tag is None:
            raise ValueError("No tag provided")
        if len(self.children) == 0:
            raise ValueError("No children provided")
        html = ""
        for i in self.children:
            html += i.to_html()
        props = ""
        if self.props != None:
            props += self.props_to_html()
        return f"<{self.tag}{props}>{html}</{self.tag}>"
    
    def __repr__(self) -> str:
        return f"ParentNode({self.tag}, {self.children}, {self.props})"
        
    


