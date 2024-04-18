import * as cdk from "aws-cdk-lib";
import * as s3 from "aws-cdk-lib/aws-s3";
import * as s3deploy from "aws-cdk-lib/aws-s3-deployment";

export class UiAppDeploymentStack extends cdk.Stack {
  constructor(scope: cdk.App, id: string, props?: cdk.StackProps) {
    super(scope, id, props);

    // Create a new S3 bucket to hold the UI application
    const bucket = new s3.Bucket(this, "UiAppBucket", {
      websiteIndexDocument: "index.html",
      publicReadAccess: true,
      removalPolicy: cdk.RemovalPolicy.DESTROY, // Automatically delete bucket when the stack is deleted
    });

    // Deploy files from the local 'build' directory to the S3 bucket
    new s3deploy.BucketDeployment(this, "DeployUiApp", {
      sources: [s3deploy.Source.asset("./../ui/.output/public")],
      destinationBucket: bucket,
    });

    new cdk.CfnOutput(this, "SiteURL", {
      value: bucket.bucketWebsiteUrl,
      description: "The URL of the website",
    });
  }
}

const app = new cdk.App();
new UiAppDeploymentStack(app, "UiAppDeploymentStack", {
  env: {
    region: process.env.AWS_REGION,
  }, // specify your preferred AWS region
});
