import os
import shutil

from htmlnode import to_html

def copy_static(source_dir, dest_dir):
    if os.path.exists(dest_dir):
        shutil.rmtree(dest_dir)

    os.makedirs(dest_dir,exist_ok=True)

    for item in os.listdir(source_dir):
        source_path = os.path.join(source_dir,item)
        dest_path = os.path.join(dest_dir,item)

        if os.path.isdir(source_path):
            copy_static(source_path,dest_path)
        else:
            shutil.copy(source_path,dest_path)


def extract_title(markdown):
    markdown = markdown.strip(" #")

def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}.")

    markdown_data = ""
    with open(from_path,"r") as file:
        markdown_data = file.read()

    template_data = ""
    with open(template_path,"r") as file:
        template_data = file.read()

    html_string = markdown_to_html_node(markdown_data).to_html()


def main():

    base_dir = os.path.dirname(os.path.abspath(__file__))

    source = os.path.join(base_dir,"static")
    destination = os.path.join(base_dir,"public")
    copy_static(source,destination)

if __name__ == "__main__":
    main()
