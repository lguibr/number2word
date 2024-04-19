#!/usr/bin/env node
import "source-map-support/register";
import * as cdk from "aws-cdk-lib";
import { InfraStack } from "../lib/infra-stack";
import { UiAppDeploymentStack } from "../lib/ui-stack";

const app = new cdk.App();
new InfraStack(app, "InfraStack", {});
new UiAppDeploymentStack(app, "UiAppDeploymentStack", {});
