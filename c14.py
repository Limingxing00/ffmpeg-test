# -*- coding: utf-8 -*-
"""
Created on Mon Nov 12 15:08:08 2018

@author: Ming
function:

in the two directories.
"""

import time
from c13 import *
from c15 import *
from c16 import *
from parameter import en_parameter
import numpy as np
import matplotlib.pyplot as plt


path1 = r'D:\Liu_Dong\Brain_map_compression\ZhangYueYi\raw_brain\test_jpg'
# path2 = r'D:\Liu_Dong\Brain_map_compression\ZhangYueYi\raw_brain'
path2 = r'D:\Liu_Dong\Brain_map_compression\ZhangYueYi\raw_brain\test_jpg_by_video'
ftype = 'jpg'
# Samples
outfile = 'z.mkv'

# The value of "-vcodecs" option.It's also the key of en_parameter
vcodec_option = '-preset'
# Provide traversable options(list)
en_value = en_parameter.get(vcodec_option)
cycle_num = len(en_value)
print('There are a total of %d operations'%cycle_num)

# Initialization module: instantiation
data_process = MyProcess(path1, path2, ftype)
compression = Codec(path1, path2, ftype)
psnr = Psnr(path1, path2, ftype)

# Just generate a set of samples for data_process.read_file(), please don't pay attention to z.mkv
compression.encoder(encoder='hevc_nvenc', vedio_file=outfile, option=vcodec_option)
compression.decoder(vedio_file=outfile)
img1, img2 = data_process.read_file()

# Traverse all values under the key of en_parameter
psnr_avr = []
result_psnr = []
result_time = []
for j in range(cycle_num):
    start = time.time()
    # Codec module
    compression.encoder(encoder='hevc_nvenc', vedio_file='output'+"%03d"%j+'.mkv', option=vcodec_option, value=en_value[j])
    compression.decoder(vedio_file='output'+"%03d"%j+'.mkv')
    end = time.time()
    print("%d end" % j)
    # Sample equally (step=4) to calculate PSNR, reducing time consumption while ensuring sample rationality
    for i in range(0, 819, 4):
        psnr0 = psnr.psnr_8bit(img1[i], img2[i])
        psnr_avr.append(psnr0)
    print('key='+str(j), 'psnr=',np.mean(psnr_avr), 'time=', str(end-start))

    result_psnr.append(np.mean(psnr_avr))
    result_time.append(end-start)
    psnr_avr = []

# Watch the final results simply
plt.figure(1)
plt.subplot(121)
plt.plot(result_psnr, 'o-', linewidth=2.0)
plt.title('avr_psnr of '+vcodec_option)
plt.subplot(122)
plt.plot(result_time, 'o-', linewidth=2.0)
plt.title('time of '+vcodec_option)
plt.show()