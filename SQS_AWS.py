import boto3
import json
import time
import random

# create SQS client
sqs = boto3.client('sqs')

# create a new SQS queue
queue_name = 'md-queue'
response = sqs.create_queue(QueueName="md-queue")
queue_url = response['QueueUrl']