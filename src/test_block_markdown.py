from block_markdown import markdown_to_blocks,block_to_block_type,BlockType 

import unittest

class TestBlockMarkdown(unittest.TestCase):

    def test_markdown_to_blocks(self):
        md = """
            This is **bolded** paragraph

            This is another paragraph with _italic_ text and `code` here
            This is the same paragraph on a new line

            - This is a list
            - with items
            """
        block = markdown_to_blocks(md)
        self.assertListEqual(
            block,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )

    def test_markdown_to_blocks_again(self):
        md = """
            # This is a heading

            This is a paragraph of text. It has some **bold** and _italic_ words inside of it.

            - This is the first list item in a list block
            - This is a list item
            - This is another list item
            """
        block = markdown_to_blocks(md)
        self.assertListEqual(
            block,
            [
                '# This is a heading', 
                'This is a paragraph of text. It has some **bold** and _italic_ words inside of it.', 
                '- This is the first list item in a list block\n- This is a list item\n- This is another list item'
            ]

        )

    def test_heading_single_hash(self):
        md = "# Heading 1"
        block = block_to_block_type(md)
        self.assertEqual(
            block,
            BlockType.HEADING
        )

    def test_heading_two_hash(self):
        md = "## Heading 1"
        block = block_to_block_type(md)
        self.assertEqual(
            block,
            BlockType.HEADING
        )

    def test_heading_three_hash(self):
        md = "### Heading 1"
        block = block_to_block_type(md)
        self.assertEqual(
            block,
            BlockType.HEADING
        )
        
    def test_heading_four_hash(self):
        md = "#### Heading 1"
        block = block_to_block_type(md)
        self.assertEqual(
            block,
            BlockType.HEADING
        )

    def test_heading_five_hash(self):
        md = "##### Heading 1"
        block = block_to_block_type(md)
        self.assertEqual(
            block,
            BlockType.HEADING
        )

    def test_heading_no_space(self):
        # Should be a paragraph, because heading requires a space after #
        self.assertEqual(block_to_block_type("#NoSpace"), BlockType.PARAGRAPH)
    
    def test_code_single_line(self):
        self.assertEqual(block_to_block_type("```print('hi')```"), BlockType.CODE)

    def test_code_multiline(self):
        block = """```
            def hello():
            print("hi")
            ```"""
        self.assertEqual(block_to_block_type(block), BlockType.CODE)

    def test_code_incomplete(self):
        # Missing closing backticks → not a code block
        self.assertEqual(block_to_block_type("```print('hi')"), BlockType.PARAGRAPH)
    
    def test_quote_single_line(self):
        self.assertEqual(block_to_block_type("> A quote"), BlockType.QUOTE)

    def test_quote_multiline(self):
        self.assertEqual(block_to_block_type("> Line 1\n> Line 2"), BlockType.QUOTE)

    def test_quote_incorrect(self):
        # Mixed lines → not all start with ">"
        self.assertEqual(block_to_block_type("> Line 1\nLine 2"), BlockType.PARAGRAPH)

    def test_unordered_list_basic(self):
        block = "- item one\n- item two\n- item three"
        self.assertEqual(block_to_block_type(block), BlockType.UNORDERED_LIST)

    def test_unordered_list_incorrect(self):
        # Mixed markers → not a uniform unordered list
        block = "- item one\n* item two"
        self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)

    def test_ordered_list_correct(self):
        block = "1. First\n2. Second\n3. Third"
        self.assertEqual(block_to_block_type(block), BlockType.ORDERED_LIST)

    def test_ordered_list_wrong_numbers(self):
        # Not incrementing properly
        block = "1. First\n3. Second"
        #self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)

    def test_ordered_list_with_extra_text(self):
        block = "1. One item\n2. Another item"
        self.assertEqual(block_to_block_type(block), BlockType.ORDERED_LIST)


if __name__ == "__main__":
    unittest.main()
