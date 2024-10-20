import boto3
import base64
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from dotenv import load_dotenv
import os

# Configure your AWS credentials and S3 bucket name
AWS_ACCESS_KEY_ID = os.getenv('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = os.getenv('AWS_SECRET_ACCESS_KEY')
BUCKET_NAME = os.getenv('BUCKET_NAME')  
load_dotenv()

s3_client = boto3.client(
    's3',
    aws_access_key_id=AWS_ACCESS_KEY_ID,
    aws_secret_access_key=AWS_SECRET_ACCESS_KEY
)

def get_topic_icon_by_topic_name(image_key: str) -> str:
    """Retrieves an image from S3 and returns it as a base64-encoded string."""
    try:
        # Get the object from S3
        response = s3_client.get_object(Bucket=BUCKET_NAME, Key="topic_icon/"+image_key+"_icon.png")
        image_data = response['Body'].read()
        # Encode the image data to base64
        return base64.b64encode(image_data).decode('utf-8')
    except Exception as e:
        print(f"Error retrieving image from S3: {e}")
        return ""
