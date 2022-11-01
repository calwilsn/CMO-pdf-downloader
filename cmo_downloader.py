import os
import re
import requests
from bs4 import BeautifulSoup


def get_pdfs(url, folder_name):
    '''
    Download all PDFs from url and store them into a folder
    '''
    folder_path = os.path.join("")
    if not os.path.exists(folder_name):
        os.mkdir(folder_name) # Create "Math Problems" folder if it does not exist
    response = requests.get(url) # Gets response object from website
    parser = BeautifulSoup(response.text, 'html.parser') # Create parser for text of website
    links = parser.find_all('a') # Get all links from website
    pdfs = [link for link in links if '.pdf' in link.get('href', '')] # Exlude links from list that are not pdfs
    for link in pdfs: # Download pdfs to folder
        # Get name of PDF which is at end of URL made up of only letters, numbers, underscores, and hypens. Ends with '.pdf'
        name = re.findall(r'((?:\d|\w|\-|\_)+.pdf)', str(link))[0]
        # Some URLS were not correctly extracted by BeautifulSoup, so need to modify them to get correct URL
        try:
            response = requests.get(link.get('href'))
        except:
            response = requests.get('https://cms.math.ca/' + link.get('href'))
        path = os.path.join(folder_name, name) # get path to save pdf
        # Write pdfs to pathmame
        pdf = open(path, 'wb')
        pdf.write(response.content)
        pdf.close()
        
        

        
        
        
if __name__ == "__main__":
    get_pdfs('https://cms.math.ca/competitions/cmo/', 'Math Problems')