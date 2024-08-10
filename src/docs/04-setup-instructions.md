<table align="center">
  <tr>
    <td>
        <a href="../docs/03-code-example.md">
        <img src="../static/icons/arrow_left.png" alt="Left" title="Constructs">
      </a>
    </td>
    <td>
      <a href="../../README.md">
        <img src="../static/icons/house.png" alt="Home" title="Back to the index">
      </a>
    </td>
    <td>
      <a href="../docs/05-app-folder-structure.md">
        <img src="../static/icons/arrow_right.png" alt="Right" title="Project folder structure">
      </a>
    </td>
  </tr>
</table>

---

# INSTALLATION

To use the AWS Cloud Development Kit (CDK), you'll need to set up a few things on your development environment.

Here's a general guide on what you need:

<table border="1" cellpadding="10">
  <tr>
    <th>Step</th>
    <th>Command</th>
    <th>Explanation</th>
  </tr>
  <tr>
    <td rowspan="2">AWS CLI</td>
    <td><code>sudo apt-get install awscli</code></td>
    <td>Installs the AWS Command Line Interface (CLI) on your Ubuntu system, allowing you to interact with AWS services from the command line.</td>
  </tr>
  <tr>
    <td><code>aws configure</code></td>
    <td>Configures the AWS CLI by prompting you for your AWS Access Key ID, Secret Access Key, region, and output format.</td>
  </tr>
  <tr>
    <td rowspan="3">NVM</td>
    <td><code>curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.1/install.sh | bash</code></td>
    <td>Downloads and installs NVM (Node Version Manager), which allows you to manage multiple versions of Node.js on your system.</td>
  </tr>
  <tr>
    <td><code>source ~/.nvm/nvm.sh</code></td>
    <td>Loads NVM into the current terminal session, making the <code>nvm</code> command available immediately after installation.</td>
  </tr>
  <tr>
    <td><code>nvm --version</code></td>
    <td>Verifies that NVM is installed correctly by checking its version.</td>
  </tr>
  <tr>
    <td rowspan="3">Node.js and npm</td>
    <td><code>nvm install v20.11.0</code></td>
    <td>Installs Node.js version 20.11.0, along with npm (Node Package Manager), using NVM.</td>
  </tr>
  <tr>
    <td><code>node --version</code></td>
    <td>Checks and confirms the installed version of Node.js.</td>
  </tr>
  <tr>
    <td><code>npm --version</code></td>
    <td>Checks and confirms the installed version of npm.</td>
  </tr>
  <tr>
    <td rowspan="3">AWS CDK</td>
    <td><code>npm install -g aws-cdk</code></td>
    <td>Installs the AWS CDK (Cloud Development Kit) CLI globally on your system, enabling you to create and manage AWS infrastructure using code.</td>
  </tr>
  <tr>
    <td><code>npm install aws-cdk-lib</code></td>
    <td>Installs the AWS CDK library in the current project directory, which provides the constructs and resources needed to define your infrastructure.</td>
  </tr>
  <tr>
    <td><code>cdk --version</code></td>
    <td>Verifies that the AWS CDK CLI is installed correctly by checking its version.</td>
  </tr>
  <tr>
    <td rowspan="2">Docker</td>
    <td><a href="https://docs.docker.com/engine/install/ubuntu/">Installation guide</a></td>
    <td>Provides a link to the official Docker installation guide for Ubuntu, which you should follow to install Docker on your system.</td>
  </tr>
  <tr>
    <td><code>sudo chmod 666 /var/run/docker.sock</code></td>
    <td>Changes the permissions on the Docker socket, allowing your user to run Docker commands without needing <code>sudo</code>.</td>
  </tr>
</table>



---

<table align="center">
  <tr>
    <td>
        <a href="../docs/03-code-example.md">
        <img src="../static/icons/arrow_left.png" alt="Left" title="Constructs">
      </a>
    </td>
    <td>
      <a href="../../README.md">
        <img src="../static/icons/house.png" alt="Home" title="Back to the index">
      </a>
    </td>
    <td>
      <a href="../docs/05-app-folder-structure.md">
        <img src="../static/icons/arrow_right.png" alt="Right" title="Project folder structure">
      </a>
    </td>
  </tr>
</table>