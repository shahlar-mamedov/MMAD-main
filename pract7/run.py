from bs4 import BeautifulSoup as bs
import requests as rq

url = rq.get('https://habr.com/ru/post/509082/')
doc = bs(url.text, 'html.parser')

name = doc.select(".post__title-text")[0].decode_contents().strip()
author = doc.select('.user-info__fullname')[0].decode_contents().strip()
date = doc.select('.post__time')[0].decode_contents().strip()
viws = doc.select('.post-stats__views-count')[0].decode_contents().strip()

print('Название статьи:', name)
print('Автор:', author)
print('Дата публикации:', date)
print('Кол-во просмотров:', viws)

comments = []
for node in doc.select('.comment'):
    text = node.select('.comment__message')[0].decode_contents().strip()
    author = node.select('.user-info__nickname_comment')[0].decode_contents().strip()
    votes = node.select('span.voting-wjt__counter')[0].decode_contents().strip()
    comments.append({'author': author, 'text': text, 'votes' : votes})

print('\nКомментариев в статье:', len(comments))
print('\nСамый маленький комментарий:', sorted(comments, key=lambda x: len(x['text']))[0]['text'])
print()
low_votes = sorted(comments, key=lambda x: x['votes'], reverse=True)[0]
print('Комментарий с самым низким рейтингом:\n', 'Автор: ' + low_votes['author'], '\nКомментарий: ' + low_votes['text'], '\nРейтинг: ', low_votes['votes'])

print()
low_votes = sorted(comments, key=lambda x: x['votes'], reverse=False)[0]
print('Комментарий с самым высоким рейтингом:\n', 'Автор: ' + low_votes['author'], '\nКомментарий: ' + low_votes['text'], '\nРейтинг: ', low_votes['votes'])
