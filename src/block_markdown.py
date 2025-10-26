from enum import Enum 
import re 

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE ="quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"

def markdown_to_blocks(markdown):
    strip_text = markdown.split("\n")
    new_list = [i.strip() for i in strip_text]
   
    result = []
    paragraph = []
        
    curent_block = []

    for line in new_list:
        if line == '':
            if curent_block:
                result.append('\n'.join(curent_block))
                curent_block = []
        else:
            curent_block.append(line)
    if curent_block:
        result.append('\n'.join(curent_block))
    
    return result

def block_to_block_type(block):
    pattern_h = r"^#{1,6} .+"
    pattern_code = r"^```[\s\S]*```$"
    pattern_quote = r"^(> .*(\n> .*)*)$"
    pattern_ul = r"^(- .*(\n- .*)*)$"
    pattern_ol = r"^(\d+\. .*(\n\d+\. .*)*)$"
    
    if re.fullmatch(pattern_h,block):
        return BlockType.HEADING
    elif re.fullmatch(pattern_code,block):
        return BlockType.CODE
    elif re.fullmatch(pattern_quote,block):
        return BlockType.QUOTE
    elif re.fullmatch(pattern_ul,block):
        return BlockType.UNORDERED_LIST
    elif re.fullmatch(pattern_ol,block):
        return BlockType.ORDERED_LIST
    else:
        return BlockType.PARAGRAPH

