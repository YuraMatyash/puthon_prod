import copy
from datetime import date

def get_weekday():
    return date.today().strftime('%A')

def get_month(post, weekday=get_weekday()):
    post_copy = post.copy()
    post_copy['on_weekday'] = weekday
    return post_copy


instal_post = {
    'id': 322,
    'athor' : 'Yura',
}
instal_post = get_month(instal_post)
print(instal_post)