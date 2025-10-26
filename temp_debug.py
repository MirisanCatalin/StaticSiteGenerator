from block_markdown import markdown_to_blocks
md = '''
```
This is text that _should_ remain
the **same** even with inline stuff
```
'''
blocks = markdown_to_blocks(md)
print('Blocks:', repr(blocks))
