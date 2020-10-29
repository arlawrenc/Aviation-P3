import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import roc_auc_score
from sklearn.metrics import confusion_matrix
from sklearn.metrics import precision_score
from sklearn.metrics import recall_score
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import roc_curve
import numpy as np

filename = 'models/trainingData.sav'
with open(filename, 'rb') as file:  
   trainingData = joblib.load(file)

# print(trainingData)

train_x, test_x, train_y, test_y = trainingData

#Random Forest
model = RandomForestClassifier(random_state=13)
model.fit(train_x,train_y)

predicted = model.predict(test_x)
model.score(test_x, test_y)

probabilities = model.predict_proba(test_x)

roc_auc_score(test_y, probabilities[:,1])

confusion_matrix(test_y, predicted)

train_predictions = model.predict(train_x)
precision_score(train_y, train_predictions)

recall_score(train_y, train_predictions)

sns.set()

fpr, tpr, _= roc_curve(test_y, probabilities[:,1])
plt.plot(fpr ,tpr)
plt.plot([0,1], [0,1], color='grey', lw=1, linestyle='--')
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')

def predict_delay(departure_date_time, origin):
    from datetime import datetime
    
    try:
        departure_date_time_parsed = datetime.strptime(departure_date_time, '%d/%m/%Y %H:%M:%S')
    except ValueError as e:
        return 'Error parsing date/time - {}'.format(e)
    
    month = departure_date_time_parsed.month
    day = departure_date_time_parsed.day
    day_of_week = departure_date_time_parsed.isoweekday()
    hour = departure_date_time_parsed.hour
    
    origin = origin.upper()
#    destination = destination.upper()
    
    input = [{'MONTH':month,
              'DAY_OF_MONTH': day,
              'DayOfWeek': day_of_week,
              'CRS_DEP_TIME': hour,
              'ORIGIN_BOS': 1 if origin == 'BOS' else 0,
              'ORIGIN_DCA': 1 if origin == 'DCA' else 0,
              'ORIGIN_DEN': 1 if origin == 'DEN' else 0,
              'ORIGIN_DFW': 1 if origin == 'DFW' else 0,
              'ORIGIN_EWR': 1 if origin == 'EWR' else 0,
              'ORIGIN_FLL': 1 if origin == 'FLL' else 0,
              'ORIGIN_LGA': 1 if origin == 'LGA' else 0,
              'ORIGIN_MCO': 1 if origin == 'MCO' else 0,
              'ORIGIN_MIA': 1 if origin == 'MIA' else 0,
              'ORIGIN_ORD': 1 if origin == 'ORD' else 0
             
        
    }]
    
    return model.predict_proba(pd.DataFrame(input))[0][0]
    
# print(predict_delay('24/10/2020 15:00:00','BOS'))

labels = ('Nov', 'Dec', 'Jan', 'Feb', 'Mar', 'Apr', 'May')
values = (predict_delay('01/11/2020 15:00:00','BOS'),
          predict_delay('01/12/2020 15:00:00','BOS'),
          predict_delay('01/01/2021 15:00:00','BOS'),
          predict_delay('01/02/2021 15:00:00','BOS'),
          predict_delay('01/03/2021 15:00:00','BOS'),
          predict_delay('01/04/2021 15:00:00','BOS'),
          predict_delay('01/05/2021 15:00:00','BOS'))
alabels = np.arange(len(labels))

plt.bar(alabels, values, align='center', alpha=0.5)
plt.xticks(alabels,labels)
plt.ylabel('Probability of On-Time Arrival')
plt.ylim((0.0, 1.0))

labels = ('Winter', 'Spring', 'Summer', 'Fall')
values = (predict_delay('21/12/2020 15:00:00','BOS'),
          predict_delay('21/03/2021 15:00:00','BOS'),
          predict_delay('21/06/2021 15:00:00','BOS'),
          predict_delay('21/09/2021 15:00:00','BOS'))
alabels = np.arange(len(labels))

plt.bar(alabels, values, align='center', alpha=0.5)
plt.xticks(alabels,labels)
plt.ylabel('Probability of On-Time Arrival')
plt.ylim((0.0, 1.0))


