# Data Visualization from default to outstanding. Test cases of tough data visualization problems with Python



## Important!

Code repository is here: https://github.com/bgbg/datascience_dataviz_workshop

During the workshop, I might share code snippets using [this shared directory](https://drive.google.com/open?id=1umiVMh5xXAxDHhXUkkNgVdDztnSjGCkx)

1. **Make sure you meet all the requirements. I will not be able to support missing installations or non-working code**. The provided notebook `00-before-we-begin.ipynb` will take you through the verification process. It will make sure that you have all the required software installed, and that you have enough knowledge to proceed with the workshop. It is up to you to make sure that everything works.


3. Follow [my blog](https://gorelik.net/blog)

## Workshop description
Data visualization is an indispensable tool for any data scientist. It serves as a means to convey a message or explain a concept. You would never settle for default settings of a machine learning algorithm. Instead, you would tweak them to obtain optimal results. Similarly, you should never stop with the default results you receive from a data visualization framework. Doing so leads to suboptimal results and makes you and your message less convincing.

After this workshop, you will be able to name three most common mistakes in data visualization, and learn how to apply them in your graphs.

During this workshop, a short theoretical introduction will be followed by several lab examples. We will use matplotlib in Jupyter notebooks to practice the knowledge. You are expected to have at least intermediate knowledge of Python, Jupyter notebook interface, and matplotlib object-oriented interface.


## Setup
The easiest way to make sure you have all the required software is to use the supplied file to create a [conda environment](https://conda.io/docs/user-guide/tasks/manage-environments.html).

In your terminal, go to the directory that contains this notebook and type

```bash
conda env create -p ./dataviz-env -f ./environment.yml
```

This will create an environment in your local directory. Next, activate the environment and start the notebook.

```bash
source activate ./dataviz-env
jupyter notebook
```

