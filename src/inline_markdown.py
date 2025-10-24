from htmlnode import LeafNode, ParentNode
from textnode import TextNode, TextType 

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue
        spllit_nodes = []
        selection = old_node.text.split(delimiter)
        if len(selection) % 2 == 0:
            raise ValleError("invalid syntax, formated selection not cleared")
        for i in range(len(selection)):
            if selection[i] == "":
                continue
            if i % 2 == 0:
                spllit_nodes.append(TextNode(selection[i],TextType.TEXT))
            else:
                spllit_nodes.append(TextNode(selection[i],text_type))
        new_nodes.extend(spllit_nodes)
    return new_nodes
