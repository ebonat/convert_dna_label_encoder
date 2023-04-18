
import sys
import time
import traceback
import numpy as np
import pandas as pd
from sklearn.preprocessing import LabelEncoder 
import os
os.system("cls")

import warnings
warnings.filterwarnings("ignore")

class ConvertDNALabelEncoder(object):
    """
        convert dna sequence string csv file to dna label encoder csv file and viceverse
    """
    def __init__(self):
        pass
    
    @staticmethod
    def convert_dna_string_to_dna_labelencoder(dna_string_csv_path, dna_labelencoder_csv_path):
        """
            convert dna sequence string csv file to dna label encoder csv file
        args:
            dna_string_csv_path (string): dna string csv file path
            dna_labelencoder_csv_path (string): dna label encoder csv file path
        returns:
            none
        """
        try: 
            df_dna_string = pd.read_csv(filepath_or_buffer=dna_string_csv_path)       
            label_encoder = LabelEncoder()
            dna_string_list = [] 
            for row in df_dna_string.itertuples():
                dna_string_row = row.dna_sequence       
                dna_string_nparray = np.array(list(dna_string_row))        
                dna_labelencoder_row = label_encoder.fit_transform(dna_string_nparray)       
                dna_string_list.append(dna_labelencoder_row)  
            df_dna_labelencoder = pd.DataFrame(dna_string_list)  
            df_dna_labelencoder.to_csv(path_or_buf=dna_labelencoder_csv_path, index=False, header=None)               
        except:
            print("An error occurred. {}".format(ConvertDNALabelEncoder.get_exception_stack_trace()))       

    @staticmethod
    def convert_dna_labelencoder_to_dna_string(dna_labelencoder_csv_path, dna_string_csv_path):
        """
            convert dna sequence label encoder csv file to dna string csv file
        args:
            dna_labelencoder_csv_path (string): dna label encoder csv file path
            dna_string_csv_path (string): dna string csv file path
        """
        try:
            df_dna_labelencoder = pd.read_csv(filepath_or_buffer=dna_labelencoder_csv_path, header=None)
            dna_labelencoder_list = df_dna_labelencoder.values.tolist()
            dna_string_list = []
            for item in dna_labelencoder_list:       
                dna_string = ""
                for column in item:           
                    if column == 0:
                        nucleotide_letter = "A"
                    elif column == 1:
                        nucleotide_letter = "C"
                    elif column == 2:
                        nucleotide_letter = "G"
                    elif column == 3:
                        nucleotide_letter = "T"
                    dna_string += nucleotide_letter
                dna_string_list.append(dna_string)        
            df_dna_string = pd.DataFrame(dna_string_list) 
            df_dna_string.to_csv(path_or_buf=dna_string_csv_path, index=False, header=None)           
        except:
            print("An error occurred. {}".format(ConvertDNALabelEncoder.get_exception_stack_trace()))         

    @staticmethod
    def get_exception_stack_trace():   
        """
            get exception stack trace
        args:
            none
        returns:
            exception_stack_trace (string): exception stack trace parameters
        """
        try:     
            exception_type, exception_value, exception_traceback = sys.exc_info()               
            file_name, line_number, procedure_name, line_code = traceback.extract_tb(exception_traceback)[-1]           
            exception_stack_trace = ''.join('[Time Stamp]: ' + str(time.strftime('%d-%m-%Y %I:%M:%S %p')) + '' + '[File Name]: ' + str(file_name) + ' '
            + '[Procedure Name]: ' + str(procedure_name) + ' '
            + '[Error Message]: ' + str(exception_value) + ' '  
            + '[Error Type]: ' + str(exception_type) + ' '                                                                                                                                
            + '[Line Number]: ' + str(line_number) + ' '
            + '[Line Code]: ' + str(line_code))               
        except:
            print("An error occurred in {}".format("get_exception_stack_trace() function"))
        return exception_stack_trace

    @staticmethod
    def get_program_running(start_time):
        """
            calculate program running
        args:
            start_time (string): start time program runtime
        returns:
            none
        """
        try:
            end_time = time.time()
            diff_time = end_time - start_time
            result = time.strftime("%H:%M:%S", time.gmtime(diff_time)) 
            print("program runtime: {}".format(result))
        except:
            print("An error occurred. {}".format(ConvertDNALabelEncoder.get_exception_stack_trace()))       