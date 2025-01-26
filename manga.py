import requests, os, bs4, re



url = input('(download will start from current url \n'
            'to the last chapter you can stop any time\nprevious downloaded chapter won\'t be deleted)\n'
            'paste the link of the manga from ANIMELEK with "/" at the end: \n')


# fct that download all pages from
def downloadMangaFromSinglePage(imageLinks:list, folder_number:int):
    os.makedirs(f'manga {folder_number}', exist_ok=True)
    for link in imageLinks:
        imageFile = open(os.path.join(f'manga {folder_number}', os.path.basename(link)), 'wb')
        response = requests.get(link)
        for chunk in response.iter_content(100000):
            imageFile.write(chunk)
        imageFile.close()

def goToNextPage():
    prevLink = soup.select('div.nav-next a')[0]
    return prevLink.get('href')
# check if link doesn't end with /number/
def ends_with_number(string):
    regex1 = r"/\d+/$"
    regex2 = r"/\d+-\d/$"
    return bool(re.search(regex1 + "|" + regex2 + "$", string))



while ends_with_number(url):
    print(f'Downloading chapter {url}...')
    res = requests.get(url)
    if res.status_code != 200:
        print('Something went wrong downloading')
        break

    soup = bs4.BeautifulSoup(res.text, 'html.parser')

    # TODO : Find URL of the comic image
    imageElem = soup.select('div.page-break.no-gaps img')

    links = list(map(lambda x: x.get('src'), imageElem))
    downloadMangaFromSinglePage(links, url[-3:-1])
    url = goToNextPage()
