---
title: Great Expectations ( work in progress )
---
# Great Expectations 

[Great Expectations](greatexpectations.io)

Got this link from reading online, seems very interesting for higher level data asserts, 
started following the [Welcome Guide](https://docs.greatexpectations.io/docs/)

Their model is quite what we usually do with data processing, 
reading from lake or data source we need to validade the data before doing another action. Like is visualized here:

![Data Archictecture](https://docs.greatexpectations.io/assets/images/GE_OSS_process-448174e3b55ae4dfd7fbb7a8c1a452e3.png)

What really got me into is the higher level declarations that are possible to asset about the data, like:

   ```bash
   # From the example on the docs
   expect_column_values_to_be_between(
      column="passenger_count",
      min_value=1,
      max_value=6
  )
  ```

## Hands on ( commented tutorial )

I followed the [tutorial](https://docs.greatexpectations.io/docs/tutorials/getting_started/tutorial_overview)

Found interesting that they let previous versions of the tutorial on the repo for reading. 
I ended up using a venv instead running direct on system python. 

The first step is create a Data Context, it felts like boostraping a web framework. 
Normally I prefer tools that are less coupled but let's see how this goes. 
Also the cli tool is great, it displayed useful information right from start on nice layout.

  great_expectations init

A classic from all data tools, let's create a DataSource. For the tutorial the DataSource is a csv file.

  ```bash
  great_expectations datasource new
  # it show a wizard
  Using v3 (Batch Request) API

  What data would you like Great Expectations to connect to?
    1. Files on a filesystem (for processing with Pandas or Spark)
    2. Relational database (SQL)
  ```
 I pickup the tutorial choices, local files with panda, and ended up with a jupyter server running. Cool. 
 Opened the url that come from the command output and got this screen:
 
 [missing image](#)
 
 I am not used to Jupyter so took me some time to figure out that the next step is on datasource_new.ipynb file. 
 I changed the datasource name and continued. The tutorial explained 
 some of the internals now before continue but I can tell that the feeling is like setting up a rails or django 
 or similar framework. The yaml file that it creates is quite self-explanatory.
 
 So now we are going to create the expectations, my expectations are high now (...). 
 There are some new, at least to me, vocabulary, so basically it seems that for a fiven set of data, 
 you create a Expectation Suite that is a set of expectations to run against it.
 
 ```bash
 great_expectations suite new
 # another wizard:
 How would you like to create your Expectation Suite?
    1. Manually, without interacting with a sample batch of data (default)
    2. Interactively, with a sample batch of data
    3. Automatically, using a profiler
: 
 # And so on...
 ```
 So, it didn't work as I expected, I opened a new terminal, and typed the command but it failed with:
 
 ```bash
 No datasources found in the context. To add a datasource, run `great_expectations datasource new`
 ```
 So I investigated it and it seems that the notebook was on the uncommited folder, for some reason.
 
 ```
 find . |grep ipynb |grep -v venv
./ge_dbt_airflow_tutorial/great_expectations_projects/final/great_expectations/notebooks/spark/validation_playground.ipynb
(...)
./great_expectations/uncommitted/datasource_new.ipynb
./great_expectations/uncommitted/.ipynb_checkpoints
./great_expectations/uncommitted/.ipynb_checkpoints/datasource_new-checkpoint.ipynb
 ```

So I started over. Now when I created a datasource I observed this error:
```bash 
    
    To access the notebook, open this file in a browser:
        file:///home/developer/.local/share/jupyter/runtime/nbserver-2831-open.html
    Or copy and paste one of these URLs:
        http://localhost:8888/?token=XXX
     or http://127.0.0.1:8888/?token=XXX
Start : This command cannot be run due to the error: The system cannot find the file specified.
At line:1 char:1
+ Start "file:///tmp/tmppvipyy8n.html"
+ ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    + CategoryInfo          : InvalidOperation: (:) [Start-Process], InvalidOperationException
    + FullyQualifiedErrorId : InvalidOperationException,Microsoft.PowerShell.Commands.StartProcessCommand
 
```

Oh boy, on the message from the tool it says: *If files are on local disk
enter a path relative to your current working directory or an absolute path.* but I bindly followed the tutorial. 
So I do it again but now use *./data* as directory and it worked. 

The output from the last tutorial step, adding a new suite was a question about the two data files present on data:

```
A batch of data is required to edit the suite - let's help you to specify it.


Which data asset (accessible by data connector "default_inferred_data_connector_name") would you like to use?
    1. yellow_tripdata_sample_2019-01.csv
    2. yellow_tripdata_sample_2019-02.csv

Type [n] to see the next page or [p] for the previous. When you're ready to select an asset, enter the index.
: 
```

I ran all the steps successfuly and got a new Jupyter notebook to open. Clicked on the getting_started_expectation_suite_taxi.demo
and got a notebook :). I am great fan of notebooks but I am used to do only with Mathematica and pure math functions so I still
a bit lost using it with python.

So following the tutorial, now I creating the expectation. Edit code on a well written Jupyter notebook is awesome.

Running all the cells got me a lot of errors(...). Iprogress not found. Checked on stackoverflow and installed a bunch of 
modules:

```
pip install ipywidgets widgetsnbextension pandas-profiling
```

These seemed to be just for the progress bars look nice, but still an error at the end, that it could not find the given file.
It may be that because I am running on windows with WSL and python on a venv inside ( that likely was not meant on the tutorial )
the reason I am getting so many errors.

I did another search and yes, it seems that you need some special setup for jupyter on WSL. This is where I am stopping now. Will continue later.






 


