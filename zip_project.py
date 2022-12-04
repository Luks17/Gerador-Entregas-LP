
from shutil import copytree
from os import walk, path, chdir
from zipfile import ZipFile


def get_all_file_paths():
  file_paths = []
  
  for root, dirs, files in walk("."):
    for filename in files:
      file_ = path.join(root, filename)
      file_paths.append(file_)
  
  return file_paths   

def copy_folders_and_cd(has_css, has_xhtml):
  copytree(path.join("input", "src"), path.join("output", "src"))

  if(has_css):
    copytree(path.join("input", "css"), path.join("output", "css"))

  if(has_xhtml):
    copytree(path.join("input", "xhtml"), path.join("output", "xhtml"))

  chdir(f"output")

def zip_project(has_css=False, has_xhtml=False):
  copy_folders_and_cd(has_css, has_xhtml)
  file_paths = get_all_file_paths()

  with ZipFile('Entrega.zip','w') as zip:
    for file in file_paths:
      zip.write(file)
