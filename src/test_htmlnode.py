import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode


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

class TestParentNode(unittest.TestCase):
    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )
    
    def test_to_html_no_tag(self):
        child_node = LeafNode("i", "italic text")
        parent_node = ParentNode(None, [child_node])
        with self.assertRaises(ValueError):
            parent_node.to_html()

    def test_to_html_no_children(self):
        parent_node = ParentNode("div", None)
        with self.assertRaises(ValueError):
            parent_node.to_html()

    def test_repr(self):
        child_node = LeafNode("u", "underlined")
        parent_node = ParentNode("p", [child_node], {"class": "text"})
        self.assertEqual(
            repr(parent_node),
            "ParentNode(tag=p, children=[LeafNode(tag=u, value=underlined, props=None)], props={'class': 'text'})"
        )

    
if __name__ == "__main__":
    unittest.main()
