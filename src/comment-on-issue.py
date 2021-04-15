from jira import JIRA
from pydantic import AnyHttpUrl, BaseSettings, SecretStr


class Settings(BaseSettings):
    class Config:
        env_prefix = "INPUT_"

    JIRA_USERNAME: str
    JIRA_PASSWORD: SecretStr
    JIRA_BASE_URL: AnyHttpUrl

    ISSUE_KEY: str
    ISSUE_COMMENT_TEXT: str


settings = Settings()

jira = JIRA(
    settings.JIRA_BASE_URL,
    auth=(settings.JIRA_USERNAME, settings.JIRA_PASSWORD.get_secret_value()),
)

issue = jira.issue(settings.ISSUE_KEY)
jira.add_comment(issue, settings.ISSUE_COMMENT_TEXT)
print(f"Comment added to issue {settings.ISSUE_KEY}")
