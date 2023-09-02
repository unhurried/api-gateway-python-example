import aws_cdk as cdk
from constructs import Construct
from aws_cdk import (aws_apigateway as apigateway,
                     aws_s3 as s3,
                     aws_lambda as lambda_)

class WidgetService(Construct):
    def __init__(self, scope: Construct, id: str):
        super().__init__(scope, id)

        layer = lambda_.LayerVersion(
                self, "MyLayer",
                code=lambda_.Code.from_asset("lambda_layer"),
                compatible_runtimes=[lambda_.Runtime.PYTHON_3_11])

        handler = lambda_.Function(
                self, "WidgetHandler",
                runtime=lambda_.Runtime.PYTHON_3_11,
                code=lambda_.Code.from_asset("resources"),
                handler="handler.handler",
                layers=[layer])

        api = apigateway.RestApi(self, "widgets-api",
                  rest_api_name="Widget Service",
                  description="This service serves widgets.")

        get_widgets_integration = apigateway.LambdaIntegration(handler,
                request_templates={"application/json": '{ "statusCode": "200" }'})

        api.root.add_method("GET", get_widgets_integration)   # GET /