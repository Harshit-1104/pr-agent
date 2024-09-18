import time
from pr_agent.log import get_logger
import requests
from typing import List

TABLE_NAME = "pr_feedback_agent"
ZOMATO_URL = "https://www.zomato.com/"
JUMBO_PUBLIC_URL = "https://jumbo.zomato.com/event"

class PRAgentEvent:
    def __init__(
        self,
        comment_url: str = "",
        feedback_author: str = "",
        agent_comment: str = "",
        feedback: str = "",
        diff_language: str = "",
        reflection_score: int = -1,
        reflection_comment: str = "",
    ):
        self.comment_url = comment_url
        self.feedback_author = feedback_author
        self.agent_comment = agent_comment
        self.feedback = feedback
        self.diff_language = diff_language
        self.reflection_score = reflection_score
        self.reflection_comment = reflection_comment

    def set_comment_url(self, comment_url):
        self.comment_url = comment_url
    
    def set_feedback_author(self, feedback_author):
        self.feedback_author = feedback_author
    
    def set_agent_comment(self, agent_comment):
        self.agent_comment = agent_comment
        
    def set_feedback(self, feedback):
        self.feedback = feedback

    def set_diff_language(self, diff_language):
        self.diff_language = diff_language

    def set_reflection_score(self, reflection_score):
        self.reflection_score = reflection_score

    def set_reflection_comment(self, reflection_comment):
        self.reflection_comment = reflection_comment


tracking_object: List[PRAgentEvent] = []
def get_tracking_object() -> List[PRAgentEvent]:
    return tracking_object

class PRAgentEventTracking:
    def to_event(self):
        return {
            "event_name": "EVENT_NAME_PUBLISH_COMMENT",
            "comment_url": self.comment_url,
            "feedback_author": self.feedback_author,
            "agent_comment": self.agent_comment,
            "feedback": self.feedback,
            "diff_language": self.diff_language,
            "reflection_score": self.reflection_score,
            "reflection_comment": self.reflection_comment,
        }

    def get_jumbo_header(self):
        return {
            "timestamp": int(time.time()),
            "user_id": "",
            "device_id": "",
            "ip_address": "",
            "user_agent": "",
            "session_id": "",
        }

    def publish_event(self):
        app_payload = {
            "app_payload": {
                "header": self.get_jumbo_header(),
                "payload": self.to_event(),
            }
        }

        headers = {
            'Content-Type': 'application/json',
            'Origin': 'https://www.zomato.com/',
            'Referer': 'https://www.zomato.com/'
        }

        response = requests.post(JUMBO_PUBLIC_URL, json=app_payload, headers=headers)
        if response.status_code == 200:
            get_logger().info('Successfully published data to jumbo:', response.json())
        else:
            get_logger().info(f"Failed to publish data with status code {response.status_code}")