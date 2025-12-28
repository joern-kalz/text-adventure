import os

from aws_cdk import CfnOutput, Duration, Stack
from aws_cdk import aws_lambda as lambda_
from aws_cdk.aws_lambda_python_alpha import PythonFunction
from constructs import Construct


class TextAdventureLambdaStack(Stack):
    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        backend_lambda = PythonFunction(
            self,
            "GameBackendFunction",
            entry="../app",
            index="lambda_handler.py",
            handler="handler",
            runtime=lambda_.Runtime.PYTHON_3_12,
            environment={
                "GROQ_API_KEY": os.getenv("GROQ_API_KEY", ""),
            },
            timeout=Duration.seconds(30),
            memory_size=512,
        )

        fn_url = backend_lambda.add_function_url(
            auth_type=lambda_.FunctionUrlAuthType.NONE,
            cors=lambda_.FunctionUrlCorsOptions(
                allowed_origins=["*"],
                allowed_methods=[lambda_.HttpMethod.ALL],
                allowed_headers=["*"],
            ),
        )

        CfnOutput(self, "ApiUrl", value=fn_url.url)
