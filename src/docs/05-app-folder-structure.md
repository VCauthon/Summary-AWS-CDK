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
├── .venv/                # Python virtual environment directory (created after running `python -m venv .venv`)
│
├── my_cdk_app/           # Contains your CDK stack definitions and application code
│   ├── __init__.py       # Marks the directory as a Python package
│   └── my_cdk_app_stack.py  # Defines your stack(s) and AWS resources
│
├── tests/                # Contains unit tests for your CDK stacks
│   ├── __init__.py       # Marks the directory as a Python package
│   └── test_my_cdk_app_stack.py  # Unit tests for your stack(s)
│
├── .gitignore            # Specifies intentionally untracked files to ignore
│
├── README.md             # Project description and instructions
│
├── app.py                # Main entry file for the CDK app (defines stacks)
│
├── cdk.json              # Configures the CDK command-line toolkit
│
├── requirements.txt      # Lists Python dependencies (for pip installation)
│
└── source.bat            # Batch script to activate the virtual environment on Windows
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