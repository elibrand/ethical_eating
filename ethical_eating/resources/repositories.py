import requests

genesis1 = requests.get("http://www.sefaria.org/api/texts/Genesis.1").json().get('text')
genesis9 = requests.get("http://www.sefaria.org/api/texts/Genesis.9").json().get('text')

isaiah11 = requests.get("http://www.sefaria.org/api/texts/Isaiah.11").json().get('text')

deut8 = requests.get("http://www.sefaria.org/api/texts/Deuteronomy.8").json().get('text')

hosea2 = requests.get("http://www.sefaria.org/api/texts/Hosea.2").json().get('text')


bible_sources = [
    f'{genesis1[28]} Genesis 1 29',
    f'{genesis1[29]} Genesis 1 30',
    f'{genesis9[3]} Genesis 9 4',
    f'{genesis9[8]} {genesis9[9]} Genesis 9 9-10',
    f'{deut8[6]} {deut8[7]} {deut8[8]} {deut8[9]} Deut. 8 7-10',
    f'{isaiah11[5].replace("<i></i>", "")} {isaiah11[6]} {isaiah11[7]} {isaiah11[8]} Isa. 11 6-9',
    f'{hosea2[19].replace("<i></i>", "")} Hosea 2 20',
]

