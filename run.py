import boto3
import os
from cashflower import run, parse_arguments
from io import StringIO
from settings import settings


if __name__ == "__main__":
    output, diagnostic, log = run(settings=settings, path=os.path.dirname(__file__))
    args, unknown = parse_arguments()
    output_filename = unknown[1]
    diagnostic_filename = unknown[3]

    # S3 bucket and buffers
    s3_client = boto3.client('s3')

    buffer1 = StringIO()
    buffer2 = StringIO()

    output.to_csv(buffer1, index=False)
    diagnostic.to_csv(buffer2, index=False)

    # Upload to S3
    s3_client.put_object(Bucket="actuhub-dev", Key=f"{output_filename}", Body=buffer1.getvalue())
    s3_client.put_object(Bucket="actuhub-dev", Key=f"{diagnostic_filename}", Body=buffer2.getvalue())
