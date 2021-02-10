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


#The 'pages' list contains dictionaries with keys/links for each page.

pages = [
    { 
        'filename': '../content/index.html',
        'output': './index.html',
        'title': 'NWM - Index',
    },
    {
        'filename': '../content/education.html',
        'output': './education.html',
        'title': 'NWM - Education',
    },
    {
        'filename': '../content/interests.html',
        'output': './interests.html',
        'title': 'NWM - Interests',
    },
    {
        'filename': '../content/skills.html',
        'output': './skills.html',
        'title': 'NWM - Skills',
    },
    ]
    

#The main function contains a loop that runs the two functions for each page, with the
# result of updating each webpage.

def main():
    for page in pages:
        page_filename, page_output, page_title = open_pages(page)
        update_pages(page_filename, page_output, page_title)


main()