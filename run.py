import boto3
import os
from cashflower import run, parse_arguments
from io import StringIO
from settings import settings


if __name__ == "__main__":
    output, diagnostic, log = run(settings=settings, path=os.path.dirname(__file__))
    args, unknown = parse_arguments()
    filename = unknown[1]

    # Upload to S3 bucket
    s3_client = boto3.client('s3')
    csv_buffer = StringIO()
    output.to_csv(csv_buffer, index=False)
    s3_client.put_object(
        Bucket="actuhub-dev",
        Key=f"{filename}",
        Body=csv_buffer.getvalue()
    )
