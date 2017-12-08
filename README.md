# CU Course Evaluation Service -- MLP
CU Course Evaluation Service -- Machine Learning Product Project

### Team Member
[Jiaqian Chen](https://github.com/Achyles), jc4676;
[TaeYoung Choi](https://github.com/taeyoung-choi), tc2777;
[Zixuan Li](https://github.com/Ironaki), zl2603;
[Zhaoxi Zheng](https://github.com/zhengzhaoxisysu),zz2497

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

In order to get data from preprocessing and traning service, run:

``` bash
    >> python service/make_data.py
```

json files will be stored in the model directory.

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
    >> python REST_api/recommand_api.py
```

open browser, enter "localhost:7777/rec/?rec=COMS"

This will return recommendation of the CS department.

(Note: the ranking and recommendation services is currently only working with the CS department (COMS).
The service currently runs on collected and pre-trained data. We may implement a service to collect and train data when user inputs data.)

## Progress and Sprint Plan

#### What we have done so far:

1. Data mining from CULPA and CU directory
2. Building word embedding model
3. Implementing model training services for course and professor rating
4. Implementing course evaluation service based on trained models
5. Building REST API for services with tornado

#### First Iteration:

1. Improve UI and dashboard output
2. Improve file structure
3. Include major requirement in course recommanding service
4. Expand service coverage on courses
5. Improve training algorithm and evaluating algorithm

#### Some Technical Debts

1. CULPA data department unspecified
2. Course section ignored
3. Professor name approximate match
4. Import from preprocess
5. Used Google NLP API rather than designing our own
