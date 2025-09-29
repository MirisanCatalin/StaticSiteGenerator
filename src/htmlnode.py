
class HTMLNode:
    """
    Base class for representing an HTML element.

    This class provides the structure for both leaf and parent HTML nodes, 
    including optional HTML attributes (props), text content (value), and child nodes.

    Attributes:
        tag (Optional[str]): The HTML tag name (e.g., 'p', 'div', 'a'). Can be None for plain text nodes.
        value (Optional[str]): The text content of the node (used for leaf nodes).
        children (Optional[List[HTMLNode]]): List of child nodes (used for parent nodes).
        props (Optional[Dict[str, str]]): Dictionary of HTML attributes (e.g., {"href": "..."})
    """
    def __init__(self,tag: str=None,value: str=None,children: list=None,props: dict[str,str]=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError

    def props_to_html(self) -> str:
        if self.props is None:
            return ""
        props_html = ""
        for prop in self.props:
            props_html += f' {prop}="{self.props[prop]}"'
        return props_html

    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, children: {self.children}, {self.props})"

class LeafNode(HTMLNode):
    """
    Represents a leaf HTML element with no child nodes.

    Leaf nodes store a single piece of text (value) and optionally a tag and HTML attributes.

    Examples:
        LeafNode('b', 'bold')      => <b>bold</b>
        LeafNode(None, 'plain')    => plain
    """
    def __init__(self,tag: str,value:str,props: dict[str,str]=None):
        super().__init__(tag,value,None,props)

    def to_html(self):
        if self.value is None:
            raise ValueError("All leaf nodes must have a value.")
        if self.tag is None:
            return f"{self.value}"
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"
    
    def __repr__(self):
        return f'LeafNode({self.tag}, {self.value}, {self.props})'

class ParentNode(HTMLNode):
    """
    Represents an HTML element that contains child nodes.

    Parent nodes do not have a direct text value; instead, they wrap other HTMLNode instances.
    They can also have a tag and optional HTML attributes.

    Examples:
        ParentNode('p', [LeafNode('b', 'bold')])  => <p><b>bold</b></p>
    """
    def __init__(self,tag: str,children:list,props: dict[str,str]=None):
        super().__init__(tag,None,children,props)

    def to_html(self) -> str:
        if self.tag is None:
            raise ValueError("Must be a tag")
        if self.children is None and isinstance(self.children,list):
            raise ValueError("Children is missing a value")
        
        children_html = ""
        for child in self.children:
            children_html += child.to_html()

        props_html = self.props_to_html()

        return f"<{self.tag}{props_html}>{children_html}</{self.tag}>"
    
    def __repr__(self) ->str:
        return f'ParentNode({self.to_html}, childrem: {self.children},{self.props})'

