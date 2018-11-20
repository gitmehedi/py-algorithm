import requests, json, sys

baseURL = "https://api.bitbucket.org/2.0"
username = sys.argv[1]
top = int(sys.argv[2])
limit = int(sys.argv[3])
commitCount = 0
commits = []
pagelen = 10
repos = []
format_data = {}

repo = requests.get(
    "{base}/repositories/{teamname}?pagelen={pagelen}".format(base=baseURL, teamname=username, pagelen=pagelen)).json()
repos.extend(repo['values'])
while 'next' in repo:
    repo = requests.get("{next}".format(next=repo['next'])).json()
    repos.extend(repo['values'])

for repo in repos:
    c = requests.get(repo['links']['commits']['href'] + "?pagelen={pagelen}".format(pagelen=pagelen)).json()
    commits.extend(c['values'])
    length = len(c['values'])
    while 'next' in c and length <= limit:
        c = requests.get("{next}".format(next=c['next'])).json()
        commits.extend(c['values'])
        length = length + len(c['values'])

for commit in commits:
    reponame = commit['repository']['name']
    if 'user' in commit['author']:
        user = commit['author']['user']['username']
        if user not in format_data:
            format_data[user] = {'git_repos': {}, "total_commit_share_percentage": 0}
        if reponame not in format_data[user]["git_repos"]:
            format_data[user]["git_repos"][reponame] = 0

        format_data[user]["git_repos"][reponame] = format_data[user]["git_repos"][reponame] + 1
        format_data[user]["total_commit_share_percentage"] = format_data[user]["total_commit_share_percentage"] + 1
        commitCount = commitCount + 1

top_commit = sorted(((format_data[val]['total_commit_share_percentage'], val) for val in format_data), reverse=True)[:top]
results = {}
for key, val in top_commit:
    results[val] = format_data[val]
    results[val]['total_commit_share_percentage'] = round(
        (float(format_data[val]['total_commit_share_percentage']) / commitCount), 5)

print json.dumps({username: results})

