import pandas as pd
import matplotlib.pyplot as plt

df = pd.DataFrame()

"""
This module will display graphics related to the model analysis
"""

model_name = "1A"
MAE = 5446744.958506204
MSE =  83923732969054.39
R2 = 0.8898315285940438

df = df.append({'Model Name' : model_name, 'MAE': MAE, 'MSE' : MSE, 'R2' : R2}, ignore_index=True)

model_name = "1B"
MAE = 6510359.295252476
MSE = 128703883016857.42
R2 = 0.8310476720428234

df = df.append({'Model Name' : model_name, 'MAE': MAE, 'MSE' : MSE, 'R2' : R2}, ignore_index=True)

model_name = "1C"
MAE =  6826671.055202761
MSE = 139800484621651.05
R2 = 0.8164809268165145

df = df.append({'Model Name' : model_name, 'MAE': MAE, 'MSE' : MSE, 'R2' : R2}, ignore_index=True)

model_name = "2A"
MAE = 5000654.3852823675
MSE = 62938090903962.75
R2 = 0.9173798278175326

df = df.append({'Model Name' : model_name, 'MAE': MAE, 'MSE' : MSE, 'R2' : R2}, ignore_index=True)

model_name = "2B"
MAE = 4866175.18721627
MSE = 62772523738694.44
R2 = 0.9175971713610968

df = df.append({'Model Name' : model_name, 'MAE': MAE, 'MSE' : MSE, 'R2' : R2}, ignore_index=True)

model_name = "2C"
MAE = 12168562.4311785
MSE = 302366176340436.6
R2 = 0.6030774814965307

df = df.append({'Model Name' : model_name, 'MAE': MAE, 'MSE' : MSE, 'R2' : R2}, ignore_index=True)

model_name = "2D"
MAE = 5000654.375839841
MSE = 62938090742252.81
R2 = 0.9173798280298127

df = df.append({'Model Name' : model_name, 'MAE': MAE, 'MSE' : MSE, 'R2' : R2}, ignore_index=True)

model_name = "2E"
MAE = 4866175.178500091
MSE = 62772523082427.21
R2 = 0.9175971722225926

df = df.append({'Model Name' : model_name, 'MAE': MAE, 'MSE' : MSE, 'R2' : R2}, ignore_index=True)

model_name = "3A"
MAE = 5350076.32045551
MSE = 80190589634976.84
R2 = 0.8947321053451556

df = df.append({'Model Name' : model_name, 'MAE': MAE, 'MSE' : MSE, 'R2' : R2}, ignore_index=True)

model_name = "3B"
MAE = 5285811.017970941
MSE = 78072246562422.64
R2 = 0.8975128994061483

df = df.append({'Model Name' : model_name, 'MAE': MAE, 'MSE' : MSE, 'R2' : R2}, ignore_index=True)

model_name = "3C"
MAE = 5265249.379328696
MSE = 77552202576140.31
R2 = 0.8981955722211638

df = df.append({'Model Name' : model_name, 'MAE': MAE, 'MSE' : MSE, 'R2' : R2}, ignore_index=True)

model_name = "3D"
MAE = 5238076.622306542
MSE = 76643386393106.39
R2 = 0.8993885945776736


df = df.append({'Model Name' : model_name, 'MAE': MAE, 'MSE' : MSE, 'R2' : R2}, ignore_index=True)

model_name = "4A"
MAE = 5714080.609408106
MSE = 83419464538687.42
R2 = 0.8867555269546786

df = df.append({'Model Name' : model_name, 'MAE': MAE, 'MSE' : MSE, 'R2' : R2}, ignore_index=True)

model_name = "4B"
MAE = 5714738.324214123
MSE = 83906390476983.36
R2 = 0.8860945101092774


df = df.append({'Model Name' : model_name, 'MAE': MAE, 'MSE' : MSE, 'R2' : R2}, ignore_index=True)

model_name = "4C"
MAE = 5679050.234239865
MSE = 83830755360108.69
R2 = 0.8861971870924199


df = df.append({'Model Name' : model_name, 'MAE': MAE, 'MSE' : MSE, 'R2' : R2}, ignore_index=True)

model_name = "4D"
MAE = 5714080.609408106
MSE = 83419464538687.42
R2 = 0.8867555269546786

df = df.append({'Model Name' : model_name, 'MAE': MAE, 'MSE' : MSE, 'R2' : R2}, ignore_index=True)

print(df.head())

pd.set_option('display.float_format', lambda x: '%.3f' % x)

fig, ax = plt.subplots()
# ax.ticklabel_format(style='plain')
# plt.bar(df['Model Name'], df['MAE'])
# plt.show()
# plt.savefig('out_mae.png')

# plt.bar(df['Model Name'], df['MSE'])
# plt.show()
# plt.savefig('out_mse.png')

plt.bar(df['Model Name'], df['R2'], color='red')
plt.show()
plt.savefig('out_r2.png')