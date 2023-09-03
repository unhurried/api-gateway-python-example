import aws_cdk as core
import aws_cdk.assertions as assertions

from backend_example_serverless_python.backend_example_severless_python_stack import BackendExampleServerlessPythonStack

# example tests. To run these tests, uncomment this file along with the example
# resource in api_gw_python_example/api_gw_python_example_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = BackendExampleServerlessPythonStack(app, "backend-example-serverless-python")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
