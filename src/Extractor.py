from github import Github

class Extractor:
    account = None
    pwd = None
    g = None
    url = None

    def __init__(self, p_account, p_pwd):
        self.account = p_account
        self.pwd = p_pwd
        self.g = Github(self.account, self.pwd)

    def extractIssueInSingleBase(self, repo):
        open_issues = repo.get_issues(state='open')
        for issue in open_issues:
            print(issue)
        return

    def extractSingleBase(self, url):
        self.url = url
        repo = self.g.get_repo(url)
        self.extractIssueInSingleBase(repo)
        return
