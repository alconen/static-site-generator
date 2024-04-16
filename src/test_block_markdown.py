import unittest

from block_markdown import (
    markdown_to_blocks,
    block_to_block_type,
    markdown_to_html_node,
    block_type_heading,
    block_type_code,
    block_type_quote,
    block_type_paragraph,
    block_type_ordered_list,
    block_type_unordered_list
)

class TestBlockMarkdown(unittest.TestCase):
    def test_markdown_to_blocks(self):
        text = """This is **bolded** paragraph

This is another paragraph with *italic* text and `code` here
This is the same paragraph on a new line

* This is a list
* with items"""
        self.assertEqual(markdown_to_blocks(text),
                        ['This is **bolded** paragraph', 'This is another paragraph with *italic* text and `code` here\nThis is the same paragraph on a new line', '* This is a list\n* with items'])
        
    def test_markdown_to_blocks_large(self):
        text = """This is **bolded** paragraph

This is another paragraph with *italic* text and `code` here
This is the same paragraph on a new line


This is another
text
that spans multiple lines

* more text
hello








* This is a list
* with items"""
        self.assertEqual(markdown_to_blocks(text),
                        ['This is **bolded** paragraph', 'This is another paragraph with *italic* text and `code` here\nThis is the same paragraph on a new line', 'This is another\ntext\nthat spans multiple lines', '* more text\nhello', '* This is a list\n* with items'])
        
    def test_markdown_block_to_type_heading(self):
        headings = ["# Heading", "## Heading", "### Heading", "#### Heading", "##### Heading", "###### Heading", """## Heading\nblah"""]
        for i in headings:
            self.assertEqual(block_to_block_type(i),
                             block_type_heading)
            
    def test_markdown_block_to_type_code(self):
        code = ["```code```", "```\ncode\n```"]
        for i in code:
            self.assertEqual(block_to_block_type(i),
                             block_type_code)
            
    def test_markdown_block_to_type_quote(self):
        quote = ">I'm\n>a\n>\n>valid\n>quote"
        self.assertEqual(block_to_block_type(quote),
                         block_type_quote)
    
    def test_markdown_block_to_type_unordered_list(self):
        ulist = "* hi\n- Im\n- list stuff"
        self.assertEqual(block_to_block_type(ulist),
                         block_type_unordered_list)
        
    def test_markdown_block_to_type_ordered_list(self):
        olist = "1. i\n2. \n3. 4"
        self.assertEqual(block_to_block_type(olist),
                         block_type_ordered_list)
        
    def test_markdown_to_html(self):
        text = """This is **bolded** paragraph

This is another paragraph with *italic* text and `code` here
This is the same paragraph on a new line

* This is a list
* with items

1. This is an **ordered**
2. list `with` 
3. some *fun* text

>This is a quote block
>with a [link](example.com)

```
This is a code block with an ![image](image.com)
```
"""
        self.assertEqual(markdown_to_html_node(text).to_html(),
                         """<div><p>This is <b>bold</b> paragraph</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> hereThis is the same paragraph on a new line</p><ul><li>This is a list</li><li>with items</li></ul><ol><li> This is an <b>bold</b></li><li> list <code>with</code> </li><li> some <i>fun</i> text</li></ol><blockquote>>This is a quote block>with a <a href="example.com">link</a></blockquote><pre><code>
This is a code block with an <img src="image.com" alt="image"></img>
</code></pre></div>""")

