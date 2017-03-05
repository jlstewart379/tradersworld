resource "aws_iam_user" "codebuild_user" {
    name = "codebuild-user"
}

resource "aws_iam_access_key" "lb" {
    user = "${aws_iam_user.codebuild_user.name}"
}

resource "aws_iam_user_policy" "lb_ro" {
    name = "test"
    user = "${aws_iam_user.codebuild_user.name}"
    policy = <<EOF
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Action": [
        "codebuild:BatchGetBuilds",
        "codebuild:BatchGetProjects",
        "codebuild:ListBuilds",
        "codebuild:ListBuildsForProject",
        "codebuild:ListProjects",
        "codebuild:StartBuild",
        "codebuild:StopBuild",
        "logs:CreateLogGroup",
        "logs:CreateLogStream",
        "logs:PutLogEvents",
        "lambda:InvokeFunction"
      ],
      "Effect": "Allow",
      "Resource": "*"
    }
  ]
}
EOF
}
