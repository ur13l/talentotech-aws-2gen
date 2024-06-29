import aws_cdk as core
import aws_cdk.assertions as assertions

from metadata_project.metadata_project_stack import MetadataStack

# example tests. To run these tests, uncomment this file along with the example
# resource in metadata_project/metadata_project_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = MetadataStack(app, "metadata-project")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
