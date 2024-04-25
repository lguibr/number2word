import * as cdk from "aws-cdk-lib";
import * as ec2 from "aws-cdk-lib/aws-ec2";
import * as ecs from "aws-cdk-lib/aws-ecs";
import * as ecs_patterns from "aws-cdk-lib/aws-ecs-patterns";
import * as elbv2 from "aws-cdk-lib/aws-elasticloadbalancingv2";
import * as acm from "aws-cdk-lib/aws-certificatemanager";

export class InfraStack extends cdk.Stack {
  constructor(scope: cdk.App, id: string, props?: cdk.StackProps) {
    super(scope, id, props);

    const vpc = new ec2.Vpc(this, "DjangoVpc", { maxAzs: 2 });
    const cluster = new ecs.Cluster(this, "DjangoCluster", { vpc });

    const certificateArn = process.env.INFRA_SSL!;
    const certificate = acm.Certificate.fromCertificateArn(
      this,
      "Certificate",
      certificateArn
    );

    const fargateService =
      new ecs_patterns.ApplicationLoadBalancedFargateService(
        this,
        "DjangoService",
        {
          cluster,
          desiredCount: 1,
          taskImageOptions: {
            environment: {
              DEBUG: "0",
              DJANGO_ALLOWED_HOSTS: "*",
              SECRET_KEY: process.env.SECRET_KEY ?? "super-secret",
              DB_USER: process.env.DB_USER ?? "lguibr",
              DB_PASSWORD: process.env.DB_PASSWORD ?? "lguibr",
            },
            image: ecs.ContainerImage.fromRegistry("lguibr/django-rest:latest"),
            containerPort: 8000,
          },
          publicLoadBalancer: true,
          healthCheck: {
            command: [
              "CMD-SHELL",
              "curl -f word2vector.luisguilher.me || exit 1",
            ],
            retries: 3,
            startPeriod: cdk.Duration.seconds(15),
            interval: cdk.Duration.seconds(30),
            timeout: cdk.Duration.seconds(5),
          },
        }
      );

    const httpsListener = fargateService.loadBalancer.addListener(
      "HttpsListener",
      {
        port: 443,
        certificates: [certificate],
        open: true,
      }
    );
    httpsListener.addTargets("EcsServiceTarget", {
      port: 80,
      targets: [fargateService.service],
    });

    // Output the HTTPS URL of the load balancer
    new cdk.CfnOutput(this, "LoadBalancerHTTPSURL", {
      value: `https://${fargateService.loadBalancer.loadBalancerDnsName}`,
      description: "URL to access the Django application via HTTPS",
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
