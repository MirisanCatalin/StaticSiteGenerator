import unittest

from htmlnode import HTMLNode


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


if __name__ == "__main__":
    unittest.main()
