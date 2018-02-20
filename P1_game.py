
import numpy as np

class game:
    def __init__(self, prob_h):
        "prob_h=probability of getting a head side"
        self._prob_h = prob_h
        self.list = []
        self._n_success = 0
        self.expected_value = 0


    def simulate(self,n_times):

        t = 0

        while t < n_times:
            if  np.random.sample() <  self._prob_h:
                self.list.append('H')
            else:
                self.list.append('T')

            t +=1


    def get_expected_value(self):

        i = 0
        while i < len(self.list) - 2 :
            if self.list[i]=='T' and self.list[i+1] == 'T'and self.list[i+2] == 'H':
                        self._n_success +=1
            i +=1

        #print(self.list)
        #print(self._n_success)


        self.expected_value = -250 + self._n_success * 100

        return self.expected_value

class trial:
     def __init__(self, TrialTimes,n_times, prob_h):
         self._trialTimes = TrialTimes
         self._prob_h = prob_h
         self._expectedValue = []

         for i in range(TrialTimes):
             myGame = game(prob_h)
             myGame.simulate(n_times)
             self._expectedValue.append(myGame.get_expected_value())
             #print(self._expectedValue)

            
     def get_ave_expected_cost(self):
        return sum(self._expectedValue)/len(self._expectedValue)