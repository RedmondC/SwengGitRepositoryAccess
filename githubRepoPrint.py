from github import Github
username = "phadej"
git = Github()
user = git.get_user(username)
commits = []
contents = []
for repo in user.get_repos():
    print(repo.full_name, "--")
    print("	Commits --")
    for commit in repo.get_commits():
        print("		", commit)
        commits.append(commit)

    print("	Contents --")
    content = repo.get_contents("")
    for content_file in content:
        print("		", content_file)
        contents.append(content_file)

print(len(commits), " <- commits || contents -> ", len(contents))
