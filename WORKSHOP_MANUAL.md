# Quest4MLOps Workshop Guiding Manual

As you already heard, Linnea pushed her code for the House Pricing prediction model to the MLOps_training repository. Now, it is your turn to continue and improve her work!

Follow these steps first:

1. Fork the repository and provide access to team members. This will be your team's repository.
1. Each person can clone the team repository. When clonning the repository, follow the instructions on the README file.
1. Ensure you are working on the "dev" branch!!

- **Tip**: This (link)\[http://i-1203.cloud.fraunhofer.pt/\] might have useful information, feel free to explore during the workshop.

## MODULE 1 - Best Practices

In  this module, you will be improving the code Linnea already developed and applying the MLOps Best Practices!

### 1. Run the code

Start by running the code and trying to see if it works! If it does not, try to fix or comment code which is not working.

### 2. Fix pre-commit errors

In this task, you have to run the pre-commit tool to identify mistakes in the code, and fix them.

- The pre-commit tests are listed in the `.pre-commit-config.yaml` file, in the root folder of the repository.
- The `pyproject.toml` file contains some configurations for these tests.
- In order to run pre-commit, you can start by using the command `pre-commit run --all-files`.
- There are some errors where **pre-commit** automatically corrects them, so you do not need to correct them yourself.
- Others, you will have to take action.
- In order to fix an error you have three options:
  1. Improve the code: This implies you fix the error in the code
  1. Change the configuration: Some pre-commit tests have configurable parameters, which are listed in the `pyproject.toml` file. You can take a look and change them there.
  1. Disable the pre-commit test: For this, you must navigate to the `.pre-commit-config.yaml` file, find the lines corresponding to the name of the test you want to disable, and either comment them or delete them.
- **Tip**: If you Ctrl+\[Left Mouse Click\] on the file path indicated in a specific error, it will take you directly to the line where the error is.
- **Tip**: To be more efficient, you can combine the following commands to scan only staged files: `git add . && pre-commit`

**Some of the tests (shellcheck and hadolint) are failing and pre-commit is asking me to install them.**

This is because some of the pre-commit tests require a local application to run. In order to install them, you need to follow the instructions and ensure they are added to the PATH environment variable of your system.

If you are unable install them, you can disable the tests on the `.pre-commit-config.yaml` file by commenting them, and move on!

**In order to print results in the console, I only know the `print` function, which raises an error in pre-commit. What can I do to fix it?**

A Logger is the solution to your problem. Although using `print` might be very convenient, it is not a good practice and creates dirty code!

A logger provides several features that `print` does not:

- Easy to see where and when (even what line no.) a logging call is being made from.
- You can log to files, sockets, pretty much anything, all at the same time.
- You can differentiate your logging based on severity.

The logger we recommend you to use is the `loguru` one. You can simply go to the top of your script and white `from loguru import logger`. Visit the [documentation](https://loguru.readthedocs.io/en/stable/index.html) page to see how you can easily start using it to organize your logs on the console!

**Note**: There is an FhP Logger created by one of our colleagues! It allows you to log text to a Zulip stream, which can be very usefull if you are running your code remotely (for example, in HPC). In order to work with the FhPLogger, you have to download a file with your Zulip API from your account. You can learn more about that in this [link](https://zulip.com/api/api-keys)

### 3. Refactor code

In this step, we want you to refactored the code in the main.py file. As you can see, both preprocessing and training are bundeled in the same file. You should split these functionalities each into its own function and its own file.

### 4. Push your code to the repository

Lastly, you need to save your changes to the remote repository. For that, you can commit by using the `make commit` helper in the root folder of the repository, which takes advatange of commitizen to standardize your commits.

**Tip**: You can take a look on how it works in http://i-1203.cloud.fraunhofer.pt/cookiecutter_precommit/

## MODULE 2 - MLFlow Experiment Tracking

In this module, you will start with tracking your experiments using the MLFlow tool. We leave here the [link](https://mlflow.org/docs/latest/index.html) for the MLFlow documentation, as we know you will use it wisely! Also, feel free to browse the web or ask us how to solve a particular issue!

We will be using the following MLFlow server for our experiments: [http://i-1286.cloud.fraunhofer.pt:8001](http://i-1286.cloud.fraunhofer.pt:8001)

### 1. Setup your credentials on a .secrets file

For this, you have to setup the MLFlow server credentials on a `.secrets` file in your project root folder. You can see that these variables are loaded in the `.envrc` file. The magic is all done, you just have to copy the following text into your `.secrets` file.

````
```python
# MLFLOW ------------------------------------------------------------
MLFLOW_TRACKING_URI="http://i-1286.cloud.fraunhofer.pt:8001"
MLFLOW_TRACKING_USERNAME="mlflow_quest4mlops"
MLFLOW_TRACKING_PASSWORD="quest4mlops"
# MINIO S3 ----------------------------------------------------------
AWS_ACCESS_KEY_ID="minio_quest4mlops"
AWS_SECRET_ACCESS_KEY="quest4mlops"
MLFLOW_S3_ENDPOINT_URL="http://i-1286.cloud.fraunhofer.pt:9000"
# EOF
```
````

### 2. Set the experiment name

### 3. Set where does the run start and end

### 4. Log the parameters used to configure your program

### 5. Log the model and save it to the Model Registry

### 6. Log any metrics and results you feel are important.

### 7. Extras! You can explore using Nested runs for running your code several times in just one go, and also explore the Hydra tool for parameter configuration!

## MODULE 3 - ML Pipelines

In this module, you will configure your first Machine Learning pipelines. This allows you to configure and run each of the steps needed for your ML project. Luckily, we have already created a template for you!

### 1. Understand how the Pipeline system works

### 2. Configure each of the steps of the pipeline, one by one, and test each time you had a new step.

### 3. After completing the pipeline, try to modify something in one of the steps! As you can see, only steps which had changes are run again.

### 4. Go to the MLFlow server and ensure your pipeline worked correctly!

## MODULE 4 - Deploy a docker Api

In this module, you will create a docker api to serve your model. This will allow to simulate a environment where you would deploy a model to real world.

### 1. Create an api with fast api

### 2. Create an endpoint where you can make predictions

### 3. Go get the model from mlflow

### 4. Try to bundle with docker

## MODULE 5 - Monitor your deployed Model

In this module, you will create a docker api to serve your model. This will allow to simulate a environment where you would deploy a model to real world.

### 1. Create an api with fast api

### 2. Create an endpoint where you can make predictions

### 3. Go get the model from mlflow

### 4. Try to bundle with docker
