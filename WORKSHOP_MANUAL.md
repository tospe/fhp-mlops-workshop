# Quest4MLOps Workshop Guiding Manual

As you already heard, Sven pushed his code for the House Pricing prediction model to the MLOps_training repository. Now, it is your turn to continue and improve her work!

Follow these steps first:

1. Fork the repository to your own GitHub account  
2. Follow the instructions on the README file.

## **MODULE 1 - Best Practices**

In  this module, you will be improving the code Sven already developed and applying the MLOps Best Practices!

### **1. Run the code**

Start by running the code and trying to see if it works!

### **2. Refactor code**

In this step, we want you to refactor the code in the main.py file. As you can see, both preprocessing and training are bundeled in the same file. You should split these functionalities each into its own function and its own file.

### **3. Fix pre-commit errors**

In this task, you have to run the pre-commit tool to identify mistakes in the code, and fix them.

- The pre-commit tests are listed in the `.pre-commit-config.yaml` file, in the root folder of the repository.
- The `pyproject.toml` file contains some configurations for these tests.
- In order to run pre-commit, you can start by using the command `pre-commit run --all-files`.
- There are some errors where **pre-commit** automatically corrects them, so you do not need to correct them yourself.
- Others, you will have to take action!
- In order to fix an error you have three options:
  1. Improve the code: This implies you fix the error in the code
  1. Change the configuration: Some pre-commit tests have configurable parameters, which are listed in the `pyproject.toml` file. You can take a look and change them there.
  1. Disable the pre-commit test: For this, you must navigate to the `.pre-commit-config.yaml` file, find the lines corresponding to the name of the test you want to disable, and either comment them or delete them.
- **Tip**: If you Ctrl+\[Left Mouse Click\] on the file path indicated in a specific error, it will take you directly to the line where the error is.
- **Tip**: To be more efficient, you can run the command `pre-commit run` to scan only staged files: 

### **Some tips**

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


### **4. Push your code to the repository**

Lastly, you need to save your changes to the remote repository. For that, you can commit by using the `make commit` helper in the root folder of the repository, which takes advantage of *commitizen* package to standardize your commits.

**Tip**: You can take a look on how it works in http://i-1203.cloud.fraunhofer.pt/cookiecutter_precommit/

## **MODULE 2 - MLFlow Experiment Tracking**

In this module, you will start with tracking your experiments using the MLFlow tool. We leave here the [link](https://mlflow.org/docs/latest/index.html) for the MLFlow documentation, as we know you will use it wisely! Also, feel free to browse the web or ask us how to solve a particular issue!

Although ideally we have an MLFlow server which several users could use and abuse, we will be working only locally during this workshop. As such, MLFlow will use a local folder called *mlruns/* to track data. In order to access the MLFlow, you have to change the current directory to *mlruns/* and start the UI, using the command `mlflow ui` 

1. **Set the experiment name**
2. **Set run start and end**
3. **Log the parameters used to configure your code**
4. **Log any metrics and results you feel are important.**
5. **Log the model (ideally you could also save it to the MLFlow Model Registry)**
6. **Extras! You can explore using Nested runs for running your code several times in just one go, and also explore the Hydra tool for parameter configuration!**



