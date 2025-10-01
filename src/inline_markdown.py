from textnode import TextNode, TextType

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue

        split_nodes = []
        sections = old_node.text.split(delimiter)

        if len(sections) % 2 == 0:
            raise ValueError("Invalid markdown section: missing closing delimiter")

        for i in range(len(sections)):
            if sections[i] == "":
                continue
            if i % 2 == 0:  # outside delimiter → plain text
                split_nodes.append(TextNode(sections[i], TextType.TEXT))
            else:  # inside delimiter → apply text_type
                split_nodes.append(TextNode(sections[i], text_type))

        new_nodes.extend(split_nodes)

    return new_nodes

