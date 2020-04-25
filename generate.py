#!/usr/bin/env python3

from jinja2 import Template

import codecs
import markdown
import re
import os

links = []

template = '''
<meta name="viewport" content="width=device-width, initial-scale=1">
<link rel="stylesheet" href="https://fredericorecsky.github.io/github.markdown.css">
<style>
	.markdown-body {
		box-sizing: border-box;
		min-width: 200px;
		max-width: 980px;
		margin: 0 auto;
		padding: 45px;
	}

	@media (max-width: 767px) {
		.markdown-body {
			padding: 15px;
		}
	}
</style>

<article class="markdown-body">
{{ article }}
</article>
'''


def render(file, links ):
    input_file = codecs.open( file, mode="r")
    text = input_file.read()

    if re.search( r'index.md$', file ):
        text += table_of_contents( links )

    html = markdown.markdown( text )
    
    tm = Template( template )
    doc = tm.render( article=html)

    output_html = re.sub( r"\.md", "", file) + ".html"
    print( output_html )
    with open ( output_html, "w" ) as fh:
        fh.write( doc )

def table_of_contents( links ):
    table = ''
    for link in links:
        if re.search( r'README.md', link ):
            continue
        if re.search( r'index.md', link ):
            continue
        if re.search( r'resume.md', link ):
            continue
        name = re.sub( r"\.md", "", link) + ".html"
        link = re.sub( r"\.md", "", link )
        link = re.sub( r"\_", " ", link )  
        link = re.sub( r"\.\/", " ", link)      

        link = re.sub( r"\/", ": ", link )

        link = link.title()

        print( f'* [{link}]({name})' )
        table += f'* [{link}]({name})\n'
    
    print( table )
    return table

if __name__ == "__main__":
    for (root,dirs,files) in os.walk('.'):
        for (file) in files:
            if re.search( r"\.md$", file ):
                links.append( root + '/' + file )

    for (link) in links:
        render( link, links )