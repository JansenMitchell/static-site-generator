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
    
    def __repr__(self) -> str:
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"
    
class LeafNode(HTMLNode):
       def __init__(self, tag, value, props=None):
           super().__init__(tag, value, [], props=None)
           
           def to_html(self):
               if self.value == None:
                   raise ValueError("Leaf node must have a value.")
               if self.tag == None:
                   return self.value
               #TODO: Loop through self.props dict to get the needed values.
               if self.props != None:
                   return f"<{self.tag}>{self.value}</{self.tag}>\n<a href=<{self.props["href"]}</a>"
               return f"<{self.tag}>{self.value}</{self.tag}>"
           