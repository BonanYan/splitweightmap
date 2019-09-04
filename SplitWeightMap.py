"""
splitweightmap
Copyright (C) 2019 Bonan Yan

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np
import math

def SplitWeightMap (rMatrix : np.array, nLim : int):
    r, c = rMatrix.shape
    cAll = rMatrix.sum(axis=0)
    cNew = np.array([math.ceil(z) for z in cAll/nLim]).sum()
    
    rMatrixSplitted = np.zeros((r,cNew))
    j_cNew = 0
    for i in range(c):
        tmpPointer = 0 
        if cAll[i]<=nLim:
            
            rMatrixSplitted[:,j_cNew] = rMatrix[:,i]
            j_cNew += 1
            
        else:
            
            while tmpPointer<r:
                deltaK = 1
                
                while rMatrix[tmpPointer:tmpPointer+deltaK,i].sum(axis=0)<nLim and tmpPointer+deltaK<r:
                    deltaK+=1 
                    
                if rMatrix[tmpPointer:tmpPointer+deltaK,i].sum(axis=0)==0:
                    break
                else:
                    rMatrixSplitted[tmpPointer:tmpPointer + deltaK,j_cNew] = \
                    rMatrix[tmpPointer:tmpPointer + deltaK,i] 
                    tmpPointer+=deltaK
                    j_cNew += 1
    return rMatrixSplitted

        
        
        
        
        
        
        
        
        
        
        