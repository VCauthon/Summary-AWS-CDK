import os

from aws_cdk import (
    aws_s3 as s3,
    RemovalPolicy,
    aws_s3_deployment as s3deploy
)

from constructs import Construct


class StaticWebPageS3(Construct):
    def __init__(self, scope: Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        bucket = s3.Bucket(self, 
            "MyStaticWebsiteBucket",
            website_index_document="index.html",
            website_error_document="error.html",
            public_read_access=True,
            removal_policy=RemovalPolicy.DESTROY,
            block_public_access=s3.BlockPublicAccess.BLOCK_ACLS,
            auto_delete_objects=True,
        )

        file_path = os.path.dirname(os.path.relpath(__file__))
        s3deploy.BucketDeployment(self, 
            "DeployWebsiteContent",
            sources=[s3deploy.Source.asset(os.path.join(file_path ,"webpage_content"))],
            destination_bucket=bucket,
        )

        # Output the bucket website URL
        self.bucket_website_url = bucket.bucket_website_url
