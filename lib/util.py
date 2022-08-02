
from os import path, sep, makedirs


def output_path(file_name):
  if not path.exists("output"):
    makedirs("output")

  file_name = f".{sep}output{sep}" + file_name

  return file_name


def format_date(date):
  day = date.day
  month = date.month
  year = date.year  

  day = "0" + str(day) if day < 10 else day
  month = "0" + str(month) if month < 10 else month

  return f"{day}/{month}/{year}"


def sort_dictio_keys(dictio):
  sorted_dictio = {}

  # sorted() ordena as chaves mas nao guarda os valores, logo eh preciso recuperar eles
  for key in sorted(dictio):
    sorted_dictio[key] = dictio[key]

  return sorted_dictio
