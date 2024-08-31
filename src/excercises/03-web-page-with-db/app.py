#!/usr/bin/env python3
import os

import aws_cdk as cdk

from web_page_with_db.web_page_with_db_stack import WebPageWithDbStack


app = cdk.App()
WebPageWithDbStack(app, "WebPageWithDbStack")

app.synth()
