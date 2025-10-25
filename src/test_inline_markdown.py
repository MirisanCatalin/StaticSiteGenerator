import unittest

from inline_markdown import split_nodes_delimiter,extract_markdown_images, extract_markdown_links
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
    
    def test_extract_markdown_images(self):
        matches = extract_markdown_images(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
        )
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)

    def test_extract_markdown_links(self):
        matches = extract_markdown_links(
            "This is text with a [link](https://www.example.com)"
        )
        self.assertListEqual([("link", "https://www.example.com")], matches)
    
    def test_extract_multiple_markdown_links_and_images(self):
        text = "Here is an ![image1](https://example.com/image1.png) and a [link1](https://example.com/link1) followed by ![image2](https://example.com/image2.png) and [link2](https://example.com/link2)."
        image_matches = extract_markdown_images(text)
        link_matches = extract_markdown_links(text)
        #print("Image Matches:", image_matches)
        #print("Link Matches:", link_matches)
        self.assertListEqual(
            [
                ("image1", "https://example.com/image1.png"),
                ("image2", "https://example.com/image2.png"),
            ],
            image_matches,
        )
        self.assertListEqual(
            [
                ("link1", "https://example.com/link1"),
                ("link2", "https://example.com/link2"),
            ],
           link_matches,
        )
if __name__ == "__main__":
    unittest.main()
