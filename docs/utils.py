# This function uses glob and os modules to find all files within the content folder and make
# a list of them that will be used to create final web pages. 


def build_list(pages):
    import glob
    import os
    all_html_files = glob.glob("../content/*.html")

    for file in all_html_files:
        file_name = os.path.basename(file)
        name_only, extension = os.path.splitext(file_name)
        pages.append({
        "filename": file,
        "title": 'NWM - ' + name_only.capitalize(),
        "output": file_name,
        })

#This function uses jinja2 to loop through the pages list created from the 'build_list' function and render
# the results to the web pages.

def build_pages(pages):        
    from jinja2 import Template
    for page in pages:
        content_html = open(page['filename']).read()
        template_html = open("../templates/base.html").read()
        template = Template(template_html)
        updated_page = template.render(
            title=page['title'],
            content=content_html,
        )
        open(page['output'], 'w+').write(updated_page)

#This function loops through the navbar/index and creates an updated navbar based on the pages in the content folder.

def build_index():
    from jinja2 import Template
    index_template = Template('''
    {% for page in pages %}
    <li class="nav-item"><a class="nav-link js-scroll-trigger" href="{{ page.output }}">{{ page.title }}</a></li>
    {% endfor %}
    ''')
    index_template.render(pages=pages, content=content_html)

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
    build_pages(pages)