import matplotlib.pyplot as plt
import re

# with open('./ckpts/wrn28-dr_0.3-wd_0.0001/console.log', 'r') as f:
#     logs = f.readlines()

# times, losses, accs = [], [], []
# for log in logs:

#     if log.startswith('---> Epoch'):
#         times.append(int(re.findall(r'[\d]+', log)[1]))

#     if log.startswith('[cla loss:'):
#         losses.append(float(re.findall('[\d]*[.][\d]+', log)[0]))
#         accs.append(float(re.findall('[\d]*[.][\d]+', log)[1]))

# # print(len(times), len(losses), len(accs))
# plt.plot(times, losses[::2], 'r',marker='.', markersize=10)
# plt.plot(times, losses[1::2], 'b', marker='.', markersize=10)
# plt.title('Loss with time')
# plt.xlabel('Time (s)')
# plt.ylabel('Loss')

# plt.legend(['Training', 'Test'])
# plt.savefig('Loss.png')

# plt.clf()
# plt.plot(times, accs[::2], 'r',marker='.', markersize=10)
# plt.plot(times, accs[1::2], 'b', marker='.', markersize=10)
# plt.title('Accuracy with time')
# plt.xlabel('Time (s)')
# plt.ylabel('Accuracy (%)')

# plt.legend(['Training', 'Test'])
# plt.savefig('Accuracy.png')
def plot_accs(t, x, y, n):
    plt.clf()
    plt.plot(t, x, 'r',marker='.', markersize=10)
    plt.plot(t, y, 'b', marker='.', markersize=10)
    plt.title('Accuracy')
    plt.xlabel('Parameter')
    plt.ylabel('Accuracy (%)')

    plt.legend(['Training', 'Test'])
    plt.savefig(n)

dp = [0.0, 0.1, 0.2, 0.4, 0.8, 1.0]
train_accs = [98.68, 98.34, 97.93, 95.89, 88.54, 64.6]
test_accs = [90.26, 90.11, 90.46, 89.08, 71.77, 52.99]

plot_accs(dp, train_accs, test_accs, 'dp.png')

wd = [0.0001, 0.0002, 0.0005, 0.001, 0.002]
train_accs = [98.68, 98.96, 98.78, 97.85, 89.77]
test_accs = [90.26, 91.4, 91.00, 90.61, 87.44]
plot_accs(wd, train_accs, test_accs, 'wd.png')