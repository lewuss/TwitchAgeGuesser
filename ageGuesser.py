# zgadywanie wieku widza
# zapytać xD
# 0. Potencjalny rocznik w nicku (ważne)
# 13 w nicku
#   a) 2013 urodzony (nielegalny) wiec ta odpada xD
#   b) 13 jak zakładałeś konto - wiek = 2022 - Data_konta + 13
#   c) napisałeś 13 przez przyadek
#   d) to twoje 13 konto bo dostałeś 12 permów
# 1. wiek konta
# 2. watchtime - kogo ogląda
# wiek 13-17:
#   ewroon, kasix, kubax, fortnite, miszel, XI nowicjusze, yfl
# wiek 18-23:
#   delordione, franio, szymek, ja, arquel, slayprox, gucio, demonz
# wiek 23+
#   rock, izak, gluhamer, overpow, indystarcraft, blackfireice, jakis cs, dmajszi, isamu, saju
import api
import requests
import json
import re
from datetime import datetime

kids = ['ewroon', 'kasix', 'kubx', 'miszel', 'xth0rek', 'diables', 'matek', 'jacob4tv', 'qlnek', 'kamifn1', 'setty__',
        'advisefn', 'xayoo_', 'popo', 'japczan', 'holak1337', 'vysotzky', 'dejvid_tibijski_zadymiarz', 'lukisteve',
        'mlodziutki7', 'youngmulti', 'smerftv_', 'pisicela', 'grendy', 'tiger_scot', '1wron3k', 'sinmivak', 'DMGPOLAND',
        'nieuczesana']
teens = ['delordione', 'franio', 'szymoool', 'lewus', 'arquel', 'slayproxx', 'h2p_gucio', 'demonzz1', 'zony',
         'rybsonlol_', 'vvarion', 'cinkrofwest', 'polsatgames', 'xmerghani', 'xntentacion', 'kaseko', 'ortis',
         'mandzio', 'furazek', 'mrdzinold', 'sandrulaax', 'szzalony', 'mork','randombrucetv','tyrisftw','mokrysuchar'
                                                          'kozok', 'xype1337', 'zeekxd', 'playboistarki']
dinozaurs = ['rockalone', 'izakooo', 'gluhammer', 'borys8', 'mkrr3', 'bixentehs', 'blackfireice', 'bonkol', 'saju',
             'pago3', 'roocket__', 'overpow', 'kubon_', 'aikoiemil', 'janusz0821', 'indystarcraft', 'dmajszi',
             'esl_csgo_pl', 'kezman22',
             'kamileater', 'chesscompl', 'dawidczerw', 'gmhikaru', 'rajonesports', 'gmpakleza', 'jaskol95',
             'jacexdowozwideo', 'grabagra']


def guess_age(user):
    account_age = 2022 - int(api.user_info(user)['data'][0]['created_at'][:4])
    numbers = re.findall('\d+', user)
    # Patterny 70-99, 00-09
    for number in numbers:
        if number in ['420', '69', '2137', '1337', '2115']:
            return account_age + 13
        elif 1970 < int(number) < 2009:
            return datetime.now().year - int(number)
        elif len(number) == 2 and "09" >= number >= "00":
            return datetime.now().year % 100 - int(number)
        elif len(number) == 2 and "99" >= number >= "80":
            return datetime.now().year - int(number) - 1900

    url = f'https://vislaud.com/api/chatter/{user.lower()}'
    response = requests.get(url).json()
    watchtimes = sorted(response['watchtimes'], key=lambda k: k['watchtime'], reverse=True)
    kid_num = 0
    teen_num = 0
    dinozaur_num = 0

    for i, streamer in enumerate(watchtimes):
        if streamer['streamer']['displayName'].lower() in kids:
            kid_num += streamer['watchtime']
        elif streamer['streamer']['displayName'].lower() in teens:
            teen_num += streamer['watchtime']
        elif streamer['streamer']['displayName'].lower() in dinozaurs:
            dinozaur_num += streamer['watchtime']
        if i == 15:
            break
    watchtime_all = kid_num + teen_num + dinozaur_num
    starting_age = 10 + account_age + 2 * (kid_num / watchtime_all) + 4 * (teen_num / watchtime_all) + 8 * (
            dinozaur_num / watchtime_all)
    return starting_age


print(guess_age('Matosh88'))
