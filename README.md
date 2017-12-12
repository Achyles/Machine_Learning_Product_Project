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
2. Include major requirement in course recommending service
3. Better inter-service communication


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

Open Machine_Learning_Product_Project folder in terminal, run:

``` bash
    >> cd React_app/basic_react_dashboard/
    
    >> npm install
    
    >> npm start
```
After the third command a webpage will be open in a browser.

Open Machine_Learning_Product_Project folder in another terminal, run:

``` bash
    >> cd REST_api/
    
    >> python rank_api.py
```

With both terminal running, enter the department and course numbers as instructed, e.g. "COMS+W1004+W3157+W4118". Hit submit button. The page will return a ranked list of courses.

##### Course Review Service

Open Machine_Learning_Product_Project folder in terminal, run:

``` bash
    >> cd React_app/review_service/
    
    >> npm install
    
    >> npm start
```
After the third command a webpage will be open in a browser.

Open Machine_Learning_Product_Project folder in another terminal, run:

``` bash
    >> cd REST_api/
    
    >> python review_api.py
```

With both terminal running, enter the professor name and the course number as instructed. As long as there is a space between first and last name, the order of them does not matter, e.g. "Feng Yang+2024" or "Yang Feng+2024". Hit submit button. The page will return the top three key sentences from all reviews for the course and professor.

**Example:**
![Sample Service](./service_example/course_rank.png)

#### Course Recommendation Services (To be improved in the first iteration)

Open Machine_Learning_Product_Project folder in terminal, run:

``` bash
    >> cd REST_api/
    
    >> python recommend_api.py
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
4. Expand service coverage on courses
