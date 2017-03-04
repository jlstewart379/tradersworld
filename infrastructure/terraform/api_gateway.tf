resource "aws_api_gateway_rest_api" "invoke_tests" {
  name = "invoke_tests"
  description = "Invoke the codebuild tests"
}

resource "aws_api_gateway_resource" "invoke_tests_resource" {
  rest_api_id = "${aws_api_gateway_rest_api.invoke_tests.id}"
  parent_id = "${aws_api_gateway_rest_api.invoke_tests.root_resource_id}"
  path_part = "invoke_tests"
}

resource "aws_api_gateway_method" "invoke_tests_post" {
  rest_api_id = "${aws_api_gateway_rest_api.invoke_tests.id}"
  resource_id = "${aws_api_gateway_resource.invoke_tests_resource.id}"
  http_method = "POST"
  authorization = "NONE"
}

resource "aws_api_gateway_integration" "invoke_tests_integration" {
  rest_api_id = "${aws_api_gateway_rest_api.invoke_tests.id}"
  resource_id = "${aws_api_gateway_resource.invoke_tests_resource.id}"
  http_method = "${aws_api_gateway_method.invoke_tests_post.http_method}"
  credentials = "${aws_iam_user.codebuild_user.arn}"
  type = "AWS_PROXY"
}

resource "aws_api_gateway_method_response" "200" {
  rest_api_id = "${aws_api_gateway_rest_api.invoke_tests.id}"
  resource_id = "${aws_api_gateway_resource.invoke_tests_resource.id}"
  http_method = "${aws_api_gateway_method.invoke_tests_post.http_method}"
  status_code = "200"
}

resource "aws_api_gateway_deployment" "invoke_tests_deployment" {
  depends_on = ["aws_api_gateway_method.invoke_tests_post"]
  rest_api_id = "${aws_api_gateway_rest_api.invoke_tests.id}"
  stage_name = "prod"
}

resource "aws_lambda_permission" "apigw_lambda" {
  statement_id  = "AllowExecutionFromAPIGateway"
  action        = "lambda:InvokeFunction"
  function_name = "${aws_lambda_function.lambda.arn}"
  principal     = "apigateway.amazonaws.com"
  source_arn    = "arn:aws:execute-api:${var.myregion}:${var.accountId}:${aws_api_gateway_rest_api.invoke_tests.id}/*/${aws_api_gateway_method.invoke_tests_post.http_method}/${aws_api_gateway_resource.invoke_tests_resource.path_part}"
}

