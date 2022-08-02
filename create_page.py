
from os import path, sep, walk, listdir
from fpdf import FPDF
from datetime import date
from lib.util import *


HEIGHT = 7
WIDTH = 40
ALIGN = "L"


class Project:

  def __init__(self, nome, entrega, cidade="Dourados", fonte="courier", data=format_date( date.today() ), 
  pdf_template={"orientation": "P", "unit": "mm", "format": "A4"}, src_files_type=".java", build_file="src", course_number=2):
    self.pdf = FPDF(pdf_template["orientation"], pdf_template["unit"], pdf_template["format"])
    self.nome = nome
    self.entrega = entrega
    self.cidade = cidade
    self.fonte = fonte
    self.data = data
    self.src_files = src_files_type
    self.build_file = build_file
    roman_numbers = "I", "II", "III"
    self.course_number = roman_numbers[course_number-1]

  def new_line(self):
    self.pdf.cell(WIDTH, HEIGHT, f"", align=ALIGN, ln=True)

  def insert_prints(self):
    images_dictio = {}

    for root, dirs, files in walk(f".{sep}input{sep}prints", topdown=False):
      for file_ in files:
        images_dictio[file_] = path.join(root, file_)

    images_dictio = sort_dictio_keys(images_dictio)

    for value in images_dictio.values():
      self.pdf.image(value, w=180, h=101.2)
      self.new_line()

  def read_sql(self):
    files = listdir(f".{sep}input")
    for file_ in files:
      if(file_.endswith(".sql")):
        f = open(f".{sep}input{sep}{file_}")
        lines = f.readlines()
        f.close()
        return lines
      
    return []

  def insert_sql(self):
    lines = self.read_sql()
    self.pdf.set_font(self.fonte, "", 9)

    for line in lines:
      self.pdf.cell(WIDTH, HEIGHT, line, align=ALIGN, ln=True)
    
    self.new_line()
    self.pdf.set_font(self.fonte, "", 12)

  def read_and_insert_source_file(self, filepath):
    f = open(filepath, "r")
    filename = path.basename(f.name).replace(self.src_files, "")
    lines = f.readlines()
    
    self.pdf.cell(WIDTH, HEIGHT, f"Módulo: {filename}", align=ALIGN, ln=True)
    self.pdf.set_font(self.fonte, "", 9)

    for line in lines:
      self.pdf.cell(WIDTH, HEIGHT, line, align=ALIGN, ln=True)

    self.new_line()
    self.new_line()
    self.pdf.set_font(self.fonte, "", 12)
    f.close()

  def insert_sources(self):

    for root, dirs, files in walk(f".{sep}input{sep}src", topdown=False):
      for file_ in files:
        if(file_.endswith(self.src_files)):
          self.read_and_insert_source_file(path.join(root, file_))
      
      for dir_ in dirs:
        pass

  def build(self):
    file_name = output_path(self.build_file + ".pdf")

    self.pdf.add_page()
    self.pdf.set_auto_page_break(auto=True, margin=15)
    self.pdf.set_font(self.fonte, "", 12)

    self.pdf.cell(WIDTH, HEIGHT, f"Linguagem de Programação {self.course_number} - {self.entrega} - {self.nome}", align=ALIGN, ln=True)
    self.new_line()

    if self.build_file == "prints":
      self.insert_prints()
    elif self.build_file == "sql":
      self.insert_sql()
    else:
      self.insert_sources()

    self.new_line()
    self.pdf.cell(WIDTH, HEIGHT, f"{self.cidade}, {self.data}", align=ALIGN)

    # se a assinatura nao ficar alinhada, modifique os valores x e y aqui
    self.pdf.image("./input/assinatura.png", w=50, h=20, x=140, y=self.pdf.get_y()-5)

    self.pdf.output(file_name)
