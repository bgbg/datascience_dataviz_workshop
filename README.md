# Data Visualization from default to outstanding. Test cases of tough data visualization problems with Python



## Important!

Code repository is here: https://github.com/bgbg/datascience_dataviz_workshop

During the workshop, I will share code snippets using [this shared directory](https://drive.google.com/open?id=1umiVMh5xXAxDHhXUkkNgVdDztnSjGCkx)

1. **Make sure you meet all the requirements. We will not be able to support missing installations or non-working code**. The provided notebook `00-before-we-begin.ipynb` will take you through the verification process. It will make sure that you have all the required software installed, and that you have enough knowledge to proceed with the workshop. It is up to you to make sure that everything works.

2. Visit the [workshop repository](https://github.com/bgbg/datascience_dataviz_workshop) one day before the workshop. I will update that repository with code examples and data sets. You should have them on your computer before the workshop starts.

3. Follow [my blog](https://gorelik.net/blog)
## Workshop description
Data visualization is an indispensable tool for any data scientist. It serves as a means to convey a message or explain a concept. You would never settle for default settings of a machine learning algorithm. Instead, you would tweak them to obtain optimal results. Similarly, you should never stop with the default results you receive from a data visualization framework. Doing so leads to suboptimal results and makes you and your message less convincing.

After this workshop, you will be able to name three most common mistakes in data visualization, and learn how to apply them in your graphs.

During this workshop, a short theoretical introduction will be followed by three lab examples. We will use matplotlib in Jupyter notebooks to practice the knowledge. You are expected to have at least intermediate knowledge of Python, Jupyter notebook interface, and matplotlib object-oriented interface.


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
## Code samples and data sets

I'll update this repository with code samples and data sets. Stay tuned!

## Timeline
1. Theoretical introduction: three most common mistakes in data visualization (45 minutes)
2. Test case (LAB): Plotting several radically different time series on a single graph (45 minutes)
3. Test case (LAB): Bar chart as an effective alternative to a pie chart (45 minutes)
4. Test case (LAB): Pie chart as an effective alternative to a bar chart (45 minutes)

The time line includes some time for recess.
