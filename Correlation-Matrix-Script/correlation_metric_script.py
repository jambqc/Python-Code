#! /usr/bin/env python

import argparse
import os 
from sklearn.neighbors import DistanceMetric
import numpy as np
import pandas as pd

################################################################################
def my_pearson(X, Y):
    num = sum((X - X.mean()) * (Y - Y.mean()))
    denom = np.sqrt(sum((X-X.mean())**2) * sum((Y - Y.mean())**2))
    r = num / denom
    return r

p_dist = DistanceMetric.get_metric(my_pearson).pairwise

## (start) Pearson Correlation Function
######################################################################
# If the user does not specify the output location by using the flag -o then the 
# file will be saved in the current directory with the default name of:
# the name of the input file + Pearson_cor.tsv
# Examp: samp_df.tsv will be saved as samp_df_Pearson_cor.tsv
def Pearson(df, name = None, toFile = None):
    df = df.T
    P = df.corr(method = 'pearson')
    try:
        P.index = list(df.index)
        P.index.name = df.index.names
        P.columns = list(df.index)
    except:
        pass
    if toFile == None:
        P.to_csv(name, sep='\t')
        printStatement = """ The Pearson correlation metric was performed
        on the input file and the resulting correlation matrix will
        be saved in the current directory as: """ + name
        print(printStatement)
       
    else:
        P.to_csv(toFile, sep='\t')
        outFile = """The Pearson correlation metric was performed on the 
        input file and the resulting correlation matrix will be saved as: """
        outFile += toFile
        print(outFile)
######################################################################
## End Pearson Correlation

## (start) Czekanowski Index
######################################################################

def my_Czek(X,Y):
    X = np.array(X)
    Y = np.array(Y)

    Cz = 2 * sum(np.minimum(X, Y)) / sum(X + Y)
    return Cz

czek_dist = DistanceMetric.get_metric(my_Czek).pairwise

def Czekanowski(df, name = None, toFile = None):
    C = pd.DataFrame(czek_dist(df))
    try:
        C.index = list(df.index)
        C.index.name = df.index.names
        C.columns = list(df.index)
    except:
        pass
    if toFile == None:
        C.to_csv(name, sep='\t')
        printStatement = """ The Czekanowski correlation metric was 
        performed on the input file and the resulting correlation matrix 
        will be saved in the current diretory as : """ + name
        print(printStatement)
    else:
        C.to_csv(toFile, sep='\t')
        outFile = """ The Czekanowski correlation metric was performed 
        on the input file and the resulting correlation matrix
        will be saved as : """ + toFile
        print(outFile)
####################################################################
# End Czekanowski


# (start) Spearman Correlation
###################################################################
def Spearman(df, name = None, toFile = None):
    df = df.T
    S = df.corr(method='spearman')
    try:
        S.index = list(df.index)
        S.index.name = df.index.names
        S.columns = list(df.index)
    except:
        pass
    if toFile == None:
        
        S.to_csv(name, sep='\t')
        printStatement = """ Spearman correlation metric was
        performed on the input file and the resulting correlation
        matrix will be saved in the current directory as: """ + name
        print(printStatement)
    else:
        S.to_csv(toFile, sep='\t')
        printStatement =  """ The Spearman correlation metric was performed
		on the input file and the resulting correlation matrix will
		be saved as: """ + toFile

        print(printStatement)
###############################################################################
 #End Spearman


# Stringent Proportional Similarity (SPS)
###############################################################################
def my_sps(X, Y):
    X = np.array(X)
    Y = np.array(Y)
    id0 = np.logical_and((X != 0) , (Y != 0))
    sps = 1. - (1. / len(X)) * ( sum(np.absolute(X[id0]**2 - Y[id0]**2)/(X[id0]**2 + Y[id0]**2)) + sum(~id0) )
    
    return sps
sps_dist = DistanceMetric.get_metric(my_sps).pairwise

def SPS(df, name = None, toFile = None):
    Sp = pd.DataFrame(sps_dist(df))
    try:
        Sp.index = list(df.index)
        Sp.index.name = df.index.names
        Sp.columns = list(df.index)
    except:
        pass
    if toFile == None:
        Sp.to_csv(name,  sep='\t')
        printStatement = """ The SPS correlation metric was
        performed on the input file and the resulting correlation
        matrix will be saved in the current directory as: """ + name
        print(printStatement)
    else:
        Sp.to_csv(toFile, sep='\t')
        outFile = """ The SPS correlation  metric was performed 
        on the input file and the resulting correlation matrix 
        will be saved as: """ + toFile
        print(outFile)
###############################################################################
# End SPS


def Main():
    parser = argparse.ArgumentParser()
    
    parser.add_argument('inputFile', help= """The inputFile argument specifies which
            dataframe you are reading in to perform a correlation test on.""")

    parser.add_argument('CorFunc' , help= """The CorFunc argument specifies which 
    correlation metric to perform on the input file. The options are: 
            <Pearson>, <Spearman>, <Czekanowski>, or <SPS>.""" )
    
    parser.add_argument('-o' , '--output', help="""This is an optional 
            argument that specifies where your output file 
            (a correlation matrix) should be written to. 
            Default is the current working directory.""", type=str)

    args = parser.parse_args()
    try:
        df = pd.read_csv(args.inputFile, sep='\t', index_col=0, skipinitialspace=True)
    except OSError:
        errorStatement = "This input file: " + args.inputFile + """
         does not exist."""
        print(errorStatement)
################################################################################
    if args.CorFunc == 'Pearson':
        if args.output:
            toFile = args.output
            return Pearson(df = df, toFile = toFile)
        else: 
            name = os.path.splitext(args.inputFile)[0] + "_Pearson_cor.tsv"
            return Pearson(df = df, name = name)
################################################################################
    elif args.CorFunc == 'Czekanowski':
        if args.output:
            toFile = args.output
            return Czekanowski(df = df, toFile = toFile)
        else:
            name = os.path.splitext(args.inputFile)[0] + "_Czekanowski_cor.tsv"
            return Czekanowski(df = df, name = name)
################################################################################

################################################################################
    elif args.CorFunc == 'Spearman':
        if args.output:
            toFile = args.output
            return Spearman(df = df, toFile = toFile)
        else:
            name = os.path.splitext(args.inputFile)[0] + "_Spearman_cor.tsv"
            return Spearman(df = df, name = name)
################################################################################

################################################################################
    elif args.CorFunc == 'SPS':
        if args.output:
            toFile = args.output
            return SPS(df = df, toFile = toFile)
        else:
            name = os.path.splitext(args.inputFile)[0] + "_SPS_cor.tsv"
            return SPS(df = df, name = name)
################################################################################

    else:
       print("Invalid entry for the argument specifying the " + \
       "correlation function. Please see help for this " + \
       "script by typing: <python ex1.py -h>.")

if __name__=='__main__':
    Main()

