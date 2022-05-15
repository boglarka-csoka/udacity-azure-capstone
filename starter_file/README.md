# Udacity azure capstone project

My project includes an AutoML run and a hyperparameter optimisation. For both I used a bank marketing dataset. My task is classification and the target variable is y.Late I deployed the best AutoML model and tested the Webservice by sending a request to a model endpoint.

## Dataset

### Overview
I'm using bank marketing data in a tabular format. This is the same which was provided for previous projects.
Source link:"https://automlsamplenotebookdata.blob.core.windows.net/automl-sample-notebook-data/bankmarketing.csv"

### Task
I'm doing a classification task with this dataset. My target variable is y. The primary metric is accuracy.

### Access
I'm accessing the data through the TabularDatasetFactory.from_delimited_files(path="..") function.

## Automated ML
I haven't used any special settings. My configuration included an experiment timeout to prevent the experiment to take to much time. 
I also clarified that the task will be classification and the primary metric is accuracy. The function also contains the train dataset, the name of the target variable and the number of cross validations.

### Results
*TODO*: What are the results you got with your automated ML model? What were the parameters of the model? How could you have improved it?

*TODO* Remeber to provide screenshots of the `RunDetails` widget as well as a screenshot of the best model trained with it's parameters.

## Hyperparameter Tuning
*TODO*: What kind of model did you choose for this experiment and why? Give an overview of the types of parameters and their ranges used for the hyperparameter search


### Results
*TODO*: What are the results you got with your model? What were the parameters of the model? How could you have improved it?

*TODO* Remeber to provide screenshots of the `RunDetails` widget as well as a screenshot of the best model trained with it's parameters.

## Model Deployment
*TODO*: Give an overview of the deployed model and instructions on how to query the endpoint with a sample input.

## Screen Recording
*TODO* Provide a link to a screen recording of the project in action. Remember that the screencast should demonstrate:
- A working model
- Demo of the deployed  model
- Demo of a sample request sent to the endpoint and its response

## Standout Suggestions
*TODO (Optional):* This is where you can provide information about any standout suggestions that you have attempted.
