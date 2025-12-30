#!/usr/bin/env node
import * as cdk from 'aws-cdk-lib/core';
import { StaticGameWebsiteStack } from '../lib/static-game-website-stack';

const app = new cdk.App();
new StaticGameWebsiteStack(app, 'StaticGameWebsite');
