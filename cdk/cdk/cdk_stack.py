from constructs import Construct
from aws_cdk import (
    Duration,
    Stack,
    aws_s3 as s3,
    aws_s3_deployment as s3deploy
)
import aws_cdk as cdk


class CdkStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        website_bucket = s3.Bucket(self, "my-meme-game-david-2024",
                            removal_policy=cdk.RemovalPolicy.DESTROY,
                            auto_delete_objects=True,
                            public_read_access=True,
                            block_public_access=s3.BlockPublicAccess
                                (
                                    block_public_acls= False,
                                    block_public_policy=False,
                                    ignore_public_acls=False,
                                    restrict_public_buckets=False
                                ),
                            website_index_document='index.html'
                        )

        s3deploy.BucketDeployment(self, "DeployWebsite",
            sources=[s3deploy.Source.asset("../website")],
            destination_bucket=website_bucket
            )
