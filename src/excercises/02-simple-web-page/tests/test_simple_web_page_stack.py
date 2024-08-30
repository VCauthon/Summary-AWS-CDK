import aws_cdk as core
import aws_cdk.assertions as assertions

from simple_web_page.components import SimpleWebPage


def test_s3_bucket_exist():
    app = core.App()
    stack = SimpleWebPage(app, "simple-web-page")
    template = assertions.Template.from_stack(stack)

    # Check that the bucket with the static content exists
    template.resource_count_is("AWS::S3::Bucket", 1)
