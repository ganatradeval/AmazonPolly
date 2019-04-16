import boto3
import time

client = boto3.client('polly')
text = """
Write Your Text Here.
"""
bucket = 'test-polly-1234'

response = client.start_speech_synthesis_task(
	OutputFormat = 'mp3',
	OutputS3BucketName = 'test-polly-1234',
	Text=text,
	VoiceId='Kendra')
taskId = response['SynthesisTask']['TaskId']
print("TaskId: "taskId)

# Rename S3 Object. Otherwise it will be taskId.mp3
s3 = boto3.resource('s3')
time.sleep(30)		# Wait till file is converted
s3.Object(bucket,'Baltagul.mp3').copy_from(CopySource='{}/{}.mp3'.format(bucket,taskId))
s3.Object(bucket,'{}.mp3'.format(taskId)).delete()    
