import unittest
from unittest import mock
from lambda_functions.invoke_tests import InvokeTestsHandler


class TestInvokeLambda(unittest.TestCase):

    @mock.patch('infrastructure.lambda.invoke_tests.boto3')
    def test_it_start_codebuild(self, mock_boto):
        sample_body = {'command': 'start'}
        handler = InvokeTestsHandler(sample_body)
        mock_client = mock.Mock()
        mock_boto.client.return_value = mock_client
        mock_client.start_build.assert_called_with(
            project='test_django_app',
            sourceVersion='master'
        )
