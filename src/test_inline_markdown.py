import unittest

from inline_markdown import split_nodes_delimiter
from textnode import TextNode,TextType

class TestInlineMarkdown(unittest.TestCase):
    def test_delim_bold(self):
        node = TextNode("This is text with a **bolded** word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertListEqual(
            [
                TextNode("This is text with a ", TextType.TEXT),
                TextNode("bolded", TextType.BOLD),
                TextNode(" word", TextType.TEXT),
            ],
            new_nodes,
        )

    def test_delim_italic(self):
        node = TextNode("This is text with an __italic__ word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "__", TextType.BOLD)
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("italic", TextType.BOLD),
                TextNode(" word", TextType.TEXT),
            ],
            new_nodes,
        )

    def test_no_delimiter(self):
        node = TextNode("This is text without delimiters", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertListEqual(
            [TextNode("This is text without delimiters", TextType.TEXT)],
            new_nodes,
        )

    def test_delim_code(self):
        node = TextNode("This is text with a `code` snippet", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertListEqual(
            [
                TextNode("This is text with a ", TextType.TEXT),
                TextNode("code", TextType.CODE),
                TextNode(" snippet", TextType.TEXT),
            ],
            new_nodes,
        )

    def test_multiple_delimiters(self):
        node = TextNode("This **is** a __test__ with `code`", TextType.TEXT)
        nodes_after_bold = split_nodes_delimiter([node], "**", TextType.BOLD)
        nodes_after_italic = []
        for n in nodes_after_bold:
            nodes_after_italic.extend(split_nodes_delimiter([n], "__", TextType.ITALIC))
        final_nodes = []
        for n in nodes_after_italic:
            final_nodes.extend(split_nodes_delimiter([n], "`", TextType.CODE))
        self.assertListEqual(
            [
                TextNode("This ", TextType.TEXT),
                TextNode("is", TextType.BOLD),
                TextNode(" a ", TextType.TEXT),
                TextNode("test", TextType.ITALIC),
                TextNode(" with ", TextType.TEXT),
                TextNode("code", TextType.CODE),
            ],
            final_nodes,
        )


if __name__ == "__main__":
    unittest.main()
