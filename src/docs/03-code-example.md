<table align="center">
  <tr>
    <td>
        <a href="../docs/02-core-concepts.md">
        <img src="../static/icons/arrow_left.png" alt="Left" title="Core concepts">
      </a>
    </td>
    <td>
      <a href="../../README.md">
        <img src="../static/icons/house.png" alt="Home" title="Back to the index">
      </a>
    </td>
    <td>
      <a href="../docs/04-setup-instructions.md">
        <img src="../static/icons/arrow_right.png" alt="Right" title="CDK installation">
      </a>
    </td>
  </tr>
</table>

---

# CODE EXAMPLE

- [Same solutions different constructs](#same-solution-different-constructs)
- [Special arguments from the CDK](#special-arguments-from-the-cdk)
- [More about constructs and communities](#more-about-constructs-and-communities)

---

## Same solution different constructs

The following sections will show different versions of code showing how to deploy the same solution but using different levels of constructs.

The solution basically is a lambda function that is able to work with an S3 bucket.

### L1

```py
from aws_cdk import (
    core as cdk,
    aws_lambda as lambda_,
    aws_iam as iam,
    aws_s3 as s3,
)

class MyStack(cdk.Stack):
    def __init__(self, scope: cdk.Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        # Create an IAM Role using L1 construct
        l1_iam_role = iam.CfnRole(self, "L1IamRole",
            assume_role_policy_document={
                "Statement": [
                    {
                        "Action": "sts:AssumeRole",
                        "Effect": "Allow",
                        "Principal": {
                            "Service": "lambda.amazonaws.com"
                        }
                    }
                ]
            }
        )

        # Create an S3 Bucket using L1 construct
        l1_bucket = s3.CfnBucket(self, "L1Bucket")

        # Create a Lambda function using L1 construct
        l1_function = lambda_.CfnFunction(self, "L1Function",
            code=lambda_.CfnFunction.CodeProperty(
                s3_bucket=l1_bucket.ref,  # Use the reference to the bucket name
                s3_key="test.zip"
            ),
            role=l1_iam_role.attr_arn  # Use the ARN of the created IAM role
        )

app = cdk.App()
MyStack(app, "MyStack")
app.synth()
```

---

### L2

```py
from aws_cdk import (
    core as cdk,
    aws_lambda as lambda_,
    aws_iam as iam,
    aws_s3 as s3,
)

class MyStack(cdk.Stack):
    def __init__(self, scope: cdk.Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        # Create an S3 Bucket using L2 construct
        bucket = s3.Bucket(self, "MyBucket")

        # Create an IAM Role for Lambda using L2 construct
        lambda_role = iam.Role(self, "MyLambdaRole",
            assumed_by=iam.ServicePrincipal("lambda.amazonaws.com")
        )

        # Grant the Lambda role permissions to read/write to the S3 bucket
        bucket.grant_read_write(lambda_role)

        # Create a Lambda function using L2 construct
        lambda_function = lambda_.Function(self, "MyFunction",
            runtime=lambda_.Runtime.NODEJS_18_X,
            handler="index.handler",
            code=lambda_.Code.from_asset("lambda"),
            role=lambda_role,  # Attach the created IAM role
        )

        # Add an environment variable to the Lambda function with the bucket name
        lambda_function.add_environment("BUCKET_NAME", bucket.bucket_name)

app = cdk.App()
MyStack(app, "MyStack")
app.synth()
```

---

### L3

Here the level 3 construct is defined

```py
from aws_cdk import (
    core as cdk,
    aws_lambda as lambda_,
    aws_iam as iam,
    aws_s3 as s3,
)

class S3LambdaConstruct(cdk.Construct):
    def __init__(self, scope: cdk.Construct, id: str, *, code: lambda_.Code, **kwargs):
        super().__init__(scope, id, **kwargs)

        # Create an S3 Bucket using L2 construct
        self.bucket = s3.Bucket(self, "MyBucket")

        # Create an IAM Role for Lambda using L2 construct
        self.lambda_role = iam.Role(self, "MyLambdaRole",
            assumed_by=iam.ServicePrincipal("lambda.amazonaws.com")
        )

        # Grant the Lambda role permissions to read/write to the S3 bucket
        self.bucket.grant_read_write(self.lambda_role)

        # Create a Lambda function using L2 construct
        self.lambda_function = lambda_.Function(self, "MyFunction",
            runtime=lambda_.Runtime.NODEJS_18_X,
            handler="index.handler",
            code=code,  # Use the code passed in as an argument
            role=self.lambda_role,  # Attach the created IAM role
        )

        # Add an environment variable to the Lambda function with the bucket name
        self.lambda_function.add_environment("BUCKET_NAME", self.bucket.bucket_name)
```

Here is instantiated

```py
from aws_cdk import core as cdk
from aws_cdk import aws_lambda as lambda_
from s3_lambda_construct import S3LambdaConstruct  # Import your custom L3 construct

class MyStack(cdk.Stack):
    def __init__(self, scope: cdk.Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        # Define the Lambda code location
        lambda_code = lambda_.Code.from_asset("lambda")

        # Instantiate the L3 construct, passing in the Lambda code
        s3_lambda = S3LambdaConstruct(self, "S3LambdaConstruct", code=lambda_code)

app = cdk.App()
MyStack(app, "MyStack")
app.synth()
```

---

## Special arguments from the CDK

When you define a construct in CDK, you're essentially creating an object that represents a collection of AWS resources.

The special arguments shown before are the following:

| ARGUMENT | USE |
|---|---|
|`scope`| The scope parameter represents the parent construct in which this construct is being defined. In CDK, every construct must be part of a construct tree, and scope determines where in that tree the current construct will be placed |
|`id`| The id parameter is a string that serves as a unique identifier for the construct within the scope. This ID is used to uniquely identify this construct within its parent, and it forms part of the logical ID that CDK assigns to resources when synthesizing CloudFormation templates |


In other sections of this guide [we will see the complete structure](/02-workshop/01-project-structure/instructions.md) of a CDK project, however, taking advantage that here we are talking about constructs we are going to go into detail about how they are generated.

Next you can see a basic example of a stack defined in CDK.
```typescript
    export class AppStackStack extends Stack {
        constructor(scope: Construct, id: string, props?: StackProps) {

            // Starting the constructor from these stack
            super(scope, id, props);

            // Define the Lambda needed (the l3 construct also has the api getway)
            const helloWorld = new lambda.Function(this, "HelloWorld", {
            runtime: lambda.Runtime.PYTHON_3_9,
            code: lambda.Code.fromAsset("lambda"),
            handler: "lambda.lambda_handler"
            }
            )
        }
    }

```

---

## More about constructs and communities

- [Official AWS constructs](https://docs.aws.amazon.com/solutions/latest/constructs/welcome.html)
- [Community constructs](https://cdkpatterns.com/patterns/)
- [Construct Hub](https://constructs.dev)

---

<table align="center">
  <tr>
    <td>
        <a href="../docs/02-core-concepts.md">
        <img src="../static/icons/arrow_left.png" alt="Left" title="Core concepts">
      </a>
    </td>
    <td>
      <a href="../../README.md">
        <img src="../static/icons/house.png" alt="Home" title="Back to the index">
      </a>
    </td>
    <td>
      <a href="../docs/04-setup-instructions.md">
        <img src="../static/icons/arrow_right.png" alt="Right" title="CDK installation">
      </a>
    </td>
  </tr>
</table>