import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_eq_false(self):
        node1 = TextNode("Ask one",TextType.ITALIC,"https://www.boot.dev")
        node2 = TextNode("Ask one",TextType.ITALIC,"https://www.wikipedia.org/")
        self.assertNotEqual(node1,node2)

    def test_eq_false1(self):
        node1 = TextNode("Ask one",TextType.ITALIC,"https://www.boot.dev")
        node2 = TextNode("Ask one",TextType.CODE,"https://www.boot.dev")
        self.assertNotEqual(node1,node2)

    def test_eq_false2(self):
        node1 = TextNode("Ask one",TextType.ITALIC,"https://www.boot.dev")
        node2 = TextNode("Ask two",TextType.ITALIC,"https://www.wikipedia.org/")
        self.assertNotEqual(node1,node2)
    
    def test_repr(self):
        node = TextNode("This is a text node", TextType.TEXT, "https://www.boot.dev")
        self.assertEqual(
            "TextNode(This is a text node, text, https://www.boot.dev)", repr(node)
        )



if __name__ == "__main__":
    unittest.main()
