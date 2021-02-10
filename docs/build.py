#The 'open_pages' function pulls in the links from the 'pages' list.

def open_pages(page):

        page_filename = page['filename']
        page_output = page['output']
        page_title = page['title']
        return page_filename, page_output, page_title 


#The 'update_pages' function uses the returned variables from the 'open_pages' function
# to add the contents to a template and write that content to the final webpage files.

def update_pages(page_filename, page_output, page_title):
    template = open('../templates/base.html').read()
    fragment_content = open(page_filename).read()
    finished_index_page = template.replace("{{content}}", fragment_content)
    finished_index_page = finished_index_page.replace("{{title}}", page_title)
    open(page_output, 'w+').write(finished_index_page)


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

    #template.render(pages=pages, content=content_html)


def build_pages(pages):        
    from jinja2 import Template
    for page in pages:
        content_html = open(page['filename']).read()
        template_html = open("../templates/base.html").read()
        template = Template(template_html)
        template.render(
            title=page['title'],
            content=content_html,
        )
    template = Template('''
    {% for page in pages %}
    <li class="nav-item"><a class="nav-link js-scroll-trigger" href="{{ page.output }}">{{ page.title }}</a></li>
    {% endfor %}
    ''')
    template.render(pages=pages, content=content_html)

#The main function contains a loop that runs the two functions for each page, with the
# result of updating each webpage.

def main():
    pages = []
    build_list(pages)
    build_pages(pages)
    #for page in pages:
    #    page_filename, page_output, page_title = open_pages(page)
    #    update_pages(page_filename, page_output, page_title)


main()