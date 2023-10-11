# Titanic - Machine Learnign from disaster

 ## [From Kaggle Titanic Competitions](https://www.kaggle.com/c/titanic/)

## Mission: Predict survial on the Titanic and get familiar with ML basics

## Data Dictionary
| Variable | Definition | Key |
| ----------- | ----------- | ----------- |
| survival | Survial | 0 = No, 1 = Yes |
| pclass | Ticket class | 1 = 1st, 2 = 2nd, 3 = 3rd |
| sex | Sex
| Age | Age in Years
| sibsp | # of siblings / spouses aboard the Titanic |
| parch | # of parents / children aboard the Titanic
| ticket | Ticket number
| fare | Passenger fare
| cabin | Cabin number
| embarked | Port of Embarkation | C = Cherboug, Q = Queenstown, S = Southampton


### Variable Notes
**pclass:** A proxy for socio-economic status (SES)
- 1st = Upper
- 2nd = Middle
- 3rd = Lower

**age:** Age is fractional if less than 1. If the age is estimated, it is in the form of xx.5

**sibsp:** The dataset define family relations in this way 
- Sibling = brother, sister, stepbrother, step sister
- Spouse = husband, wife (mistresses and fiances were ignored)

**parch:** The dataset defines family relations in this way
- Parent = mother, father
- Child = daughter, son, stepdaughter, stepson
- Some children travelled only with a nanny, therefore parch=0 for them