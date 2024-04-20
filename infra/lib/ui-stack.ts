import * as cdk from "aws-cdk-lib";
import * as s3 from "aws-cdk-lib/aws-s3";
import * as s3deploy from "aws-cdk-lib/aws-s3-deployment";
import * as iam from "aws-cdk-lib/aws-iam";
import * as cloudfront from "aws-cdk-lib/aws-cloudfront";
import * as origins from "aws-cdk-lib/aws-cloudfront-origins";
import * as acm from "aws-cdk-lib/aws-certificatemanager";

export class UiAppDeploymentStack extends cdk.Stack {
  constructor(scope: cdk.App, id: string, props?: cdk.StackProps) {
    super(scope, id, props);

    const bucket = new s3.Bucket(this, "UiAppBucket", {
      bucketName: "bucket-trellis-law-ui-adhoc",
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

    const certificateArn =
      "arn:aws:acm:us-east-1:019749023127:certificate/1cb041d3-bd8e-4dd2-9364-68fd8c76e0c3";
    const certificate = acm.Certificate.fromCertificateArn(
      this,
      "Certificate",
      certificateArn
    );

    const distribution = new cloudfront.Distribution(
      this,
      "UiAppDistribution",
      {
        defaultBehavior: {
          origin: new origins.S3Origin(bucket),
          viewerProtocolPolicy:
            cloudfront.ViewerProtocolPolicy.REDIRECT_TO_HTTPS,
          allowedMethods: cloudfront.AllowedMethods.ALLOW_GET_HEAD_OPTIONS,
          cachedMethods: cloudfront.CachedMethods.CACHE_GET_HEAD,
          compress: true,
        },
        defaultRootObject: "index.html",
        domainNames: ["number2word.luisguilher.me"],
        certificate: certificate,
      }
    );

    new s3deploy.BucketDeployment(this, "DeployUiApp", {
      sources: [s3deploy.Source.asset("./../ui/.output/public/")],
      destinationBucket: bucket,
      distribution,
      distributionPaths: ["/*"],
    });

    new cdk.CfnOutput(this, "DistributionURL", {
      value: `https://${distribution.distributionDomainName}`,
      description: "The URL of the website via CloudFront",
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
