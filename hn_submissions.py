from matplotlib.pyplot import title
import requests
import json
from operator import itemgetter
from plotly.graph_objects import Bar
from plotly import offline

# Make an API call and store the response.
url = 'https://hacker-news.firebaseio.com/v0/topstories.json'
r = requests.get(url,) 
print(f"Status code: {r.status_code}")

# Process information about each submission.
submission_ids = r.json()
submission_dicts = []
for submission_id in submission_ids[:30]:
    try:
        url = f"https://hacker-news.firebaseio.com/v0/item/{submission_id}.json"
        r = requests.get(url)
        print(f"id: {submission_id}\tstatus: {r.status_code}")
        response_dict = r.json()

        # Build a dictionary for each article.
    
        submission_dict = {
            'title':response_dict['title'],
            'hn_link':f"http://news.ycombinator.com/item?id={submission_id}",
            'comments':response_dict['descendants'] 
        }
    except(KeyError):
        print(f'{submission_id} has no descendants and it\'s skipped')
        continue
    else:
        submission_dicts.append(submission_dict)
    


submission_dicts = sorted(submission_dicts, key=itemgetter('comments'),
                                    reverse=True)
n=1
titles , comments_number, links = [], [], []
for submission_dict in submission_dicts:
    #print(f"\n {n}-Title: {submission_dict['title']}")
    #print(f"Discussion link: {submission_dict['hn_link']}")
    #print(f"Comments: {submission_dict['comments']}")
    submission_title=submission_dict['title']
    submission_url=submission_dict['hn_link']
    submission_link = f"<a href='{submission_url}'>{submission_title}</a>"
    comments_number.append(submission_dict['comments'])
    links.append(submission_link)
    #n += 1

data = [{
    'type':'bar',
    'x': links,
    'y':comments_number,
    'marker':{
        'color':'rgb(176,164,223)',
        'line':{'color':'rgb(25,25,25)','width':1.5}
    },
    'opacity':0.6
}]
my_layout = {
    'title':'most recent stories on Hacker-news',
    'xaxis':{
        'title':'article',
        'titlefont':{'size':26},
        'tickfont':{'size':14}
        },
    'yaxis':{
        'title':'comments',
        'titlefont':{'size':26},
        'tickfont':{'size':14}
        }
}
fig = {'data':data, 'layout':my_layout}
offline.plot(fig,filename='hackers\' toparticles.html')
