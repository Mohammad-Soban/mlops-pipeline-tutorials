## MLOPS COMPLETE PIPELINE TUTORIAL

#### CREATE EXPERIMENTS
- Create a new experiment in the `experiments` folder.
- Then paste your initial code in the ipynb file inside the experiments folder where you will complete the Data Science pipeline from data collection to model evaluation.

#### CREATION OF SRC FOLDER
- Create a new folder named `src` in the root directory of your project. This folder will save all the components of the pipeline.
- The src folder contains all the python files that are used in the pipeline.
- Here we will have the following python files:
    1. data_ingestion.py
    2. data_preprocessing.py
    3. feature_engineering.py
    4. model_training.py
    5. model_evaluation.py

- Each of these files will contain the code for each step of the pipeline. each of them will give artifacts that will be used in the next step of the pipeline. Finally a model will be saved in the models folder which will be used for prediction.

- Similarly data folder will be created by the pipeline which will contain the data used in the pipeline. The data folder will have artifcats in the csv format which will be used in the pipeline.

- Inside every component proper logging should be done along with proper exception handling. The logs should be saved in the logs folder. The logs folder will be created by the pipeline. The logs folder will contain the logs of each component of the pipeline. The logs will be saved in the logs folder in a text file with the name of the component. The logs will be saved in the format of `component_name.log`.

#### ABOUT YAML
- YAML (YAML Ain't Markup Language) is designed to be easy for humans to read and write and has indentation-based scoping for structuring data.
- It uses key-value pairs to represent data just like the JSON format or dictionaries in Python.
- It follows a hierarchical structure, which makes it easy to represent complex data structures.
- YAML is extensively used in DevOps, MLOps and many other fields for configuration files, data serialization, and data exchange between languages with different data structures.


#### The next step is to set up the DVC Pipeline
- For setting up the DVC pipeline we will create a `dvc.yaml` file in the root directory of the project.

##### Content of `dvc.yaml` file
- The YAML file will contain the following information:
    1. Start with stages: which will contain the name of the stages of the pipeline. (Ingestion, Preprocessing, Feature Engineering, Training, Evaluation)
    2. Each stage will contain the following information:
        - cmd: The command to run the stage. (python src/component_name.py)
        - params: The parameters to be passed to the stage. (The parameters will be passed in the form of key-value pairs. The parameters will be used in the component.)
        - outs: The output of the stage. (The output will be used in the next stage. The output will be in the form of a dictionary. The output will be used in the component.)
        - deps:` The dependencies of the stage. (The dependencies will be used in the next stage. The dependencies will be in the form of a dictionary. The dependencies will be used in the component.)

#### DVC STEPS
- Initialize DVC in the root directory of the project. (dvc init)
- Reproduce the pipeline using the dvc.yaml file. (dvc repro)
    - This will create a dvc.lock file and run all the commands present in the dvc.yaml file
    - The lock file will contain the md5 hash of the output files and the command used to create the output files which can be used by dvc to move to that particular version of data or models. 
    - Now you can check the flow using the command `dvc dag` (Visually shows the flow of the pipeline)
- Now to keep tracking we will add - commit - push to git 


#### SETTING THE PARAMETERS
- create a `params.yaml` file in the root directory of the project.
- The params.yaml file will contain the parameters to be used in the pipeline. The parameters will be in the form of key-value pairs. The parameters will be used in the components of the pipeline
- The params.yaml file will be of the type
```yaml
module_name:
    param1: value1
    param2: value2
```
- Then for each module, where we want to use the parameters, we will import the yaml file and use the parameters in the code.

#### SETTING UP DVC LIVE
- DVC Live is a tool that helps you visualize and monitor your machine learning experiments in real-time. It provides a web-based dashboard to track the progress of your experiments, view metrics, and compare different runs.
- To set up DVC Live, you need to install it using pip: `pip install dvclive`
- Import dvclive and yaml in the code block where you want to track the metrics (For our case it will be in the model_evaluation.py file)
- Now run different kinds of experiments by changing the parameters from the params.yaml file and then run the experiment using the command `dvc exp run`.
- `dvc repro` does not track the experiments, it just reproduces the pipeline. So we will use `dvc exp run` to track the experiments.
- This will start running the experiment and will create a new folder named `dvc-live` in the root directory of the project. Here the metrics along with the params will be stored and a random name will be given to the experiment.
- Now we can change the parameters in the params.yaml file and run the experiment again using the command `dvc exp run`.
- Now after running many experiments we can visualize the experiments using the command `dvc exp show`. This will give the table but with a lot of information, which is difficult to interpret.
- So we use the DVC Live Extension for VS Code to visualize the experiments in a better way. This extension will give a better view of the experiments and will help you to compare the experiments easily.
- To delete an experiment use the command `dvc exp remove <experiment_name>`.
- To reproduce the experiment use the command `dvc exp apply <experiment_name>`.
- By using `dvc exp apply <experiment_name>` we can move to that particular experiment and then we can run the pipeline from there using the command `dvc repro`. This is similar to git checkout where we can move to a particular commit and then run the pipeline from there.



#### USING THE DVC LIVE EXTENSION
- Install the DVC Extension for VS Code from the marketplace.
- Open the extension and click on show Experiments, which will show the experiments in a table format.
- We can also show plots by clicking on the plot icon in the top right corner of the extension and select all those experiments which we want to compare.
- We can also run a new experiment by clicking on the run button in the top right corner of the extension.