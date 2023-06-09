import google_play_scraper as gps

country = 'us'
lang = 'ko'
id = 'com.eland.kidslevel1'

result  = gps.reviews_all(
    id,
    sleep_milliseconds=2000,  # defaults to 0
    lang=lang,  # defaults to 'en'
    country=country,  # defaults to 'us'
    sort=gps.Sort.NEWEST,  # defaults to Sort.MOST_RELEVANT
    filter_score_with=None  # defaults to None(means all score)
)

f = open("후기.txt", 'w', encoding='utf-8')
print(result)
for i in result:
    data = f"'time' : {i['at']},'userName': {i['userName']}, 'score' : {i['score']}, 'text' : {i['content']}\n"
    print(data)
    f.write(data)
f.close()