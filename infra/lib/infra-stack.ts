import * as cdk from "aws-cdk-lib";
import * as ec2 from "aws-cdk-lib/aws-ec2";
import * as ecs from "aws-cdk-lib/aws-ecs";
import * as ecs_patterns from "aws-cdk-lib/aws-ecs-patterns";
import * as sm from "aws-cdk-lib/aws-secretsmanager";
import * as dotenv from "dotenv";
dotenv.config({ path: "../.env" });

export class InfraStack extends cdk.Stack {
  constructor(scope: cdk.App, id: string, props?: cdk.StackProps) {
    super(scope, id, props);

    const vpc = new ec2.Vpc(this, "DjangoVpc", {
      maxAzs: 2,
    });

    const cluster = new ecs.Cluster(this, "DjangoCluster", {
      vpc,
    });

    const secret = sm.Secret.fromSecretAttributes(this, "ImportedSecret", {
      secretCompleteArn: `arn:aws:secretsmanager:${process.env.AWS_REGION}:${process.env.AWS_ACCOUNT}:secret:trellis-example-123456`,
    });

    const fargateService =
      new ecs_patterns.ApplicationLoadBalancedFargateService(
        this,
        "DjangoService",
        {
          cluster,
          cpu: 256,
          memoryLimitMiB: 512,
          desiredCount: 1,
          taskImageOptions: {
            environment: {
              DEBUG: "0",
              DJANGO_ALLOWED_HOSTS: "* localhost 127.0.0.1 [::1]",
            },
            secrets: {
              SECRET_KEY: ecs.Secret.fromSecretsManager(secret, "SECRET_KEY"),
              DB_USER: ecs.Secret.fromSecretsManager(secret, "DB_USER"),
              DB_PASSWORD: ecs.Secret.fromSecretsManager(secret, "DB_PASSWORD"),
            },
            image: ecs.ContainerImage.fromRegistry(
              "lguibr/django-trellis-example:latest"
            ),
            containerPort: 8000,
          },
          publicLoadBalancer: true,
        }
      );

    new cdk.CfnOutput(this, "LoadBalancerDNS", {
      value: fargateService.loadBalancer.loadBalancerDnsName,
    });
  }
}

const app = new cdk.App();
new InfraStack(app, "DjangoAppStack", {
  env: {
    account: process.env.AWS_ACCESS_KEY_ID,
    region: process.env.AWS_REGION,
  },
});
app.synth();
