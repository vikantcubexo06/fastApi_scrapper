import copy
import random

import requests
from bs4 import BeautifulSoup

from scrapper.model import ScrapperModel
from scrapper.serializer import ScrapperSerializer


def scrapdata():
    url = "https://www.sebi.gov.in/sebiweb/ajax/other/getintmfpiinfo.jsp"
    main_list_2 = []
    for to in range(10):
        # for to in range(int(996 / 25 +1)):
        payload = 'nextValue=4&next=n&intmId=16&contPer=&name=&regNo=&email=&location=&exchange=&affiliate=&alp=&doDirect=' + str(
            to) + '&intmIds='
        headers = {
            'Accept': '*/*',
            'Accept-Language': 'en-GB,en-US;q=0.9,en;q=0.8',
            'Connection': 'keep-alive',
            'Content-type': 'application/x-www-form-urlencoded',
            'Cookie': 'JSESSIONID=DF666AB6552C3B95E5A11E2CA0F270CC; _ga=GA1.3.1775389936.1657102153; _gid=GA1.3.1434386927.1657102153; JSESSIONID=29257ED968815FFB4EF47C4A5B520017',
            'Origin': 'https://www.sebi.gov.in',
            'Referer': 'https://www.sebi.gov.in/sebiweb/other/OtherAction.do?doRecognisedFpi=yes&intmId=16',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-origin',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36',
            'sec-ch-ua': '".Not/A)Brand";v="99", "Google Chrome";v="103", "Chromium";v="103"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"macOS"'
        }

        response1 = requests.request("POST", url, headers=headers, data=payload)

        s = BeautifulSoup(response1.text, "html.parser")

        h = s.findAll("div", attrs={"class": "fixed-table-body card-table"})
        main_list = []
        for index, data in enumerate(h):
            j = 0
            to_be_iterate = data.find("div").findAll("div", attrs={"class": "card-view"})
            to_be_added = {}
            to_be_added_with_reg = {}
            reg_key = ""
            for index1, i in enumerate(to_be_iterate):
                i = i.findAll("div")
                if i[0].text == "Registration No.":
                    to_be_added_with_reg[i[1].text] = {}
                    reg_key = i[1].text
                else:
                    to_be_added[i[0].text] = i[1].text
            if reg_key:
                to_be_added_with_reg[reg_key] = to_be_added
            main_list.append(to_be_added_with_reg)
        main_list_2 = [*main_list_2, *main_list]
    return main_list_2


def scrapCreation():
    """ mock data """
    # listData = []
    # for data in range(100):
    #     payload = {
    #         "registration_id": str(random.randint(300, 6745)),
    #         "Name": "fast" + str(random.randint(100, 89798)),
    #         "Address": "fastadd" + str(random.randint(100, 89798)),
    #         "Correspondence_Address": "fastccc" + str(random.randint(100, 89798)),
    #         "Validity": "fastvalidty" + str(random.randint(100, 89798)),
    #
    #     }
    #     createData = ScrapperModel.create(**payload)
    #     listData.append(payload)

    all_data = scrapdata()
    listData = []
    for data in all_data:

        dict_data = list(data.keys())[0]
        if dict_data:
            payload = {
                "registration_id": dict_data,
                "Name": data.get(dict_data).get("Name") if data.get(dict_data) else None,
                "Address": data.get(dict_data).get("Address") if data.get(dict_data) else None,
                "Correspondence_Address": data.get(dict_data).get("Correspondence_Address") if data.get(
                    dict_data) else None,
                "Validity": data.get(dict_data).get("Validity") if data.get(dict_data) else None,

            }
            createData = ScrapperModel.create(**payload)
            listData.append(payload)

    return {"msg": "data created successfully"}


#

def scrapperdetails(id: int):
    data = ScrapperModel.getdetails(id=id)
    data_dict = copy.deepcopy(data.__dict__)
    return ScrapperSerializer(**data_dict)
