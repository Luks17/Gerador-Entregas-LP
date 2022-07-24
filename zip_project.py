
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

def copy_src_and_cd():
  copytree(path.join("input", "src"), path.join("output", "src"))
  chdir(f"output")

def zip_project():
  copy_src_and_cd()
  file_paths = get_all_file_paths()

  with ZipFile('Entrega.zip','w') as zip:
    for file in file_paths:
      zip.write(file)
