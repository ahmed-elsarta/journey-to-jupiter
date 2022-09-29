# import numpy as np
import matplotlib.pyplot as plt

hazards = [0.2,0.4,0.6,0.8]
organismsForGravity = {
    'human': 4.8*hazards[0],
    'mice': 4*hazards[0],
    'rat': 3.5*hazards[0]
}
organismsForRadiation = {
    'dr': 2.4*hazards[1],
    'tard':2.1*hazards[1],
    'human':1.85*hazards[1]
}
organismsForDna = {
    'tard' : 1.55 * hazards[2],
    'nmr': 1.3* hazards[2],
    'mice':1.1* hazards[2]
}
organismsForeye = {
    'rbs': 1.2* hazards[3],
    'human':1* hazards[3],
    'eagle':0.8* hazards[3]
}
probabilities  = []
for keyG,valG in organismsForGravity.items():
    for keyR,valR in organismsForRadiation.items():
        for keyD,valD in organismsForDna.items():
            for keyE,valE in organismsForeye.items():
                probabilities.append(valG * valR * valD * valE)
                
                
print(probabilities)
plt.hist(probabilities)
plt.show()