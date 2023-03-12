import boto3
aws_resource = boto3.resource("s3")
bucket  = aws_resource.Bucket("ayaats3")
response = bucket.create(
    ACL = 'private-read',
    CreateBucketConfiguration={
        'LocationConstraint':'us-west-2'
    },

)

print(response)