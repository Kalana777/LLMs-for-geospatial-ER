# LLMs-for-geospatial-ER
#### Code for 'Omni Geometry Representation Learning vs Large Language Models for Geospatial Entity Resolution'

This project presents the code for the experiments conducted on LLMs for geospatial entity resolution.

This is a baseline compared against Omni. For the novel Omni model proposed in the paper, please check this [repo](https://github.com/Kalana777/Omni).


### Install required packages
```
pip install -r requirements.txt
```

### Download Data
The model is tested with 4 geospatial ER datasets. Download the New Zealand Entity Resolution dataset (NZER) 
[here](https://figshare.com/s/e0e0481d62a3e411178b) and copy to data directory. 


The complex geometry enhanced, pre-processed versions of the third-party geospatial ER datasets: GeoD, SGN & GTMD, have 
been made available [here](https://figshare.com/s/7858aa81a88b2347d09d). Unzip the content into the data directory.

Alternatively, you can set the path to the dataset folder of the original Omni project, where you may already have downloaded this data. 


### Notebooks

The code is split into four notebooks:

1. **prompt_dataset_prep** - Use this notebook to create the prompt datasets from the original ER geospatial datasets.
2. **zeroshot_llama3_8b** - Execute the geospatial ER and geospatial relation mining tasks in zero shot setting.
3. **fewshot_llama3_8b** - Same as above in few-shot setting.
4. **finetune_llama38b** - Code for fine-tuning the model using the training data and then predicting on the corresponding test sets. 

