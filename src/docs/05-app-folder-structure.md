<table align="center">
  <tr>
    <td>
        <a href="../docs/04-setup-instructions.md">
        <img src="../static/icons/arrow_left.png" alt="Left" title="CDK Installation">
      </a>
    </td>
    <td>
      <a href="../../README.md">
        <img src="../static/icons/house.png" alt="Home" title="Back to the index">
      </a>
    </td>
    <td>
      <a href="../docs/06-deploying-cycle.md">
        <img src="../static/icons/arrow_right.png" alt="Right" title="Deploying Cycle">
      </a>
    </td>
  </tr>
</table>

---

# APP STRUCTURE

- [Creating a new project](#creating-a-new-project)
- [Project structure](#project-structure)

---

## Creating a new project

Once you have [AWS CDK installed](./04-setup-instructions.md), you can create a new CDK application by following these steps:

- Create the project folder:
  - `mkdir my-cdk-app&&cd my-cdk-app`
- Initialize a new CDK app:
  - `cdk init app --language python`
- Create a virtual interpreter with conda
  - `conda create -n my-cdk-env python=3.10`
  - `conda activate my-cdk-env`
- Install dependencies into the virtual interpreter
  - `pip install -r requirements.txt`

---

## Project structure

The basic folder distribution created with CDK will be the following:

```
my-cdk-app/               # Root directory of your CDK project
│
├── bin/                  # Contains the entry point for the CDK application
│   └── my_cdk_app.py     # Main entry file for the CDK app (defines stacks)
│
├── lib/                  # Contains your CDK stack definitions
│   └── my_cdk_app_stack.py  # Defines your stack(s) and AWS resources
│
├── .gitignore            # Specifies intentionally untracked files to ignore
│
├── cdk.json              # Configures the CDK command-line toolkit
│
├── requirements.txt      # Lists Python dependencies (for pip installation)
│
└── README.md             # Project description and instructions
```

However, you can make your how custom format. [Here](https://aws.amazon.com/blogs/developer/recommended-aws-cdk-project-structure-for-python-applications/) you will find the recommended aws project CDK structure.

---

<table align="center">
  <tr>
    <td>
        <a href="../docs/04-setup-instructions.md">
        <img src="../static/icons/arrow_left.png" alt="Left" title="CDK Installation">
      </a>
    </td>
    <td>
      <a href="../../README.md">
        <img src="../static/icons/house.png" alt="Home" title="Back to the index">
      </a>
    </td>
    <td>
      <a href="../docs/06-deploying-cycle.md">
        <img src="../static/icons/arrow_right.png" alt="Right" title="Deploying Cycle">
      </a>
    </td>
  </tr>
</table>