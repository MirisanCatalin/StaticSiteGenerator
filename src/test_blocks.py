import unittest

from block import (
    markdown_to_blocks,
    block_to_block_type,
    BlockType,
)

class TestBlock(unittest.TestCase):
    def test_markdown_to_blocks(self):
        md = """
            This is **bolded** paragraph

            This is another paragraph with _italic_ text and `code` here
            This is the same paragraph on a new line

            - This is a list
            - with items
            """
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )

    def test_single_paragraph(self):
        md = "Just a simple paragraph without line breaks"
        blocks = markdown_to_blocks(md)
        self.assertEqual(blocks, ["Just a simple paragraph without line breaks"])

    def test_multiple_blank_lines(self):
        md = """
            First paragraph


            Second paragraph after two blank lines

            Third paragraph
        """
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "First paragraph",
                "Second paragraph after two blank lines",
                "Third paragraph",
            ],
        )

    def test_list_items_separated(self):
        md = """
        - Item one

        - Item two

        - Item three
        """
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "- Item one",
                "- Item two",
                "- Item three",
            ],
        )


if __name__ == "__main__":
    unittest.main()
