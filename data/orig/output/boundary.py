import numpy as np
from math import *
import pylab as pl
r=[
0.687577,
0.676901,
0.665197,
0.654094,
0.646847,
0.64644,
0.650196,
0.651424,
0.652102,
0.659642,
0.683005,
0.742056,
0.820856,
0.893835,
0.95584,
1.00661,
1.04588,
1.07307,
1.08929,
1.09909,
1.10617,
1.10675,
1.09726,
1.07996,
1.05891,
1.03142,
0.991081,
0.935228,
0.864771,
0.781975,
0.687577
]
z=[
0.387416,
0.25613,
0.177619,
0.118037,
0.0650413,
0.014642,
-0.033987,
-0.0850646,
-0.1447,
-0.215887,
-0.296645,
-0.348633,
-0.350153,
-0.328334,
-0.295102,
-0.254917,
-0.209187,
-0.159652,
-0.109357,
-0.0611169,
-0.0141787,
0.0335354,
0.0808553,
0.126964,
0.175283,
0.228014,
0.280742,
0.32697,
0.361434,
0.38143,
0.387416
]
r=np.array(r)
z=np.array(z)
rl=[
1.136,
1.1356,
0.970737,
0.964983,
0.671636,
0.666176,
0.624691,
0.624,
0.624,
0.624352,
0.67185,
0.67897,
0.964983,
0.970737,
1.1356,
1.136,
1.136
]
zl=[
0.542692,
0.54988,
0.746615,
0.75,
0.75,
0.745476,
0.703991,
0.696943,
-0.696456,
-0.70364,
-0.74947,
-0.75,
-0.75,
-0.746615,
-0.54988,
-0.542692,
0.542692
]
rl=np.array(rl)
zl=np.array(zl)
rx=[0.687577]
zx=[0.387416]
rx=np.array(rx)
zx=np.array(zx)
rxu=[0.687577]
zxu=[0.387416]
rxu=np.array(rxu)
zxu=np.array(zxu)
rs1=[0]
zs1=[0]
rs1=np.array(rs1)
zs1=np.array(zs1)
rs2=[0]
zs2=[0]
rs2=np.array(rs2)
zs2=np.array(zs2)
rsep1=[0]
zsep1=[0]
rsep1=np.array(rsep1)
zsep1=np.array(zsep1)
rsep2=[0]
zsep2=[0]
rsep2=np.array(rsep2)
zsep2=np.array(zsep2)
fig=pl.figure()
pl.plot(r,z,'-r',label='plasma boundary')
pl.plot(rl,zl,'+-b',label='limiter')
pl.plot(rx,zx,'or')
pl.plot(rxu,zxu,'or')
pl.plot(rs1,zs1,'or')
pl.plot(rs2,zs2,'or')
pl.plot(rsep1,zsep1,'or')
pl.plot(rsep2,zsep2,'or')
pl.legend(loc='best')
pl.title('plasma boundary')
pl.axis('equal')
fig.savefig('plasma_boundary.png')
pl.show()
