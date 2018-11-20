# -*- coding: utf-8 -*-
"""
Created on Wed Nov 14 10:24:54 2018
function:
    Provide parameters of hevc_nvenc
@author: ASUS
"""
# =============================================================================
# two definition: one is below, the orther is use of pure numbers
# en_parameter={'-preset': ['default', 'slow', 'medium', 'fast', 'hp', 'hq', 'bd',
#                        'll', 'llhq', 'llhp', 'lossless', 'losslesshp']}
# =============================================================================
en_parameter={'-preset': range(12)}
en_parameter.update({'-profile': range(5)})
en_parameter.update({'-level': ['auto', 1, 1.0, 2, 2.0, 2.1, 3, 3.0, 3.1, 4, 4.1,
                            5, 5.0, 5.1, 5.2, 6, 6.0, 6.1, 6.2]})
en_parameter.update({'-tier': ['main', 'high']})
en_parameter.update({'-rc': ['constqp', 'vbr', 'cbr', 'vbr_minqp', 'll_2pass_quality',
                          'll_2pass_size', 'vbr_2pass', 'cbr_ld_hq', 'cbr_hq', 'vbr_hq']})
en_parameter.update({'-cq': range(0, 51, 3)})
en_parameter.update({'-qp': range(-1, 3)})