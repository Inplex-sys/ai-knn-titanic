from sklearn.neighbors import KNeighborsClassifier
import pandas

class AI:
    def __init__( self, data ):
        self.passengers = data['passengers']
        self.params = data['params']
        pass

    def parseUsefullData(self):
        return {
            'data': [
                self.passengers[:,"Age"],
                self.passengers[:,"Pclass"],
                self.passengers[:,"Sex"]
            ],
            'survivors': self.passengers[:,"Survived"]
        }
        pass

    def checkSurvivalProbability(self):
        parsedData = self.parseUsefullData()
        raw = list(zip(
            parsedData['data'][0], 
            parsedData['data'][1], 
            parsedData['data'][2]
        ))

        # Creating knn object
        model = KNeighborsClassifier(n_neighbors=3)

        # Training the model
        model.fit( raw, parsedData['survivors'] )

        # We predict the survival probability of the passenger
        return model.predict([
            [
                self.params['passenger_age'],
                self.params['passenger_class'],
                self.params['passenger_sex']
            ]
        ])
    pass

def main():
    global params
    passengers = pandas.read_csv("titanic.csv")

    print(
        f"We have loaded {len(passengers[:,"PassengerId"])} passangers\n" +
         "The others have issue with their data ..."
    )
    
    params = {}
    params['passenger_age'] = int(input('        Age (1-99) > '))
    params['passenger_class'] = int(input('        Classe (1-3) > '))
    params['passenger_sex'] = str(input('        Sex (male/femme) > '))

    if params['passenger_age'] > 99 or params['passenger_age'] < 1:
        print("Error: The age of the passenger have to be between 1 and 99")
        return False
    elif params['passenger_class'] > 3 or params['passenger_class'] < 0:
        print("Error: The passenger class must be between 0 and 3")
        return False
    elif params['passenger_sex'] != 'male' or params['passenger_sex'] != 'female':
        print("Error: Le sex can only be male or female")
        return False
        pass

    if params['passenger_sex'] == 'male':
        params['passenger_sex'] = 0
    elif params['passenger_sex'] == 'female':
        params['passenger_sex'] = 1
        pass

    ai = AI({
        'passengers': passengers,
        'params': params
    })

    SurvivalRate = ai.checkSurvivalProbability()

    if SurvivalRate[0] == 0:
        print("\nThis passenger has not survived")
    else:
        print("\nThis passenger has survived")
        pass
    pass

if __name__ == "__main__":
    main()
    pass
