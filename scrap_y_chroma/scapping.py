"""
Scrapper para sacar informacion de los HTML de la wiki de Pyar, para alimentar el buscador semantico (vectores embebidos) con chromaDB
"""

import bs4
import os, csv


class Scrapper:
  def scrap_output_folders(self) -> None:
    folders = os.walk('output')

    ouput_csv = open('url_content_searchbar.csv', 'w')
    csv_writer = csv.writer(ouput_csv, delimiter=';')
    csv_writer.writerow(['TITLE', 'URL'])
    for file in folders:
      path = file[0]
      
      if len(file) == 3:
        try:
          #htmls validos dentro de las carpetas de output
          folder_html = file[2][0]
          
          html = path+ '/' +folder_html

          url = path.split('/')[-1]

          with open(html, 'r') as file:
            bs = bs4.BeautifulSoup(file)
            try:
              title = bs.find('h2').get_text()

              csv_writer.writerow([title, url])

            except Exception as e:
              pass

        except Exception as e:
          pass
        #

    ouput_csv.close()

if __name__ == '__main__':
  scrapper = Scrapper()
  scrapper.scrap_output_folders()

  """
  TODO implementar la creacion de la base de datos de chroma
  """










