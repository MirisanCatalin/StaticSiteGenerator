import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_eq_false(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a different text node", TextType.BOLD)
        self.assertNotEqual(node, node2)

    def test_repr(self):
        node = TextNode("This is a text node", TextType.ITALIC)
        self.assertEqual(repr(node), "TextNode(This is a text node, TextType.ITALIC, None)")

    def test_url(self):
        node = TextNode("This is a link", TextType.LINK, "https://example.com")
        self.assertEqual(node.url, "https://example.com")

    def test_no_url(self):
        node = TextNode("This is a text node", TextType.TEXT)
        self.assertIsNone(node.url)


if __name__ == "__main__":
    unittest.main()
