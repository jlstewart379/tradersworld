resource "aws_iam_role" "invoke_te" {
    name = "invoke_tests_lambda"
    assume_role_policy = <<EOF
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Resource": [
        "*"
      ],
      "Action": [
        "codebuild:StartBuild"
      ]
    }
  ]
}
EOF
}

resource "aws_lambda_function" "lambda" {
  filename = "invoke_tests.zip"
  function_name    = "invoke_tests"
  role             = "${aws_iam_role.codebuild_role.arn}"
  handler          = "invoke_tests.lambda_handler"
  runtime          = "python3.5"
  source_code_hash = "${base64sha256(file("invoke_tests.zip"))}"
}

