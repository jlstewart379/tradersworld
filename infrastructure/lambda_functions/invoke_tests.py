import boto3

class InvokeTestsHandler:

    def __init__(self, data):
        self.data = data
        self.client = boto3.client('codebuild', region_name='us-east-1')

    def invoke_tests(self):
        self.client.start_build(
            project='test-django-rest-app',
            sourceVersion='master'
        )


def lambda_handler(event, context):
    handler = InvokeTestsHandler(event['body'])
    handler.invoke_tests()
