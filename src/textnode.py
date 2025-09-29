from enum import Enum

from htmlnode import HTMLNode, LeafNode

class TextType(Enum):
    """Enumeration of supported text styles."""
    TEXT = "text"
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    IMAGE = "image"
    LINK = "link"


class TextNode:
    """
    Represents a piece of text with a specific type and an optional URL.

    Attributes:
        text (str): The actual text content.
        text_type (TextType): The type of the text (e.g., plain, bold, link).
        url (Optional[str]): An optional URL, only relevant if the text is a link.
    """

    def __init__(self,text: str, text_type: TextType, url: str = None) -> None:
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, other) -> bool:
        if not isinstance(other,TextNode):
            return NotImplemented
        return self.text == other.text and self.text_type == other.text_type and self.url == other.url

    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"

def text_node_to_html_node(text_node: TextNode) -> LeafNode:
    """
    Convert a TextNode into a corresponding LeafNode for HTML rendering.

    Args:
        text_node (TextNode): The text node to convert.

    Returns:
        LeafNode: The HTML representation of the text node.

    Raises:
        TypeError: If the input is not a TextNode.
        ValueError: If the text_type of the node is not supported.
    """
    if not isinstance(text_node, TextNode):
        raise Exception("Is nothing that matches my node types")
    if text_node.text_type == TextType.TEXT:
        return LeafNode(None,text_node.text)
    if text_node.text_type == TextType.BOLD:
        return LeafNode('b',text_node.text)
    if text_node.text_type == TextType.ITALIC:
        return LeafNode('i',text_node.text)
    if text_node.text_type == TextType.CODE:
        return LeafNode('code',text_node.text)
    if text_node.text_type == TextType.LINK:
        return LeafNode('a',text_node.text,{"href":text_node.url})
    if text_node.text_type == TextType.IMAGE:
        return LeafNode('img',"",{"src":text_node.url,"alt": text_node.text})
    
    
