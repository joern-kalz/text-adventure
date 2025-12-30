import * as cdk from 'aws-cdk-lib/core';
import { Template } from 'aws-cdk-lib/assertions';
import * as Infra from '../lib/static-game-website-stack';

test('SQS Queue Created', () => {
    const app = new cdk.App();
    // WHEN
    const stack = new Infra.StaticGameWebsiteStack(app, 'MyTestStack');
    // THEN
    const template = Template.fromStack(stack);

    template.hasResourceProperties('AWS::SQS::Queue', {
        VisibilityTimeout: 300
    });
});
