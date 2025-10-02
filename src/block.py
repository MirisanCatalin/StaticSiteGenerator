import re
from enum import Enum 

def markdown_to_blocks(markdown: str):
    split_markdown = markdown.split("\n\n")
    strip_markdown = [line.strip().replace("            ","") for line in split_markdown if line.strip() != ""]
    return strip_markdown

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"

def block_to_block_type(block_markdown):
    if re.match(r"^#{1,6}"):
       return BlockType.HEADING
    if block_markdown.startswith("```") and block_markdown.endswith("```"):
        return BlockType.CODE

    lines = block_markdown.split("\n")
    if all(lines.startswith(">") for line in lines):
        return BlockType.QUOTE

    if all(lines.startswith("- ") for line in lines):
        return BlockType.UNORDERED_LIST

    ordered = True 
    for i, lines in enumerate(lines,start=1):
        if not re.match(rf"^{i}\.", line):
            ordered = False 
            break
    if ordered and len(lines) > 0:
        return BlockType.ORDERED_LIST

    return BlockType.PARAGRAPH
    
    

