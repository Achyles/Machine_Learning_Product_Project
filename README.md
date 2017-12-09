# CU Course Evaluation Service -- MLP
CU Course Evaluation Service -- Machine Learning Product Project

## Project Information

### Team Member
[Jiaqian Chen](https://github.com/Achyles), jc4676;
[TaeYoung Choi](https://github.com/taeyoung-choi), tc2777;
[Zixuan Li](https://github.com/Ironaki), zl2603;
[Zhaoxi Zheng](https://github.com/zhengzhaoxisysu),zz2497

### Bullet Points from the Project Requirements

**Required Services:**
1. More than one service: We have one for course recommendation and one for course ranking
2. Inter-service communication
3. Use github
4. Use JIRA
5. Standups and Retros

**Optional Requirements:**
1. [REST API](./REST_api)
2. [Train](./service) (and use) [Model](./model)
3. Present Data: Now data is used in csv and json file, and ranking results are in plain text. We may improve this part in the first iteration
4. An event-driven service:
    1. A library shared by at least two services: both of our services uses [web scraping library](./Web_Scraping)
    2. More than one service: course recommendation and course ranking


### Sprint Plan for the First Iteration

1. Improve UI of the website
3. Include major requirement in course recommending service
4. Expand service coverage on courses


## Service description

CU Course Evaluation Service is a machine learning product that provides functions of course and professor recommendation, ranking and evaluations for Columbia University student. The data come from [CU Course Directory](http://www.columbia.edu/cu/bulletin/uwb/) and  [CULPA](http://culpa.info/). Currently it provides limited features of recommendation and ranking for Computer Science courses.

## MVP Architecture
![MVP Architecture](./data/mvp.png)

## Running services

clone the repository

``` bash
    >> git clone https://github.com/Ironaki/Machine_Learning_Product_Project.git
```

#### Web Scraping 
See the [Web Scraping folder](./Web_Scraping) for information about getting course info from [CU Course Directory](http://www.columbia.edu/cu/bulletin/uwb/) and professor and course reviews from [CULPA](http://culpa.info/). The collected data is stored in csv files in the [data folder](./data).

#### Preprocessing and Training Service

See the [service folder](./service) for the preprocessing and training model service. The result in json format is stored in the [model folder](./model).

#### Run Services on Webpage

After json files are stored in the model direcory, run:

##### Course Ranking Service

``` bash
    >> python REST_api/rank_api.py
```

open browser, enter "localhost:7777/rank/?rank=COMS+W4111+W1004+W4995"

This will return a ranking of courses COMS W4111, COMS W1004, COMS W4995. Add other courses with "+" in the url.

#### Course Recommendation Services

``` bash
    >> python REST_api/recommend_api.py
```

open browser, enter "localhost:7777/rec/?rec=COMS"

This will return recommended courses of the CS department.

(Note: the ranking and recommendation services is currently only working with the CS department (COMS).
The service currently runs on collected and pre-trained data. We may implement a service to collect and train data when user inputs data.)

## Progress and Sprint Plan

#### What we have done so far:

1. Data mining from CULPA and CU directory
2. Building word embedding model
3. Implementing model training services for course and professor rating
4. Implementing course evaluation service based on trained models
5. Building REST API for services with tornado


#### Technical Debts

1. CULPA data department unspecified
2. Course section ignored
3. Professor name approximate match
4. Import from preprocess
5. Used Google NLP API rather than designing our own

#### Possible Improvement in the Future

1. Improve file structure
2. Improve training algorithm and evaluating algorithm
3. Make interactive dashboard
