from urllib.request import urlopen
import pickle
from bs4 import BeautifulSoup
import sys
import httplib2
from googleapiclient import discovery
from googleapiclient.errors import HttpError
import csv


def get_culpa(department):
    """
    get_culpa scrapes every text data on Culpa.info given a list of departments

    :param department: a dictionary of departments that we want to collect review data on
    :return culpa: a list of raw data retrieved from culpa.info
    """
    culpa = []
    for i in department:
        cs_page = urlopen("http://culpa.info/departments/{}".format(i))
        soup = BeautifulSoup(cs_page.read(), 'lxml')

        prof = soup.find("div", {"class": "leftcolumn"})
        profs = prof.find_all("li")

        for p in profs:
            print(p.text.strip())
            nugget = p.find("img")
            if nugget is not None:
                nugget = nugget.text
            else:
                nugget = "none"
            cs_page = urlopen("http://culpa.info/{}".format(p.find("a")['href']))
            soup2 = BeautifulSoup(cs_page.read(), 'lxml')
            reviews = soup2.find_all("div", {"class":"review box"})
            for review in reviews:
                try:
                    course_num = review.find("span", {"class": "course_number"}).text.strip()
                except AttributeError:
                    course_num = 'none'
                try:
                    course_name = review.find("span", {"class": "course_name"}).text.strip()
                except AttributeError:
                    course_name = 'none'
                try:
                    date = review.find("p", {"class": "date"}).text.strip()
                except AttributeError:
                    date = 'none'
                try:
                    text = review.find("div", {"class": "review_content"})
                    if text is not None:
                        paragraphs = text.find_all("p")
                        text = ''
                        for paragraph in paragraphs:
                            text += paragraph.text.strip()
                    else:
                        text = 'none'
                except AttributeError:
                    text = 'none'
                culpa.append([p.text.strip(), nugget, course_num, course_name, date, text])

    pickle.dump(culpa, open('data/culpa.p', 'wb'))
    return culpa


def test_language_api(content):
    """
    test_language_api creates a connection to Google Cloud NLP API and returns the result

    :param content: a text block that we want to analyze
    :return response: analyzed text formatted in dic
    """
    discovery_url = 'https://{api}.googleapis.com/$discovery/rest?version={apiVersion}'
    service = discovery.build(
        'language', 'v1',
        http=httplib2.Http(),
        discoveryServiceUrl=discovery_url,
        developerKey='YOUR_API_KEY',
    )

    service_request = service.documents().annotateText(
        body={
            'document': {
                'type': 'PLAIN_TEXT',
                'content': content,
            },
            'features': {
                'extract_syntax': False,
                'extractEntities': False,
                'extractDocumentSentiment': True,
            },
            'encodingType': 'UTF16' if sys.maxunicode == 65535 else 'UTF32',
        })

    try:
        response = service_request.execute()
    except HttpError as e:
        response = {'error': e}

    return response


def nlp_processing(culpa_data):
    """
    nlp_processing calls Google Cloud NLP API and average the scores for each Professor - Course pair

    :param culpa_data: raw culpa.info text data
    :return csv_list: a list of [Professor, Course, Rating]
    """
    for i in range(len(culpa_data)):
        result = test_language_api(culpa_data[i][5])
        culpa_data[i].append(result)

    pickle.dump(culpa_data, open('culpa.p', 'wb'))

    culpa_data = pickle.load(open("culpa.p", "rb"))

    csv_file = ['Professor', 'Course', 'Rating']
    average = {}

    for i in culpa_data:
        if i[0] == "Madigan, David" or i[0] == 'Papageorgiou, Anargyros ' or i[0]=='Servedio, Rocco':
            i[1] = "gold"
        elif i[1] == "":
            i[1] = "silver"
        nlp_part = i[6]['documentSentiment']
        score = nlp_part['magnitude'] * nlp_part['score']
        csv_file.append([i[0],i[1],i[2].replace("[", "").replace("]", ""), i[3], round(score,2)])

    for k in range(len(csv_file)):
        j = csv_file[k]
        if (j[0], j[2]) in average:
            score, times = average[(j[0], j[2])]
            average[(j[0], j[2])] = (score+j[4], times+1)

        else:
            average[(j[0], j[2])] = (j[4], 1)

    csv_list = []
    for i in average:
        score, times = average[i]
        prof, course = i
        csv_list.append([prof, course, round(score/times, 2)])
    return csv_list


def main():
    wanted_departments = {'7':'CS', '31':'STAT'}
    raw_data = get_culpa(wanted_departments)
    csv_list = nlp_processing(raw_data)

    with open('data/culpa.csv', 'w', encoding='utf-8') as csvfile:
        csvwriter = csv.writer(csvfile, quoting=csv.QUOTE_NONNUMERIC)
        for i in range(len(csv_list)):
            csvwriter.writerow(csv_list[i])
        csvfile.close()


if __name__ == "__main__":
    main()
