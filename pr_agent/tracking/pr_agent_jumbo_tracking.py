TABLE_NAME = "pr_feedback_agent"
ZOMATO_URL = "https://www.zomato.com/"

class PRFeedbackPayload:
    def __init__(
        self,
        comment_url: str = "",
        feedback_author: str = "",
        agent_comment: str = "",
        feedback: str = "",
        diff_language: str = "",
        reflection_score: int = -1,
        reflection_comment: str = ""
    ):
        self.comment_url = comment_url
        self.feedback_author = feedback_author
        self.agent_comment = agent_comment
        self.feedback = feedback
        self.diff_language = diff_language
        self.reflection_score = reflection_score
        self.reflection_comment = reflection_comment
    
    def to_event(self):
        return {
            "comment_url": self.comment_url,
            "feedback_author": self.feedback_author,
            "agent_comment": self.agent_comment,
            "feedback": self.feedback,
            "diff_language": self.diff_language,
            "reflection_score": self.reflection_score,
            "reflection_comment": self.reflection_comment
        }
        
    def get_jumbo_header(self):
        return {
            
        }