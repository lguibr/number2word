import * as cdk from "aws-cdk-lib";
import * as ec2 from "aws-cdk-lib/aws-ec2";
import * as ecs from "aws-cdk-lib/aws-ecs";
import * as ecs_patterns from "aws-cdk-lib/aws-ecs-patterns";

export class InfraStack extends cdk.Stack {
  constructor(scope: cdk.App, id: string, props?: cdk.StackProps) {
    super(scope, id, props);

    const vpc = new ec2.Vpc(this, "DjangoVpc", { maxAzs: 2 });
    const cluster = new ecs.Cluster(this, "DjangoCluster", { vpc });

    new ecs_patterns.ApplicationLoadBalancedFargateService(
      this,
      "DjangoService",
      {
        cluster,
        cpu: 512,
        memoryLimitMiB: 1024,
        desiredCount: 2,
        taskImageOptions: {
          environment: {
            DEBUG: "0",
            DJANGO_ALLOWED_HOSTS: "* localhost 127.0.0.1 [::1]",
            SECRET_KEY: process.env.SECRET_KEY ?? "super-secret",
            DB_USER: process.env.DB_USER ?? "lguibr",
            DB_PASSWORD: process.env.DB_PASSWORD ?? "lguibr",
          },

          image: ecs.ContainerImage.fromRegistry(
            "lguibr/django-trellis-example:latest"
          ),
          containerPort: 8000,
        },
        publicLoadBalancer: true,
      }
    );
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
