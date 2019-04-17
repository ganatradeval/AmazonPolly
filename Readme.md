# Polly Text-to-Speech
This will a demonstration of Amazon Polly which converts your given text file into Speech. Strange thing is that it is almost free. Amazon doen't charges you to first 1 million words. 
Just follow steps and I will guide you to that.

## Prerequisites
* Little knowledge of AWS.
* Enthusiasm to learn.

## Input
- text: Just write some paragraph of whatever length. 
- Create one S3 bucket. (Give Amazon Polly permission to write in S3)([AWS Doc](https://docs.aws.amazon.com/polly/latest/dg/asynchronous-iam.html))
- Select your favourite voice for given language as input. ([Voice List](https://docs.aws.amazon.com/polly/latest/dg/voicelist.html))
- rename: Destination file name in S3 bucket.

## Steps to run
1. Install boto3
```
pip install boto3
```
2. Install AWS CLI and configure credentials
```
aws configure
```
OR
put below code into  ~/.aws/credentials
```
[default]
aws_access_key_id = YOUR_ACCESS_KEY
aws_secret_access_key = YOUR_SECRET_KEY
region=us-east-1
```
3. Create S3 bucket and Create Role for Polly [AWS Doc](https://docs.aws.amazon.com/polly/latest/dg/asynchronous-iam.html)
4. Clone https://github.com/ganatradeval/AmazonPolly.git.
5. Specify variables in polly.py file.
6. Run following.
```
cd AmazonPolly
python polly.py
```
# What next!
- Put this script in loop with number of your text files. and you will receive all files with desired name in S3 bucket.
- Large file to convert? Just increase sleep time.
