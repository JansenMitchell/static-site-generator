class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
        
    def to_html(self):
        raise NotImplementedError("Not implemented!")
    
    def props_to_html(self):
        return f" href={self.props["href"]} target={self.props["target"]}"
    
    def __eq__(self, value):
        if isinstance(value, HTMLNode):
            if (self.tag == value.tag 
                and self.value == value.value 
                and self.children == value.children
                and self.props == value.props):
                return True
            return False
        return False
    
    def __repr__(self) -> str:
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"
    
class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, [], props)
           
    def to_html(self):
        if self.value == None:
            raise ValueError("Leaf node must have a value.")
        if self.tag == None:
            return self.value
        if self.props != None:
            attributes = []
            for key, value in self.props.items():
                attributes.append(f'{key}="{value}"')
            attributes_str = " ".join(attributes)
            return f"<{self.tag} {attributes_str}>{self.value}</{self.tag}>"
        return f"<{self.tag}>{self.value}</{self.tag}>"
    
class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)
        
    def to_html(self):
        if self.tag == None:
            raise ValueError("Parent node must have a tag.")
        if self.children == None:
            raise ValueError("Parent node must have children")
        
        result = f"<{self.tag}>"
        for child in self.children:
            result += child.to_html()    
        result += f"</{self.tag}>"
        return result