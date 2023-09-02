import aws_cdk as core
import aws_cdk.assertions as assertions

from api_gw_python_example.api_gw_python_example_stack import ApiGwPythonExampleStack

# example tests. To run these tests, uncomment this file along with the example
# resource in api_gw_python_example/api_gw_python_example_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = ApiGwPythonExampleStack(app, "api-gw-python-example")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
