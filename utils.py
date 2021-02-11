import glob
import os
from jinja2 import Template

# This function uses glob and os modules to find all files within the content folder and make
# a list of them that will be used to create final web pages. 


def build_list(pages):
    
    all_html_files = glob.glob("./content/*.html")

    for file in all_html_files:
        file_name = os.path.basename(file)
        name_only, extension = os.path.splitext(file_name)
        pages.append({
        "filename": file,
        "title": 'NWM - ' + name_only.capitalize(),
        "nav_title": name_only.capitalize(),
        "output": "./docs/" + file_name,
        })

#This function uses jinja2 to loop through the pages list created from the 'build_list' function and render
# the results to the web pages.

def build_page(pages):
    for page in pages:
        content_html = open(page['filename']).read()
        template_html = open("./templates/base.html").read()
        template = Template(template_html)
        
        index_template = Template('''          
        {% for page in pages %}
        <li class="nav-item"><a class="nav-link js-scroll-trigger" href="{{ page.output }}">{{ page.nav_title }}</a></li>
        {% endfor %}
        ''')

        updated_page = index_template.render()
        
        updated_page = template.render(
            title=page['title'],
            content=content_html,
        )

        open(page['output'], 'w+').write(updated_page)


#This function creates a plain template for a new content page.

def create_new():
    new_page_template = '''
    <h1>{{ New Content!}} </h1>
    <p>{{ New content...}} </p>
    '''
    open('../content/new_content_page.html', 'w+').write(new_page_template)

#The main function contains a loop that runs the two functions for each page, with the
# result of updating each webpage.

def main():
    pages = []
    build_list(pages)
    build_page(pages)