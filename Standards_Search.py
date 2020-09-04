# This is the link to use to get a list of the standards all on one page
## https://shop.bsigroup.com/SearchResults/?q=bs+5266&pg=1&no=100&c=100&t=p

import requests
from bs4 import BeautifulSoup
import re
import os
import pdfplumber


class Standards_Search_Tools:
    #defining constructor
    def __init__(self, filePath):
        self.file_path = filePath


    def return_list_of_standards(self, standard_name):
        URL = f"https://shop.bsigroup.com/SearchResults/?q={standard_name}&pg=1&no=100&c=20&t=p"
        page = requests.get(URL)
        soup = BeautifulSoup(page.content, 'html.parser')
        results = soup.find(id='MainFrame')
        standards_lists = results.find_all('div', class_='resultsInd')
        results_list = []
        for _ in standards_lists:
            title_name = _.find('h2', class_='H2SearchResultsTitle')
            title_status = _.find('span', class_='text12Grey')
            results_list.append(_.text.strip())
        returned_list = []
        for _ in results_list:
            formatted_text = _.replace("  ", "")
            formatted_text = formatted_text.replace("\n\n", "\n")
            formatted_text = formatted_text.replace("\r\n", "")
            formatted_text = formatted_text.replace("\xa0", " ")
            formatted_text = formatted_text.strip('\r')
            output_list = []
            for item in formatted_text.splitlines():
                output_list.append(item)
            output_list[:] = [x for x in output_list if x]
            returned_list.append(output_list)
        return returned_list


    def text_search_for_standards(self, input_text):
        #regex = r"(BS|BS |BS EN|EN|EN |ISO|ISO |IEC|IEC |BSRIABG |DW)\d+"
        regex = r"(BS|BS EN|EN|ISO|IEC|BSRIABG|DW) ?\d+"
        matches = re.finditer(regex, input_text, re.MULTILINE)
        list_of_standards_in_text = []
        for matchNum, match in enumerate(matches, start=1):
            list_of_standards_in_text.append(match.group())
        print(list_of_standards_in_text)
        list_of_standards_in_text = list(set(list_of_standards_in_text))
        return list_of_standards_in_text


    def extract_text_from_pdf(self):
        with pdfplumber.open(self.file_path) as pdf:
            full_text = ""
            pages = pdf.pages
            for i, pg in enumerate(pages):
                text = pages[i].extract_text()
                full_text += text
            #first_page = pdf.pages[0]
            #print(first_page.extract_text())
            #print(full_text)
        return full_text


    def write_to_file(self, document_to_write):
        filename_to_write = f"{self.file_path}.txt"
        with open(filename_to_write, 'w', encoding="utf-8") as standards_review_doc:
            standards_review_doc.write("Summary of Standards:")
            standards_review_doc.write("""

            """)
            standards_review_doc.write(document_to_write)


