# 1142_CE5033_Group7_Climate_Impact_Analysis
[![Python Version](https://img.shields.io/badge/python-3.11-blue.svg)](https://www.python.org/)
[![Docker Support](https://img.shields.io/badge/docker-enabled-blue.svg)](https://www.docker.com/)
[![Development Branch](https://img.shields.io/badge/branch-dev-orange.svg)](https://github.com/IamsleepingOuO/1142_CE503)

## Abstract
### Background
As climate change intensifies, accurately assessing the economic impact of extreme weather events is critical for disaster management. Traditional risk assessments often rely heavily on the meteorological severity of an event. However, this study investigates whether physical severity alone is sufficient to predict catastrophic economic losses.
### Methods
We analyzed a global dataset of climate events from 2020 to 2025. The research employed a hybrid analytical approach, combining traditional statistical hypothesis testing with machine learning techniques. Initially, Welch’s t-test and Cohen’s d effect size were used to examine the baseline relationship between climate severity and economic impact. Subsequently, a Random Forest classifier was trained to predict the occurrence of extreme economic disasters (defined as the top 20% of economic losses) and extract feature importance.
### Results
Statistical analysis indicated that while meteorological severity is significantly associated with economic loss ($p < 0.001$), its practical effect size is surprisingly small (Cohen's $d \approx 0.19$). The Random Forest model further revealed the underlying cause: the "Golden Triangle" of disaster economics. Feature importance analysis demonstrated that socio-economic variables—specifically impact per capita, total affected population, and event duration—overwhelmingly outweigh physical severity in determining the scale of financial devastation.
### Conclusion
This study demonstrates that the true cost of a climate disaster is dictated more by the socio-economic vulnerability of the affected region than by the natural intensity of the weather event itself. These findings suggest that governments and insurance sectors should shift their risk evaluation frameworks to prioritize population density and regional economic exposure over mere meteorological warnings.

## How to use
Downlad the dataset, put it under the folder `data/raw/`.
https://www.kaggle.com/datasets/uom190346a/global-climate-events-and-economic-impact-dataset \
And `cd` into the folder.

### First time

```
docker build -t climate-env .
```

### Run docker and prepare for Jupyter connection

``` 
docker run -it --rm -p 8888:8888 -v $(pwd):/workspace climate-env
```

### Run Jupyter Lab
```
jupyter lab --ip=0.0.0.0 --port=8888 --no-browser --allow-root
```

