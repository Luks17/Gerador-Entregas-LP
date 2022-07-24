
from create_page import Project
from zip_project import zip_project


def main():
  print("\nANTES DE CONTINUAR, COLOQUE AS PASTAS <src> (OBRIGATORIO) <prints> (OBRIGATORIO) E O ARQUIVO .sql (OPCIONAL) E SUA ASSINATURA <assinatura.png> DENTRO DE INPUTS\n\n")
  print("Verifique tambem que seus prints tenham um aspecto 16:9 e sua assinatura um aspecto 4:9")
  username = input("Nome completo: ")
  task_name = input("Nome da entrega (Entrega 1, Entrega 2, Lista de Exercicios, etc): ")
  number = int(input("Vc esta em qual linguagem de programacao? (1, 2 ou 3): "))
  has_sql = input("Sua entrega inclui sql? (Sim/Nao): ")

  # se estiver em linguagem de programacao I, ele ira procurar por sources python, senao ira procurar por sources java
  src_files_type = ".py" if number == 1 else ".java"

  project_src = Project(username, task_name, course_number=number, src_files_type=src_files_type)
  project_src.build()

  project_prints = Project(username, task_name, build_file="prints", course_number=number, src_files_type=src_files_type)
  project_prints.build()

  if(has_sql.startswith("S")):
    project_sql = Project(username, task_name, build_file="sql", course_number=number, src_files_type=src_files_type)
    project_sql.build()

  zip_project()

if __name__ == "__main__":
  main()
