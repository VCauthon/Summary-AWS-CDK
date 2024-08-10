# Summary-AWS-CDK (っ´ω`)ﾉ(╥ω╥)

This repository provides a concise summary of AWS CDK, offering insights on how it works, along with instructions for installation and management.

The explanations below assume that the project will run on `LINUX` and will be developed using `Python`.

### PROJECT INDEX

- __Theory:__
    - [Overview](./src/docs/01-overview.md)
    - [Core concepts](./src/docs/02-core-concepts.md)
    - [Code Example](./src/docs/03-code-example.md)
- __Technical details:__
    - [Installation](./src/docs/04-setup-instructions.md)
    - [App structure](./src/docs/05-app-folder-structure.md)
    - [Deploying Cycle](./src/docs/06-deploying-cycle.md)
- __Exercises:__
    - [Creating a bucket](./src/excercises/adding-a-bucket/README.md)


### CHEAT SHEET

| __COMMAND__ | __ACTION__ |
|---|---|
| `cdk list` | Lists all the stacks in the app |
| `cdk diff` | Compares the current state of the stack with the state of the deployed stack |
| `cdk deploy` | Deploys the stack to your default AWS account/region |
| `cdk destroy` | Destroys the stack |
| `cdk doctor` | Checks your environment and displays information about issues that it detects |
| `cdk synth` | Synthesizes and prints the CloudFormation template for the specified stack(s) |

### SOURCES

- [AWS Cloud Development Kit (CDK) Crash Course from freeCodeCamp.org](https://www.youtube.com/watch?v=T-H4nJQyMig)
- [Construct documentation](https://docs.aws.amazon.com/cdk/v2/guide/constructs.html)
- [Apps documentation](https://docs.aws.amazon.com/cdk/v2/guide/apps.html)
- [CDK library documentation](https://docs.aws.amazon.com/cdk/v2/guide/libraries.html)
- [Recommended AWS CDK project structure for Python applications](https://aws.amazon.com/blogs/developer/recommended-aws-cdk-project-structure-for-python-applications/)