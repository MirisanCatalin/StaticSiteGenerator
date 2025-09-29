import unittest

from htmlnode import HTMLNode, LeafNode

class TestHTMLnode(unittest.TestCase):
    def test_to_html(self):
        node = HTMLNode(
            'div',
            'hello mom',
            None,
            {"class":"greeting","href":"https://boot.dev"},
        )
        self.assertEqual(
            node.props_to_html(),
            ' class="greeting" href="https://boot.dev"'
        )

    def test_values(self):
        node = HTMLNode(
            "ana",
            "I miss you"
        )
        self.assertEqual(
            node.tag,
            'ana'
        )

        self.assertNotEqual(
            node.value,
            "I miss yu"
        )
        
        self.assertEqual(
            node.children,
            None
        )

        self.assertEqual(
            node.props,
            None
        )

    def test_repr(self):
        node = HTMLNode(
            'pip',
            'What a nice word',
            None,
            {"class":"primary"}
        )
        self.assertEqual(
            node.__repr__(),
            "HTMLNode(pip, What a nice word, children: None, {'class': 'primary'})"
        )

class TestLeafNode(unittest.TestCase):
    def test_leaf_to_html(self):
        node = LeafNode('p','Anan are mere')
        self.assertEqual(node.to_html(),'<p>Anan are mere</p>')
    
    def test_leaf_to_html_a(self):
        node = LeafNode('a','Click me boy',{'href':'https://google.com'})
        self.assertEqual(node.to_html(),'<a href="https://google.com">Click me boy</a>')

    def test_leaf_to_html_no_tag(self):
        node = LeafNode(None,'Hello World!')
        self.assertEqual(node.to_html(),"Hello World!")

    def test_repr(self):
        node = LeafNode('a','Click me boy',{'href':'https://google.com'})
        self.assertEqual(
            node.__repr__(),
            "LeafNode(a, Click me boy, {'href': 'https://google.com'})"
        )

if __name__ == "__main__":
    unittest.main()
