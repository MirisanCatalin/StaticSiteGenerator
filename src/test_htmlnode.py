import unittest

from htmlnode import HTMLNode, LeafNode


class TestHtmlNode(unittest.TestCase):

    def test_to_html_props(self):
        node = HTMLNode(
            "div",
            "Hello mom",
            None,
            {"class": "greetings","href": "https://example.com"}
        )
        self.assertEqual
        (
            node.props_to_html(), 
            ' class="greetings" href="https://example.com"'
        )

    def test_repr(self):
        node = HTMLNode(
            "p",
            "This is a paragraph",
            None,
            {"id": "para1"}
        )
        self.assertEqual(
            repr(node),
            "HTMLNode(tag=p, value=This is a paragraph, children=None, props={'id': 'para1'})"
        )

    def test_values(self):
        node = HTMLNode(
            "span",
            "Some text",
            None,
            {"style": "color:red;"}
        )
        self.assertEqual(node.tag, "span")
        self.assertEqual(node.value, "Some text")
        self.assertEqual(node.children, None)
        self.assertEqual(node.props, {"style": "color:red;"})

class TestLeafNode(unittest.TestCase):

    def test_to_html_with_tag_and_props(self):
        node = LeafNode(
            "a",
            "Click here",
            {"href": "https://example.com", "target": "_blank"}
        )
        self.assertEqual(
            node.to_html(),
            '<a href="https://example.com" target="_blank">Click here</a>'
        )

    def test_to_html_with_tag_no_props(self):
        node = LeafNode(
            "b",
            "Bold text"
        )
        self.assertEqual(
            node.to_html(),
            '<b>Bold text</b>'
        )

    def test_to_html_no_tag(self):
        node = LeafNode(
            None,
            "Just some text"
        )
        self.assertEqual(
            node.to_html(),
            'Just some text'
        )

    def test_to_html_no_value(self):
        node = LeafNode(
            "span",
            None
        )
        with self.assertRaises(ValueError):
            node.to_html()


if __name__ == "__main__":
    unittest.main()
