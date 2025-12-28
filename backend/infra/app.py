import aws_cdk as cdk
from stack import TextAdventureLambdaStack

app = cdk.App()

TextAdventureLambdaStack(app, "TextAdventureLambdaStack")

app.synth()
