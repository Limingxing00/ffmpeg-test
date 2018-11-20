# -*- coding: utf-8 -*-
"""
Created on Tue Nov 13 11:20:22 2018

@author: ASUS
"""
import os
from c13 import MyProcess
from subprocess import run


class Codec(MyProcess):
    def __init__(self, path1, path2, ftype):
        super(Codec, self).__init__(path1, path2, ftype)
        #self.outfile = outfile

    def encoder(self, encoder, vedio_file, option, value=0):
        """
        Simulate ffmpeg shell command
        :param encoder: like hevc, libx265 and hevc_nvenc
        :param vedio_file: veidio name
        :param option: The parameter that need to be changed, like -qp, -preset
        :param value: The value of the option
        """
        in_file_path = self.path1
        out_file_path = self.path2
        # outfile = self.outfile
        ftype = self.ftype
        command = 'ffmpeg.exe -y -i '+in_file_path+'\%05d.'+ftype+' -vcodec '+encoder+' '+option+' '+str(value)+' '+out_file_path+'\\'+vedio_file
        # command = 'ffmpeg.exe -y -i '+in_file_path+'\%05d.'+ftype+' -vcodec '+encoder+' '+out_file_path+'\\'+outfile+' '+option+' '+str(value)
        run(command)
    
    def decoder(self, vedio_file):
        """
        Simulate ffmpeg shell command(Default parameters)
        :param vedio_file: veidio name
        """
        in_file_path = self.path2
        out_file_path = self.path2
        # outfile = self.outfile
        ftype = self.ftype
        command = 'ffmpeg.exe -y -i '+in_file_path+'\\'+vedio_file+' '+out_file_path+'\\'+'\%05d.'+ftype
        run(command)
