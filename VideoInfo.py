# -*- coding: utf-8 -*-
"""
Created on Thu Nov 15 20:24:26 2018
@author: Ming

Function :
    Count the size of all videos under file_dir and save them in the current directory with the csv format.
"""
import os
import sys
import xlwt
import glob
# Video directory and video type
file_dir = r"D:\Liu_Dong\Brain_map_compression\ZhangYueYi\raw_brain\test_jpg_by_video"
ftype = "mkv"


class FileCheck(object):
 
    def __init__(self):
        self.file_dir = file_dir
        self.ftype = ftype

    def get_file(self):
        """
        get the filename from file_dir
        :return: filename that the type is list
        """
        file_dir = self.file_dir
        ftype = self.ftype
        img = glob.glob(file_dir+'\*.'+ftype)
        return img

    def get_filesize(self, filename):
        """
        Get file size (M: megabytes)
        """
        file_byte = os.path.getsize(filename)
        # return self.sizeConvert(file_byte)
        return file_byte / 1024 / 1024
    
# =============================================================================
#     def sizeConvert(self, size):
#         """
#         File size unit conversion
#         """
#         K, M, G = 1024, 1024**2, 1024**3
#         if size >= G:
#             return str(size/G)+'G Bytes'
#         elif size >= M:
#             return str(size/M)+'M Bytes'
#         elif size >= K:
#             return str(size/K)+'K Bytes'
#         else:
#             return str(size)+'Bytes'
# =============================================================================
        
    def write_csv(self, file_path):
        """
        write the info of file names and file sizes in the video.csv
        :param file_path: file path
        """
        datas = [[u'FileName', u'FileSize']]# Header is saved in a two-dimensional array
        for f in file_path:
            cell = []
            file_size = fc.get_filesize(f)
            f = f.split("\\")[-1]
            # file_times = fc.get_file_times(file_path.encode("gbk"))
            print ("FileName：{filename},FileSize：{filesize}".format(filename=f,filesize=file_size))
            cell.append(f)
            cell.append(file_size)
            datas.append(cell)
         
        wb = xlwt.Workbook() # Create a workbook
        sheet = wb.add_sheet('data')# sheet's name is test
             
        # Cell format in .csv
        style = 'pattern: pattern solid, fore_colour yellow; '# Background color is yellow
        style += 'font: bold on; '# Bold
        style += 'align: horz centre, vert center; '# Centered
        header_style = xlwt.easyxf(style)
             
        row_count = len(datas)
        col_count = len(datas[0])
        for row in range(0, row_count): 
            col_count = len(datas[row]) 
            for col in range(0, col_count):
                # Format the header cell
                if row == 0:
                    sheet.write(row, col, datas[row][col], header_style)
                else:
                    sheet.write(row, col, datas[row][col])
        wb.save(file_dir+'\\'+"video.csv")

# =============================================================================
#     def timeConvert(self,size):# 单位换算
#         M, H = 60, 60**2
#         if size < M:
#             return str(size)+u'秒'
#         if size < H:
#             return u'%s分钟%s秒'%(int(size/M),int(size%M))
#         else:
#             hour = int(size/H)
#             mine = int(size%H/M)
#             second = int(size%H%M)
#             tim_srt = u'%s小时%s分钟%s秒'%(hour,mine,second)
#             return tim_srt
# =============================================================================

if __name__ == "__main__":
    print ("...START...")
    fc = FileCheck()
    file_path = fc.get_file()
    fc.write_csv(file_path)
    print ("...END...")