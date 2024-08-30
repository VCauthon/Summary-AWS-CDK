from aws_cdk import Stack
from constructs import Construct

from simple_web_page.backend.host.infrastructure import StaticWebPageS3

class SimpleWebPage(Stack):
    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        bucket = StaticWebPageS3(self, "DatabaseService")
        print(bucket.bucket_website_url)
