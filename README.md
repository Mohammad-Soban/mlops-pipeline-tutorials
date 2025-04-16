## MLOPS COMPLETE PIPELINE TUTORIAL

#### CREATE EXPERIMENTS
- Create a new experiment in the `experiments` folder.
- Then paste your initial code in the ipynb file inside the experiments folder where you will complete the Data Science pipeline from data collection to model evaluation.

#### CREATION OF SRC FOLDER
- Create a new folder named `src` in the root directory of your project. This folder will save all the components of the pipeline.
- The src folder contains all the python files that are used in the pipeline.
- Here we will have the following python files
    1. data_ingestion.py
    2. data_preprocessing.py
    3. feature_engineering.py
    4. model_training.py
    5. model_evaluation.py

- Each of these files will contain the code for each step of the pipeline. each of them will give artifacts that will be used in the next step of the pipeline. Finally a model will be saved in the models folder which will be used for prediction.
- Similarly data folder will be created by the pipeline which will contain the data used in the pipeline. The data folder will have artifcats in the csv format which will be used in the pipeline.
- Inside every component proper logging should be done along with proper exception handling. The logs should be saved in the logs folder. The logs folder will be created by the pipeline. The logs folder will contain the logs of each component of the pipeline. The logs will be saved in the logs folder in a text file with the name of the component. The logs will be saved in the format of `component_name.log`.


#### CREATION OF YAML FILE
- YAML (YAML Ain't Markup Language) is designed to be easy for humans to read and write and has indentation-based scoping for structuring data.
- It uses key-value pairs to represent data just like the JSON format or dictionaries in Python.
- It follows a hierarchical structure, which makes it easy to represent complex data structures.
- YAML is extensively used in DevOps, MLOps and many other fields for configuration files, data serialization, and data exchange between languages with different data structures.

#### Content of YAML file
- The YAML file will contain the following information:
    1. Start with stages: which will contain the name of the stages of the pipeline. (Ingestion, Preprocessing, Feature Engineering, Training, Evaluation)
    2. Each stage will contain the following information:
        - cmd: The command to run the stage. (python src/component_name.py)
        - params: The parameters to be passed to the stage. (The parameters will be passed in the form of key-value pairs. The parameters will be used in the component.)
        - outs: The output of the stage. (The output will be used in the next stage. The output will be in the form of a dictionary. The output will be used in the component.)
        - deps: The dependencies of the stage. (The dependencies will be used in the next stage. The dependencies will be in the form of a dictionary. The dependencies will be used in the component.)


### DVC STEPS
- Initialize DVC in the root directory of the project. (dvc init)
- Reproduce the pipeline using the dvc.yaml file. (dvc repro)
    - This will create a dvc.lock file and run all the commands present in the dvc.yaml file
    - The lock file will contain the md5 hash of the output files and the command used to create the output files which can be used by dvc to move to that particular version of data or models. 
    - Now you can check the flow using the command `dvc dag` (Visually shows the flow of the pipeline)
- Now to keep tracking we will add - commit - push to git 
