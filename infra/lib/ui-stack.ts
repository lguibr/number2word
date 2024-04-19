import * as cdk from "aws-cdk-lib";
import * as s3 from "aws-cdk-lib/aws-s3";
import * as s3deploy from "aws-cdk-lib/aws-s3-deployment";
import * as iam from "aws-cdk-lib/aws-iam";

export class UiAppDeploymentStack extends cdk.Stack {
  constructor(scope: cdk.App, id: string, props?: cdk.StackProps) {
    super(scope, id, props);

    // Create a new S3 bucket to hold the UI application
    const bucket = new s3.Bucket(this, "UiAppBucket", {
      bucketName: `bucket-trellis-law-ui-adhoc`,
      websiteIndexDocument: "index.html",
      publicReadAccess: true,
      objectOwnership: s3.ObjectOwnership.OBJECT_WRITER,
      blockPublicAccess: new s3.BlockPublicAccess({
        blockPublicAcls: false,
        ignorePublicAcls: false,
        blockPublicPolicy: false,
        restrictPublicBuckets: false,
      }),
      lifecycleRules: [
        {
          abortIncompleteMultipartUploadAfter: cdk.Duration.days(7),
        },
      ],
      cors: [
        {
          allowedOrigins: ["*"],
          allowedMethods: [s3.HttpMethods.GET, s3.HttpMethods.HEAD],
          allowedHeaders: ["*"],
          exposedHeaders: [],
          maxAge: 3000,
        },
      ],
      removalPolicy: cdk.RemovalPolicy.DESTROY,
    });

    const public_policy = new iam.PolicyStatement({
      actions: ["s3:GetObject"],
      effect: iam.Effect.ALLOW,
      principals: [new iam.AnyPrincipal()],
      resources: [bucket.arnForObjects("*")],
    });

    bucket.addToResourcePolicy(public_policy);

    // Deploy files from the local 'build' directory to the S3 bucket
    new s3deploy.BucketDeployment(this, "DeployUiApp", {
      sources: [s3deploy.Source.asset("./../ui/.output/public/")],
      destinationBucket: bucket,
    });

    // Output the URL of the website
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
    account: process.env.AWS_ACCOUNT,
  },
});
