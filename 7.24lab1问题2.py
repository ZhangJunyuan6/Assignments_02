import numpy as np
import matplotlib.pyplot as plt

test=np.load('D:\dataX.npy')
print(test)

data = np.mean(test)
print(data)

data2=test-data
print(data2)

datamin=np.min(data2)
datajmin=data2-datamin
datamax=np.max(data2)
data_normalize=datajmin/datamax

plt.subplot(1,3,1)
plt.scatter(test[:, 0],test[:, 1],s=5)
plt.xlabel('test_x')
plt.ylabel('test_y')
plt.title('oringnal_data')

plt.subplot(1,3,2)
plt.scatter(data2[:, 0],data2[:, 1],s=5)
plt.xlabel('data_x')
plt.ylabel('data_y')
plt.title('mean_data')

plt.subplot(1,3,3)
plt.scatter(data_normalize[:, 0],data_normalize[:, 1],s=5)
plt.xlabel('guiyihua_x')
plt.ylabel('guiyihua_y')
plt.title('normalizid_data')
plt.show()
