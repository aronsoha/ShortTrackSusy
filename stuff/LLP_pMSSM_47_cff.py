import FWCore.ParameterSet.Config as cms

from Configuration.Generator.Pythia8CommonSettings_cfi import *
from Configuration.Generator.Pythia8CUEP8M1Settings_cfi import *

generator = cms.EDFilter("Pythia8GeneratorFilter",
    pythiaPylistVerbosity = cms.untracked.int32(0),
    filterEfficiency = cms.untracked.double(1.0),
    pythiaHepMCVerbosity = cms.untracked.bool(False),
    comEnergy = cms.double(13000),
SLHAFileForPythia8  = cms.string('SigPoints/pMSSM12_MCMC1_47_667155.slha'), 
#SLHAFileForPythia8  = cms.string('SigPoints/LMG34.slha'),
#SLHAFileForPythia8 = cms.string('SLHA/pMSSM12_MCMC1_15_971629.slha'),                                                                                 
#SLHAFileForPythia8 = cms.string('SLHA/CharginoPmssm.slha'),                                                                                           
#SLHAFileForPythia8 = cms.string('SLHA/LMG34.slha'),                                                                                                   
    #SLHAFileForPythia8 = cms.string('SLHA/normal.slha'),#try a healthy pMSSM file                                                                     
    maxEventsToPrint = cms.untracked.int32(3),
    PythiaParameters = cms.PSet(
        pythia8CommonSettingsBlock,
        pythia8CUEP8M1SettingsBlock,
        processParameters = cms.vstring(
#            'IMSS(1)     = 11    ! Spectrum from external SLHA file',
#            'IMSS(21)    = 33    ! LUN number for SLHA File (must be 33) ',
#            'IMSS(22)    = 33    ! Read-in SLHA decay table ',
#            'MSEL        = 0     ! General SUSY',
#            'MSUB(226)   = 1     ! to double chargino',
#            'MSUB(229)   = 1     ! to neutralino + chargino',
#            'MDCY(312,1) = 0     ! set the chargino stable.',

'SUSY:qqbar2chi+chi- = on',
#'SUSY:all = on',
'ResonanceWidths:minThreshold = 0.0001',
'ParticleDecays:mSafety = 0.00001',
'print:quiet=false'
'SLHA:allowUserOverride = true',
#'1000024:isResonance = false',
#'-1000024:isResonance = false',
#'1000024:doExternalDecay = true',                                                                                                                     
#'-1000024:doExternalDecay = true'                                                                                                                    
#'1000024:onMode = off',
#'-1000024:onMode = off'


#'PartonLevel:ISR = off','PartonLevel:FSR = off',                                                                                                      
#'PartonLevel:MPI = off','PartonLevel:Remnants = off',                                                                                                 
#'HadronLevel:all = off',                                                                                                                              

#'SUSY:all = off',                                                                                                                                     
#'SUSY:gg2gluinogluino = on',                                                                                                                          
#'SUSY:qqbar2gluinogluino = on',                                                                                                                       
        ),
        parameterSets = cms.vstring('pythia8CommonSettings','pythia8CUEP8M1Settings','processParameters'),
#        SLHAParameters = cms.vstring('SLHAFILE = SigPoints/LMG34.slha'),
    ),
    processFile = cms.untracked.string('SimG4Core/CustomPhysics/data/RhadronProcessList.txt'),
    useregge = cms.bool(False),
    hscpFlavor = cms.untracked.string('stau'),
    massPoint = cms.untracked.int32(886),
#    particleFile = cms.untracked.string('Customise/data/geant4_pMSSM_lmg.slha')
    particleFile = cms.untracked.string('Customise/data/geant4_pMSSM_47.slha') 

)
