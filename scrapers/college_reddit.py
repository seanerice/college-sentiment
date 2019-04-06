import praw
import re, json
reddit = praw.Reddit(redirect_uri='http://localhost:8080',
                     user_agent='script by /u/PicassoAndPringles')

college_wiki = reddit.subreddit('college').wiki['faq'].content_md
links = [x.strip() for x in ''.join(college_wiki.split('-------------------')[1:])
        .split('\n') if len(x) > 0 and x[0] == '[']

subreddits = [(re.search(r'\[(.*)\]', link).group(1).strip(), re.search(r'r/(\w*)', link).group(1)) for link in links]

comments = {}
for name, sub in subreddits:
    print(name)
    try:
        comments[name] = [c.body for c in reddit.subreddit(sub).comments(limit=500)]
    except:
        print("{} messed up".format(sub))

with open('college_comments.json', 'w') as f:
    json.dump(comments, f)
