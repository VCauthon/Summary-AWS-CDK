#!/usr/bin/env python3
import aws_cdk as cdk

from simple_web_page.components import SimpleWebPage


app = cdk.App()
SimpleWebPage(app, "SimpleWebPageStack")

app.synth()
