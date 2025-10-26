
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
