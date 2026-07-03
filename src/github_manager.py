from github import Github
from github.PullRequest import PullRequest

class GitHubManager:
    """Handles interactions with the GitHub API to fetch PR details and post comments."""
    
    def __init__(self, token: str, repo_name: str, pr_number: int):
        self.gh = Github(token)
        self.repo = self.gh.get_repo(repo_name)
        self.pr: PullRequest = self.repo.get_pull(pr_number)

    def get_pr_diff(self) -> str:
        """Fetches the code changes (diff) of the pull request."""
        diffs = []
        for file in self.pr.get_files():
            if file.patch: # Only get files that have actual code changes
                diffs.append(f"File: {file.filename}\n{file.patch}")
        return "\n".join(diffs)

    def post_comment(self, review_text: str) -> None:
        """Posts the AI-generated review as a comment on the PR."""
        self.pr.create_issue_comment(review_text)