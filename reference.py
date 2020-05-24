from PIL import Image, ImageFilter
import numpy

class Agent:
    # The default constructor for Agent
    def __init__(self):
        self.setSelections = {}
        self.setProblem = {}
        self.blackWhiteThreshold = 255
        self.minDiffThreshold = 10.0
        self.minSimThreshold = 25.0
        self.simThreshold = 40.0
        self.nDiff = 1.0
        pass
    
    def setupProblem(self, problem):
        for key, obj in problem.figures.items():
            ravensImg = numpy.array(Image.open(obj.visualFilename).convert('L'))
            ravensImg[ravensImg < self.blackWhiteThreshold] = 0    # Black
            ravensImg[ravensImg >= self.blackWhiteThreshold] = 1 # White
            if key.isalpha():
                self.setProblem[key] = ravensImg
            elif key.isdigit:
                self.setSelections[key] = ravensImg
    
    def crtBin(self, Ar):
        Ar[Ar < self.blackWhiteThreshold] = 0    # Black
        Ar[Ar >= self.blackWhiteThreshold] = 1 # White
        return Ar
        

    def mergeDict(self, *dicts):
        mergedict = {}
        for dict in dicts:
            for key in dict:
                try:
                    mergedict[key].append(dict[key])
                except KeyError:
                    mergedict[key] = [dict[key]]
        return mergedict
    
    def euclidDisttance(self,Ar1, Ar2):
        eucDistance = numpy.sqrt(numpy.sum(numpy.power(Ar1-Ar2, 2)))
        return eucDistance

    def PatternMatch2rc(self):
        self.ABDistance=self.euclidDisttance(self.setProblem['A'],self.setProblem['B'])
        self.ACDistance=self.euclidDisttance(self.setProblem['A'],self.setProblem['C'])
        self.BCDistance=self.euclidDisttance(self.setProblem['B'],self.setProblem['C'])
        self.diffBCAB=abs(self.BCDistance - self.ABDistance)
        self.diffBCAC=abs(self.BCDistance - self.ACDistance)
        self.sumBCAB=self.BCDistance + self.ABDistance
        self.sumBCAC=self.BCDistance + self.ACDistance
        
    def PatternMatch3rc(self):
        #horizontal
        self.ABDistance=self.euclidDisttance(self.setProblem['A'],self.setProblem['B'])
        self.BCDistance=self.euclidDisttance(self.setProblem['B'],self.setProblem['C'])
        self.DEdist=self.euclidDisttance(self.setProblem['D'],self.setProblem['E'])
        self.EFdist=self.euclidDisttance(self.setProblem['E'],self.setProblem['F'])
        self.GHdist=self.euclidDisttance(self.setProblem['G'],self.setProblem['H'])
        #vertical
        self.ADdist=self.euclidDisttance(self.setProblem['A'],self.setProblem['D'])
        self.DGdist=self.euclidDisttance(self.setProblem['D'],self.setProblem['G'])
        self.BEdist=self.euclidDisttance(self.setProblem['B'],self.setProblem['E'])
        self.EHdist=self.euclidDisttance(self.setProblem['E'],self.setProblem['H'])
        self.CFdist=self.euclidDisttance(self.setProblem['C'],self.setProblem['F'])
        #diagonal
        self.CEdist=self.euclidDisttance(self.setProblem['C'],self.setProblem['E'])
        self.EGdist=self.euclidDisttance(self.setProblem['E'],self.setProblem['G'])
        self.AEdist=self.euclidDisttance(self.setProblem['A'],self.setProblem['E'])
        self.BDdist=self.euclidDisttance(self.setProblem['B'],self.setProblem['D'])
        self.FHdist=self.euclidDisttance(self.setProblem['F'],self.setProblem['H'])
        self.BFdist=self.euclidDisttance(self.setProblem['B'],self.setProblem['F'])
        self.DHdist=self.euclidDisttance(self.setProblem['D'],self.setProblem['H'])
        #skipping mid array
        self.CGdist=self.euclidDisttance(self.setProblem['C'],self.setProblem['G'])
        self.ACDistance=self.euclidDisttance(self.setProblem['A'],self.setProblem['C'])
        self.DFdist=self.euclidDisttance(self.setProblem['D'],self.setProblem['F'])
        self.AGdist=self.euclidDisttance(self.setProblem['A'],self.setProblem['G'])
        self.BHdist=self.euclidDisttance(self.setProblem['B'],self.setProblem['H'])
        #horizontal diff
        self.hABBC=abs(self.ABDistance-self.BCDistance)
        self.hDEEF=abs(self.DEdist-self.EFdist)
        #vertical diff
        self.vADDG=abs(self.ADdist-self.DGdist)
        self.vBEEH=abs(self.BEdist-self.EHdist)
        #skip mid array
        self.sACDF=abs(self.ACDistance-self.DFdist)
        self.sAGBH=abs(self.AGdist-self.BHdist)
        self.sBCGH=abs(self.BCDistance-self.GHdist)
        #diag diff
        self.dCEEG=abs(self.CEdist-self.EGdist)
        self.dAECE=abs(self.AEdist-self.CEdist)
        self.dAEEG=abs(self.AEdist-self.EGdist)
        self.dBDCE=abs(self.BDdist-self.CEdist)
        self.dBDCG=abs(self.BDdist-self.CGdist)
        self.dCGFH=abs(self.CGdist-self.FHdist)
        self.dBFDH=abs(self.BFdist-self.DHdist)

    def solveHelper(self):
        
        self.PatternMatch2rc()
        if self.ABDistance < self.minSimThreshold:
            findInt = {}
            for key, im in self.setSelections.items():
                findInt[key]=abs((self.euclidDisttance(self.setProblem['C'], im ))-self.ABDistance)
            return int(min(findInt, key=findInt.get))
        
        if self.ACDistance < self.minSimThreshold:
            findInt = {}
            for key, im in self.setSelections.items():
                findInt[key]=abs((self.euclidDisttance(self.setProblem['B'], im ))-self.ACDistance)
            return int(min(findInt, key=findInt.get))
        
        #flipped A:B
        if self.euclidDisttance(numpy.fliplr(self.setProblem['A']), self.setProblem['B']) < self.minSimThreshold:
            findInt={}
            for key, im in self.setSelections.items():
                findInt[key]=abs(self.euclidDisttance(numpy.fliplr(self.setProblem['C']), im )-self.euclidDisttance(numpy.fliplr(self.setProblem['A']), self.setProblem['B']))
            return int((min(findInt, key=findInt.get)))

        else:
            findInt = {}
            for key, im in self.setSelections.items():
                findInt[key]=abs((self.euclidDisttance(self.setProblem['A'], im ))-self.BCDistance)
            return int(min(findInt, key=findInt.get))

    def prob3x3(self):

        self.PatternMatch3rc()
        if self.ACDistance < self.minSimThreshold and self.DFdist < self.minSimThreshold:
            findInt = {}
            for key, im in self.setSelections.items():
                findInt[key]=abs(self.euclidDisttance(self.setProblem['G'], im )-self.ACDistance)
            ar= int(min(findInt, key=findInt.get))
            return ar
        
        if self.AGdist < self.minSimThreshold and self.BHdist < self.minSimThreshold:
            findInt = {}
            for key, im in self.setSelections.items():
                findInt[key]=abs((self.euclidDisttance(self.setProblem['C'], im ))-self.AGdist)
            ar= int(min(findInt, key=findInt.get))
            return ar
        
        #horizontal flipped
        flACdist=self.euclidDisttance(numpy.fliplr(self.setProblem['A']),self.setProblem['C'])
        flDFdist=self.euclidDisttance(numpy.fliplr(self.setProblem['D']),self.setProblem['F'])
        horizontalDiff=abs(flACdist-flDFdist)
        predictI=abs(horizontalDiff+flDFdist)
        if flACdist < self.minSimThreshold and flDFdist < self.minSimThreshold and flDFdist > flACdist:
            findInt = {}
            for key, im in self.setSelections.items():
                findInt[key]=abs(self.euclidDisttance(numpy.fliplr(self.setProblem['G']), im )-predictI)
            ar= int(min(findInt, key=findInt.get))
            return ar
        
        #diagonal flip
        flCGdist=self.euclidDisttance(numpy.fliplr(self.setProblem['C']),self.setProblem['G'])
        flFHdist=self.euclidDisttance(numpy.fliplr(self.setProblem['F']),self.setProblem['H'])
        flBDdist=self.euclidDisttance(numpy.fliplr(self.setProblem['B']),self.setProblem['D'])
        if flCGdist < self.minSimThreshold and flFHdist < self.minSimThreshold and flBDdist < self.minSimThreshold \
        and self.CEdist > self.minSimThreshold:
            diagonalDiff=abs(self.dBDCG - self.dCGFH)
            predictI=diagonalDiff+self.AEdist
            findInt = {}
            for key, im in self.setSelections.items():
                findInt[key]=abs(self.euclidDisttance(self.setProblem['E'], im )-predictI)
            ar= int(min(findInt, key=findInt.get))
            return ar
        
        #diagonal rotate
        rDBdist=self.euclidDisttance(numpy.rot90(self.setProblem['D'],k=1),self.setProblem['B'])
        rGCdist=self.euclidDisttance(numpy.rot90(self.setProblem['G'],k=1),self.setProblem['C'])
        rHFdist=self.euclidDisttance(numpy.rot90(self.setProblem['H'],k=1),self.setProblem['F'])
        if rDBdist < self.minSimThreshold and rGCdist < self.minSimThreshold and rHFdist < self.minSimThreshold \
        and self.CEdist > self.minSimThreshold:
            diagonalDiff=abs(self.dBDCG - self.dCGFH)
            predictI=diagonalDiff+self.AEdist
            findInt = {}
            for key, im in self.setSelections.items():
                findInt[key]=abs(self.euclidDisttance(self.setProblem['E'], im )-predictI)
            ar= int(min(findInt, key=findInt.get))
            return ar
            
            
        #diagonal with h E:F > v E:H - high similarity A:E
        if self.hABBC > self.vADDG and self.EFdist > self.EHdist \
        and self.DHdist < self.simThreshold and self.AEdist < self.simThreshold and self.AEdist < self.DHdist:
            findInt = {}
            for key, im in self.setSelections.items():
                findInt[key]=abs(self.euclidDisttance(self.setProblem['E'], im )-self.AEdist)
            ar =int(min(findInt, key=findInt.get))
            return ar

        #incrementing horizontally rows of arrays by rows of 
        #incrementing with E:F < E:H diagonal high similarity F:H
        if self.hABBC > self.vADDG and \
        self.ADdist > self.DGdist and self.BEdist < self.EHdist and self.vBEEH > self.vADDG \
        and self.ADdist > self.BEdist > self.CFdist and self.FHdist < self.simThreshold:
            findInt = {}
            for key, im in self.setSelections.items():
                findInt[key]=abs(self.euclidDisttance(self.setProblem['H'], im )-self.FHdist)
            ar =int(min(findInt, key=findInt.get))
            return ar
        
        #decreasing difference and mid increment hE:F > vE:H
        if self.hABBC < self.vADDG and \
        self.ABDistance <= self.BCDistance and self.DEdist <= self.EFdist and self.hDEEF < self.hABBC \
        and self.EFdist > self.EHdist and self.DHdist < self.simThreshold:
            findInt={}
            for key, im in self.setSelections.items():
                findInt[key]=abs(self.DHdist-self.euclidDisttance(self.setProblem['E'], im ))
            ar= int(min(findInt, key=findInt.get))
            return ar

        #decreasing difference and mid increment hE:F < vE:H
        if self.hABBC < self.vADDG and \
        self.ABDistance <= self.BCDistance and self.DEdist <= self.EFdist and self.hDEEF < self.hABBC \
        and self.EFdist < self.EHdist:
            horizontalDiff=abs(self.hDEEF - self.hABBC)
            predictI=abs(horizontalDiff-self.hDEEF)
            findInt={}
            for key, im in self.setSelections.items():
                findInt[key]=abs(abs(self.GHdist-self.euclidDisttance(self.setProblem['H'], im ))-predictI)
            ar= int(min(findInt, key=findInt.get))
            return ar
        
        #incrementing difference with mid exp and h E:F > v E:H
        if self.hABBC < self.vADDG and \
        self.ABDistance <= self.BCDistance and self.DEdist <= self.EFdist and self.hDEEF > self.hABBC and self.vBEEH > self.vADDG \
        and self.hDEEF > self.minSimThreshold and self.EFdist > self.EHdist and self.GHdist < self.EFdist and self.GHdist < self.CFdist \
        and self.AGdist < self.ACDistance and self.AGdist < self.simThreshold:
            verticalDiff=abs(self.vBEEH-self.vADDG)
            verticalSum=self.AGdist+self.BHdist
            predictI=abs(verticalSum/2)+self.vADDG
            findInt={}
            for key, im in self.setSelections.items():
                findInt[key]=abs(self.euclidDisttance(self.setProblem['C'], im )-predictI)
            ar= int(min(findInt, key=findInt.get))
            return ar
            
        #incrementing difference with mid exp and h E:F > v E:H
        if self.hABBC < self.vADDG and \
        self.ABDistance <= self.BCDistance and self.DEdist <= self.EFdist and self.hDEEF > self.hABBC and self.vBEEH > self.vADDG \
        and self.hDEEF > self.minSimThreshold and self.EFdist > self.EHdist and self.GHdist < self.EFdist:
            verticalDiff=abs(self.vBEEH - self.vADDG) 
            predictI=abs((verticalDiff+self.vBEEH)/6)
            findInt={}
            for key, im in self.setSelections.items():
                findInt[key]=abs(abs(self.CFdist-self.euclidDisttance(self.setProblem['F'], im ))-predictI)
            ar= int(min(findInt, key=findInt.get))
            return ar
        
        #incrementing difference with h E:F < v E:H
        if self.hABBC < self.vADDG and \
        self.ABDistance <= self.BCDistance and self.DEdist <= self.EFdist and self.hDEEF > self.hABBC and self.vBEEH > self.vADDG \
        and self.EFdist < self.EHdist:
            horizontalDiff=abs(self.hDEEF - self.hABBC)
            predictI=abs(horizontalDiff+self.hDEEF)
            findInt={}
            for key, im in self.setSelections.items():
                findInt[key]=abs(abs(self.GHdist-self.euclidDisttance(self.setProblem['H'], im ))-predictI)
            ar= int(min(findInt, key=findInt.get))
            return ar
        
        
        #collapse and expand
        if self.hABBC < self.vADDG and \
        self.ABDistance >= self.BCDistance and self.DEdist >= self.EFdist and self.hDEEF < self.hABBC \
        and self.ABDistance > self.DEdist and self.GHdist > self.DEdist and self.GHdist > self.ABDistance:
            horizontalDiff=abs(self.hDEEF - self.hABBC)
            predictI=abs(horizontalDiff+(self.hABBC*2))
            findInt={}
            for key, im in self.setSelections.items():
                findInt[key]=abs(abs(self.GHdist-self.euclidDisttance(self.setProblem['H'], im ))-predictI)
            ar= int(min(findInt, key=findInt.get))
            return ar
        
        
        if self.hABBC == self.vADDG and \
        self.ABDistance <= self.BCDistance and self.DEdist >= self.EFdist and self.hDEEF > self.hABBC:
            horizontalDiff=abs(self.hDEEF - self.hABBC)
            predictI=abs(horizontalDiff-self.GHdist)
            findInt={}
            for key, im in self.setSelections.items():
                findInt[key]=abs(self.euclidDisttance(self.setProblem['H'], im )-predictI)
            ar= int(min(findInt, key=findInt.get))
            return ar
        
        #incrementing vertically column of arrays by column of 
        #decreasing difference
        if self.hABBC > self.vADDG and \
        self.ADdist <= self.DGdist and self.BEdist <= self.EHdist and self.vBEEH < self.vADDG and self.EFdist < self.EHdist \
        and self.sAGBH < self.nDiff:
            verticalDiff=self.sAGBH
            predictI=verticalDiff*6
            findInt={}
            for key, im in self.setSelections.items():
                findInt[key]=abs(abs(self.AGdist-self.euclidDisttance(self.setProblem['C'], im ))-predictI)
            ar= int(min(findInt, key=findInt.get))
            return ar
        
        #decreasing difference and h E:F < v E:H
        if self.hABBC > self.vADDG and \
        self.ADdist <= self.DGdist and self.BEdist <= self.EHdist and self.vBEEH < self.vADDG and self.EFdist < self.EHdist \
        and self.sAGBH > self.nDiff:
            verticalDiff=abs(self.vBEEH - self.vADDG)
            predictI=abs((verticalDiff-self.vBEEH)*6)
            findInt={}
            for key, im in self.setSelections.items():
                findInt[key]=abs(abs(self.CFdist-self.euclidDisttance(self.setProblem['F'], im ))-predictI)
            ar= int(min(findInt, key=findInt.get))
            return ar
        
        #**incrementing difference over difference threshold with hE:F > vE:H,ver flip
        fudD=numpy.flipud(self.setProblem['D'])
        fudE=numpy.flipud(self.setProblem['E'])
        fudF=numpy.flipud(self.setProblem['F'])
        fudAD=self.euclidDisttance(fudD,self.setProblem['A'])
        fudDG=self.euclidDisttance(fudD,self.setProblem['G'])
        fudBE=self.euclidDisttance(fudE,self.setProblem['B'])
        fudEH=self.euclidDisttance(fudE,self.setProblem['H'])
        fudCF=self.euclidDisttance(fudF,self.setProblem['C'])
        fudADDG=abs(fudAD-fudDG)
        fudBEEH=abs(fudBE-fudEH)
        #print("fudH3",self.euclidDisttance(numpy.flipud(fudF),self.setSelect['3']))
        if self.hABBC > self.vADDG and \
        self.ADdist <= self.DGdist and self.BEdist <= self.EHdist and self.vBEEH > self.vADDG \
        and self.sBCGH > self.minDiffThreshold and self.dAECE > self.minDiffThreshold and self.dCEEG < self.nDiff \
        and self.CFdist > self.BEdist > self.ADdist and self.EFdist > self.EHdist and self.vBEEH > self.minDiffThreshold  \
        and self.FHdist > self.BFdist and self.BDdist < self.CEdist and fudAD < fudDG and fudBE < fudEH and fudCF > fudBE > fudAD:
            verticalFlDiff=abs((fudADDG - fudBEEH))
            predictI=fudCF+verticalFlDiff
            findInt={}
            for key, im in self.setSelections.items():
                findInt[key]=abs(abs(fudCF-self.euclidDisttance(fudF, im ))-predictI)
            ar= int(min(findInt, key=findInt.get))
            return ar
            
        #incrementing difference over difference threshold with hE:F > vE:H
        if self.hABBC > self.vADDG \
        and self.ADdist <= self.DGdist and self.BEdist <= self.EHdist and self.vBEEH > self.vADDG \
        and self.CFdist > self.BEdist > self.ADdist and self.EFdist > self.EHdist and self.vBEEH > self.minDiffThreshold \
        and self.FHdist > self.BFdist and self.BDdist < self.CEdist and self.sBCGH > self.minDiffThreshold and self.dAECE < self.minDiffThreshold:
            diagonalDiff=self.dBDCE
            predictI=diagonalDiff+self.DHdist
            findInt={}
            for key, im in self.setSelections.items():
                findInt[key]=abs(self.euclidDisttance(self.setProblem['E'], im )-predictI)
            ar= int(min(findInt, key=findInt.get))
            return ar
            
        #incrementing difference over difference threshold with hE:F > vE:H
        if self.hABBC > self.vADDG \
        and self.ADdist <= self.DGdist and self.BEdist <= self.EHdist and self.vBEEH > self.vADDG \
        and self.CFdist > self.BEdist > self.ADdist and self.EFdist > self.EHdist and self.vBEEH > self.minDiffThreshold \
        and self.FHdist > self.BFdist and self.BDdist < self.CEdist and self.sBCGH < self.minDiffThreshold:
            diagonalDiff=self.dBDCE
            predictI=diagonalDiff+self.DHdist
            findInt={}
            for key, im in self.setSelections.items():
                findInt[key]=abs(self.euclidDisttance(self.setProblem['E'], im )-predictI)
            ar= int(min(findInt, key=findInt.get))
            return ar
            
        #incrementing difference over difference threshold with hE:F > vE:H and close BEEH
        if self.hABBC > self.vADDG and \
        self.ADdist <= self.DGdist and self.BEdist <= self.EHdist and self.vBEEH > self.vADDG \
        and self.CFdist > self.BEdist > self.ADdist and self.EFdist > self.EHdist and self.vBEEH < self.minDiffThreshold \
        and self.FHdist < self.BFdist and self.BDdist < self.CEdist:
            verticalDiff=abs(self.vBEEH - self.vADDG)
            predictI=abs((verticalDiff+self.vBEEH)/6)
            findInt={}
            for key, im in self.setSelections.items():
                findInt[key]=abs(abs(self.CFdist-self.euclidDisttance(self.setProblem['F'], im ))-predictI)
            ar= int(min(findInt, key=findInt.get))
            return ar
            
        #incrementing difference over difference threshold with hE:F > vE:H
        if self.hABBC > self.vADDG and \
        self.ADdist <= self.DGdist and self.BEdist <= self.EHdist and self.vBEEH > self.vADDG \
        and self.CFdist > self.BEdist > self.ADdist and self.EFdist < self.EHdist and self.vBEEH > self.minDiffThreshold:
            verticalDiff=abs(self.vBEEH - self.vADDG)
            predictI=abs((verticalDiff+self.vBEEH))
            findInt={}
            for key, im in self.setSelections.items():
                if self.euclidDisttance(self.setProblem['F'], im) > self.CFdist:
                    findInt[key]=abs(abs(self.CFdist-self.euclidDisttance(self.setProblem['F'], im ))-predictI)
            if findInt:
                ar= int(min(findInt, key=findInt.get))
                return ar
            else:
                return -1

        
        #incrementing difference under difference threshold
        if self.hABBC > self.vADDG and \
        self.ADdist <= self.DGdist and self.BEdist <= self.EHdist and self.vBEEH > self.vADDG \
        and self.CFdist > self.BEdist > self.ADdist and self.EFdist < self.EHdist and self.vBEEH < self.nDiff:
            verticalDiff=abs(self.vBEEH - self.vADDG)
            predictI=abs((verticalDiff+self.vBEEH)/6)
            findInt={}
            for key, im in self.setSelections.items():
                findInt[key]=abs(abs(self.CFdist-self.euclidDisttance(self.setProblem['F'], im ))-predictI)
            ar= int(min(findInt, key=findInt.get))
            return ar

            
        if self.hABBC > self.vADDG and \
        self.ADdist <= self.DGdist and self.BEdist <= self.EHdist and self.vBEEH > self.vADDG \
        and self.CFdist > self.BEdist > self.ADdist and self.vBEEH > self.nDiff and self.vBEEH < self.minDiffThreshold:
            verticalDiff=abs(self.vBEEH - self.vADDG)
            predictI=abs((verticalDiff+self.vBEEH)/6)
            findInt={}
            for key, im in self.setSelections.items():
                if self.euclidDisttance(self.setProblem['F'], im) > self.CFdist:
                    findInt[key]=abs(abs(self.CFdist-self.euclidDisttance(self.setProblem['F'], im ))-predictI)
            if findInt:
                ar= int(min(findInt, key=findInt.get))
                return ar
            else:
                return -1

        else:
            return -1

    # The primary method for solving incoming Raven's Progressive Matrices.
    # For each problem, your Agent's Solve() method will be called. At the
    # conclusion of Solve(), your Agent should return an int representing its
    # answer to the question: 1, 2, 3, 4, 5, or 6. Strings of these ints 
    # are also the Names of the individual RavensFigures, obtained through
    # RavensFigure.getName(). Return a negative number to skip a problem.
    #
    # Make sure to return your answer *as an integer* at the end of Solve().
    # Returning your answer as a string may cause your program to crash.
    def Solve(self,problem):
        self.setupProblem(problem)
        if problem.problemType == '2x2':
            answer = self.solveHelper()
        #print(problem.name,answer)
        return answer