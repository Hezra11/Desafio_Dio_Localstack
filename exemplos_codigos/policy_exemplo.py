{
    "Version": "2012-10-17",
    "Id": "default",
    "Statement": [
        {
            "Sid": "AllowS3Invoke",
            "Effect": "Allow",
            "Principal": {
                "Service": "s3.amazonaws.com"
            },
            "Action": "lambda:InvokeFunction",
            "Resource": "arn:aws:lambda:regiao-da-aws:123456789012:function:nome-da-sua-funcao",
            "Condition": {
                "StringEquals": {
                    "AWS:SourceAccount": "123456789012"
                },
                "ArnLike": {
                    "AWS:SourceArn": "arn:aws:s3:::nome-do-seu-bucket"
                }
            }
        }
    ]
}
