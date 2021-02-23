#!/usr/bin/env python3

from aws_cdk import core

from sample_cdk_codepipeline.sample_cdk_codepipeline_stack import SampleCdkCodepipelineStack


app = core.App()
SampleCdkCodepipelineStack(app, "sample-cdk-codepipeline")

app.synth()
