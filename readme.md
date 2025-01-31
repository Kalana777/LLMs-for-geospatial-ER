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
4. **finetune_llama3_8b** - Code for fine-tuning the model using the training data and then predicting on the corresponding test sets. 



### Detailed Prompt Designs

Here are examples for each of the prompts designed for the experiments in the paper:

simple (geospatial ER)

```
Do the two place descriptions refer to the same real-world place? Answer with 'Yes' if they do and 'No' if they do not.
Place 1: 'Base Backpackers hostel -36.8496619 174.764636'
Place 2: 'Queen Street Backpackers hostel -36.8489282 174.7624718'
```

simple (geospatial relation prediction)

```
Two place descriptions are provided. Predict the relation between them. Answer only with ‘same_as’, ‘part_of’, ‘serves’ or ‘unknown’.
Place 1: 'Chintaroma cafe 555 Lonsdale Street 3000 -37.8146313 144.9569527'
Place 2: 'Owen Dixon Chambers West office 525 Lonsdale Street 3000 -37.8142242 144.9566218'
```

attribute-value (geospatial ER)

```
Do the two place descriptions refer to the same real-world place? Answer with 'Yes' if they do and 'No' if they do not.
Place 1: 'name: Base Backpackers type: hostel latitude: -36.8496619 longitude: 174.764636'
Place 2: 'name: Queen Street Backpackers type: hostel latitude: -36.8489282 longitude: 174.7624718'
```

attribute-value (geospatial relation prediction)
```
Two place descriptions are provided. Answer with 'same_as' if the first place is the same as the second place. 
Answer with 'part_of' if the first place is a part of the second place and is located inside the second place. 
Answer with 'serves' if the first place provides a service to the second place in terms of human mobility, assistance, etc. 
Answer with 'unknown' if the two places show none of these relations.
Place 1: 'name: That Schnitzel Place type: cafe address: 231 Exhibition Street 3000 latitude: -37.810514 longitude: 144.969612'
Place 2: 'name: Hotel Ovolo type: hotel address: 19 Little Bourke Street 3000 latitude: -37.8107508 longitude: 144.9719983'
```

plm-serialization (geospatial ER)

```
Do the two place descriptions refer to the same real-world place? Answer with 'Yes' if they do and 'No' if they do not.
Place 1: 'COL name VAL SKYCITY Hotel COL type VAL hotel COL latitude VAL -36.84851 COL longitude VAL 174.76197'
Place 2: 'COL name VAL SkyCity Grand Hotel COL type VAL hotel COL latitude VAL -36.84939821850368 COL longitude VAL 174.76257662778417'
```

plm-serialization (geospatial relation prediction)
```
Two place descriptions are provided. Answer with 'same_as' if the first place is the same as the second place. 
Answer with 'part_of' if the first place is a part of the second place and is located inside the second place. 
Answer with 'serves' if the first place provides a service to the second place in terms of human mobility, assistance, etc. 
Answer with 'unknown' if the two places show none of these relations.
Place 1: 'COL name VAL That Schnitzel Place COL type VAL cafe COL address VAL 231 Exhibition Street 3000 COL latitude VAL -37.810514 COL longitude VAL 144.969612'
Place 2: 'COL name VAL Hotel Ovolo COL type VAL hotel COL address VAL 19 Little Bourke Street 3000 COL latitude VAL -37.8107508 COL longitude VAL 144.9719983'
```

attribute-value-distance (geospatial ER)

```
Two place descriptions and the geographic distance between them is provided. Do the two place descriptions refer to the same real-world place? Answer with 'Yes' if they do and 'No' if they do not.
Place 1: 'COL name VAL SKYCITY Hotel COL type VAL hotel COL latitude VAL -36.84851 COL longitude VAL 174.76197'
Place 2: 'COL name VAL SkyCity Grand Hotel COL type VAL hotel COL latitude VAL -36.84939821850368 COL longitude VAL 174.76257662778417'
Distance: 0.11km: 
```

attribute-value-distance (geospatial relation prediction)
```
Two place descriptions and the geographic distance between them is provided. Answer with 'same_as' if the first place is the same as the second place. 
Answer with 'part_of' if the first place is a part of the second place and is located inside the second place. 
Answer with 'serves' if the first place provides a service to the second place in terms of human mobility, assistance, etc. 
Answer with 'unknown' if the two places show none of these relations.
Place 1: 'COL name VAL That Schnitzel Place COL type VAL cafe COL address VAL 231 Exhibition Street 3000 COL latitude VAL -37.810514 COL longitude VAL 144.969612'
Place 2: 'COL name VAL Hotel Ovolo COL type VAL hotel COL address VAL 19 Little Bourke Street 3000 COL latitude VAL -37.8107508 COL longitude VAL 144.9719983'
Distance: 0.21km
```

