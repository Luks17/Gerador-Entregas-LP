
from create_page import Project
from zip_project import zip_project


def extra_builds(username, task_name, number, src_files_type, build_type):
  project_sql = Project(username, task_name, build_file=build_type, course_number=number, src_files_type=src_files_type)
  project_sql.build()


def main():
  print("\nANTES DE CONTINUAR, COLOQUE AS PASTAS: \n<src> (OBRIGATORIO) \n<prints> (OBRIGATORIO) \n<xhtml> (LP3) \n<css> (LP3) " + 
        "\nE O ARQUIVO <.sql> (LP2++)\nE SUA ASSINATURA <assinatura.png> \nDENTRO DE INPUTS\n\n")
  print("Verifique tambem que seus prints tenham um aspecto 16:9 e sua assinatura um aspecto 4:9")
  username = input("Nome completo: ")
  task_name = input("Nome da entrega (Entrega 1, Entrega 2, Lista de Exercicios, etc): ")
  number = int(input("Vc esta em qual linguagem de programacao?\n[1] para LP1\n[2] para LP2\n[3] para LP3\n\n> "))
  has_sql_str = input("Sua entrega inclui sql? [Sim/Nao]\n")

  has_sql = has_sql_str.strip().capitalize()[0] == "S"
  has_xhtml = True if number == 3 else False
  has_css = True if number == 3 else False

  # se estiver em linguagem de programacao I, ele ira procurar por sources python, senao ira procurar por sources java
  src_files_type = ".py" if number == 1 else ".java"

  project_src = Project(username, task_name, course_number=number, src_files_type=src_files_type)
  project_src.build()

  project_prints = Project(username, task_name, build_file="prints", course_number=number, src_files_type=src_files_type)
  project_prints.build()

  if(has_sql):
    extra_builds(username, task_name, number, src_files_type, "sql")

  if(has_css):
    extra_builds(username, task_name, number, src_files_type, "css")

  if(has_xhtml):
    extra_builds(username, task_name, number, src_files_type, "xhtml")

  zip_project(has_css, has_xhtml)

  print("Se a assinatura não ficar alinhada, você pode dar uma olhada no arquivo create_page.py no método build e mudar a posição")

if __name__ == "__main__":
  main()
