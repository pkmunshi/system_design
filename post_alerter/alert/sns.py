import boto3

def send_sns_alert(subject: str, message: str, topic_arn: str):
    client = boto3.client('sns', region_name='us-east-2')
    try:
        response = client.publish(
                TopicArn=topic_arn,
                Subject=subject,
                Message=message
            )
        print(f"SNS alert sent successfully: {response}")
    except Exception as e:
        print(f"Error sending SNS alert: {e}")
        raise
    return response

if __name__ == "__main__":
    send_sns_alert("Test", "This is a test message", "arn:aws:sns:us-east-2:627754054200:daily_trades")
