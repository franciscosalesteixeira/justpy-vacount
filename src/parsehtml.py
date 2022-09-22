import sys
import justpy as jp

def parse_html(file):
    
    output = ""
    html = jp.parse_html_file(file)
    f = open("aux.txt", "w")
    
    for c in html.commands:
        output = output + c + "\n"

    f.write(output)
    f.close()

parse_html(sys.argv[1])