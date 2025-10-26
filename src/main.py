import os
import shutil

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

def main():

    base_dir = os.path.dirname(os.path.abspath(__file__))

    source = os.path.join(base_dir,"static")
    destination = os.path.join(base_dir,"public")
    copy_static(source,destination)

if __name__ == "__main__":
    main()
