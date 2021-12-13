import pandas as pd
import numpy as np
from scipy import stats
import scikit_posthocs

from matplotlib.ticker import MaxNLocator
import matplotlib.pyplot as plt
SMALL_SIZE = 14
BIGGER_SIZE = 26

plt.rc('axes', titlesize=BIGGER_SIZE)     # fontsize of the axes title
plt.rc('axes', labelsize=BIGGER_SIZE)    # fontsize of the x and y labels
plt.rc('xtick', labelsize=BIGGER_SIZE)    # fontsize of the tick labels
plt.rc('ytick', labelsize=BIGGER_SIZE)    # fontsize of the tick labels
plt.rc('legend', fontsize=SMALL_SIZE)    # legend fontsize
plt.rc('figure', titlesize=BIGGER_SIZE)  # fontsize of the figure title

WS = pd.read_excel('PPS.xlsx')
WS_np = np.array(WS)

#print(WS.loc[:,[4,5]])

#print(stats.kruskal(WS.iloc[:,[5]],WS.iloc[:,[10]]))

#print(stats.mannwhitneyu(WS.iloc[:,[5]],WS.iloc[:,[10]]))

#############################################################################################################################

# Test for how well companies keep your privacy

# print('Test for how well companies keep your privacy')
how_well_ins = [x for x in WS.iloc[:,5].tolist() + WS.iloc[:,10].tolist() + WS.iloc[:,15].tolist() if np.isnan(x) == False]

how_well_snap = [x for x in WS.iloc[:,20].tolist() + WS.iloc[:,25].tolist() + WS.iloc[:,30].tolist() if np.isnan(x) == False]

how_well_tt = [x for x in WS.iloc[:,65].tolist() + WS.iloc[:,70].tolist() + WS.iloc[:,75].tolist() if np.isnan(x) == False]

how_well_fb = [x for x in WS.iloc[:,35].tolist() + WS.iloc[:,40].tolist() + WS.iloc[:,45].tolist() if np.isnan(x) == False]

how_well_gm = [x for x in WS.iloc[:,50].tolist() + WS.iloc[:,55].tolist() + WS.iloc[:,60].tolist() if np.isnan(x) == False]

# print(stats.kruskal(how_well_fb, how_well_tt, how_well_gm, how_well_snap, how_well_ins))
#
# print(scikit_posthocs.posthoc_dunn([how_well_ins, how_well_snap, how_well_fb, how_well_gm, how_well_tt]))

#############################################################################################################################

# # Test for how long companies keep your privacy

# print("Test for how long companies keep your privacy")
how_long_ins = [x for x in WS.iloc[:,4].tolist() + WS.iloc[:,9].tolist() + WS.iloc[:,14].tolist() if np.isnan(x) == False]

how_long_snap = [x for x in WS.iloc[:,19].tolist() + WS.iloc[:,24].tolist() + WS.iloc[:,29].tolist() if np.isnan(x) == False]

how_long_tt = [x for x in WS.iloc[:,64].tolist() + WS.iloc[:,69].tolist() + WS.iloc[:,74].tolist() if np.isnan(x) == False]

how_long_fb = [x for x in WS.iloc[:,34].tolist() + WS.iloc[:,39].tolist() + WS.iloc[:,44].tolist() if np.isnan(x) == False]

how_long_gm = [x for x in WS.iloc[:,49].tolist() + WS.iloc[:,54].tolist() + WS.iloc[:,59].tolist() if np.isnan(x) == False]

# print(stats.kruskal(how_long_fb, how_long_tt, how_long_gm, how_long_snap, how_long_ins))
#
# print(scikit_posthocs.posthoc_dunn([how_long_ins, how_long_snap, how_long_fb, how_long_gm, how_long_tt]))

#############################################################################################################################

# Test for 3rd party access
#print("Test for 3rd party access")
third_ins = [x for x in WS.iloc[:,6].tolist() + WS.iloc[:,11].tolist() + WS.iloc[:,16].tolist() if np.isnan(x) == False]

third_snap = [x for x in WS.iloc[:,21].tolist() + WS.iloc[:,26].tolist() + WS.iloc[:,31].tolist() if np.isnan(x) == False]

third_tt = [x for x in WS.iloc[:,66].tolist() + WS.iloc[:,71].tolist() + WS.iloc[:,76].tolist() if np.isnan(x) == False]

third_fb = [x for x in WS.iloc[:,36].tolist() + WS.iloc[:,41].tolist() + WS.iloc[:,46].tolist() if np.isnan(x) == False]

third_gm = [x for x in WS.iloc[:,51].tolist() + WS.iloc[:,56].tolist() + WS.iloc[:,61].tolist() if np.isnan(x) == False]

# print(stats.kruskal(third_fb, third_tt, third_gm, third_snap, third_ins))
#
# print(scikit_posthocs.posthoc_dunn([third_ins, third_snap, third_fb, third_gm, third_tt]))

#############################################################################################################################

# Test for strictly following
#print("Test for strictly following")
strict_ins = [x for x in WS.iloc[:,7].tolist() + WS.iloc[:,12].tolist() + WS.iloc[:,17].tolist() if np.isnan(x) == False]

strict_snap = [x for x in WS.iloc[:,22].tolist() + WS.iloc[:,27].tolist() + WS.iloc[:,32].tolist() if np.isnan(x) == False]

strict_tt = [x for x in WS.iloc[:,67].tolist() + WS.iloc[:,72].tolist() + WS.iloc[:,77].tolist() if np.isnan(x) == False]

strict_fb = [x for x in WS.iloc[:,37].tolist() + WS.iloc[:,42].tolist() + WS.iloc[:,47].tolist() if np.isnan(x) == False]

strict_gm = [x for x in WS.iloc[:,52].tolist() + WS.iloc[:,57].tolist() + WS.iloc[:,62].tolist() if np.isnan(x) == False]

# print(stats.kruskal(strict_fb, strict_tt, strict_gm, strict_snap, strict_ins))
#
# print(scikit_posthocs.posthoc_dunn([strict_ins, strict_snap, strict_fb, strict_gm, strict_tt]))

#############################################################################################################################

# plotting multibar histograms， due to MaxNlocator issues plotting one at a time is prefered
X = ['Instagram', 'Snapchat', 'Facebook', 'Groupme', 'Tiktok']

# ax = plt.figure().gca()
# ax.yaxis.set_major_locator(MaxNLocator(integer=True))
# ax.xaxis.set_major_locator(MaxNLocator(integer=True))
# plt.hist([[int(x) for x in how_long_ins], [int(x) for x in how_long_snap],[int(x) for x in how_long_fb],[int(x) for x in how_long_gm],[int(x) for x in how_long_tt]],range=[-0.5, 6.5] ,bins=7,edgecolor="black",label=['Instagram', 'Snapchat', 'Facebook', 'Groupme', 'Tiktok'])
# plt.xlabel('Years')
# plt.ylabel('Counts')
# plt.tight_layout()
# #plt.title('How long do you think companies keep your privacy?')
# plt.legend(loc='upper center')
# plt.show()


ax = plt.figure().gca()
ax.xaxis.set_major_locator(MaxNLocator(integer=True))
plt.hist([[int(x) for x in how_well_ins], [int(x) for x in how_well_snap],[int(x) for x in how_well_fb],[int(x) for x in how_well_gm],[int(x) for x in how_well_tt]], range=[0.8,5.2],bins=9,edgecolor="black",label=['Instagram', 'Snapchat', 'Facebook', 'Groupme', 'Tiktok'])
plt.xlabel('Scores')
plt.ylabel('Counts')
plt.tight_layout()
#plt.title('How well do you think Companies keep your privacy?')
ax.legend()
plt.show()


# ax = plt.figure().gca()
# ax.yaxis.set_major_locator(MaxNLocator(integer=True))
# ax.xaxis.set_major_locator(MaxNLocator(integer=True))
# plt.hist([['Yes' if int(x) ==1 else 'No' for x in third_ins], ['Yes' if int(x) ==1 else 'No' for x in third_snap],['Yes' if int(x) ==1 else 'No'for x in third_fb],['Yes' if int(x) ==1 else 'No' for x in third_gm],['Yes' if int(x) ==1 else 'No' for x in third_tt]] , bins=3,edgecolor="black",label=['Instagram', 'Snapchat', 'Facebook', 'Groupme', 'Tiktok'])
# plt.xlabel('Opinions')
# plt.ylabel('Counts')
# plt.tight_layout()
# #plt.title('Do you think there is any mention of third companies accessing your data?')
# ax.legend(loc='upper center', bbox_to_anchor=(0.5, 1.05),
#           ncol=2, fancybox=True)
# plt.show()

# ax = plt.figure().gca()
# ax.yaxis.set_major_locator(MaxNLocator(integer=True))
# ax.xaxis.set_major_locator(MaxNLocator(integer=True))
# plt.hist([['Yes' if int(x) ==1 else 'No' for x in strict_ins], ['Yes' if int(x) ==1 else 'No' for x in strict_snap],['Yes' if int(x) ==1 else 'No'for x in strict_fb],['Yes' if int(x) ==1 else 'No' for x in strict_gm],['Yes' if int(x) ==1 else 'No' for x in strict_tt]], bins=3,edgecolor="black",label=['Instagram', 'Snapchat', 'Facebook', 'Groupme', 'Tiktok'])
# plt.xlabel('Opinions')
# plt.ylabel('Counts')
# plt.tight_layout()
# #plt.title('Do you think companies strictly follow their user agreement?')
# ax.legend(loc='upper center', bbox_to_anchor=(0.5, 1.05),
#           ncol=2, fancybox=True)
# plt.show()
