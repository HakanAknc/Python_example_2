# coding=utf-8

import feedparser

"""
    ligtv haberleri feed ile ayrıştırma
    Öncelikle feedparser modülünü indirip kurmanız gerekli
    Terminalde  pip install feedparser  yapıp çalıştırsanız yeterli olacaktır
"""

print('''
    ######################################
    #                                    #
    #    Ligtv Besiktaş Haberleri     #
    #                                    #
    ######################################
''')
haberler_besiktas = feedparser.parse('https://beinsports.com.tr/rss/takim/besiktas')

i = 1
for haber in haberler_besiktas.entries:
    print(i, haber.title)
    print("  ", haber.guid, "\n")
    i += 1