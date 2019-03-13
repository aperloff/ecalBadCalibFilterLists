import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/data/Run2017E/MET/NANOAOD/Nano14Dec2018-v1/20000/0D14D4B3-E49F-2B49-8962-049453F38062.root',
       '/store/data/Run2017E/MET/NANOAOD/Nano14Dec2018-v1/20000/0E62B8E4-C63D-1945-A044-9EE1DA516276.root',
       '/store/data/Run2017E/MET/NANOAOD/Nano14Dec2018-v1/20000/10A5C953-DC6D-AD4F-9B5C-1E930FED5546.root',
       '/store/data/Run2017E/MET/NANOAOD/Nano14Dec2018-v1/20000/173E7C9C-AF87-794C-9C32-A0E811FB90A7.root',
       '/store/data/Run2017E/MET/NANOAOD/Nano14Dec2018-v1/20000/22D0413F-0554-0249-8F49-D120D51BD095.root',
       '/store/data/Run2017E/MET/NANOAOD/Nano14Dec2018-v1/20000/297A431C-0EEA-F44C-A631-412DEB3EEBBB.root',
       '/store/data/Run2017E/MET/NANOAOD/Nano14Dec2018-v1/20000/37F0E5FB-5F27-FC4F-BBAA-9FC27E185820.root',
       '/store/data/Run2017E/MET/NANOAOD/Nano14Dec2018-v1/20000/3A498619-C53F-C946-BE52-492D145BB836.root',
       '/store/data/Run2017E/MET/NANOAOD/Nano14Dec2018-v1/20000/3AEE3782-E4EA-7546-B51C-5FE7C24DA95B.root',
       '/store/data/Run2017E/MET/NANOAOD/Nano14Dec2018-v1/20000/3C13EF41-894B-F240-A9A6-EA1C91E4DF19.root',
       '/store/data/Run2017E/MET/NANOAOD/Nano14Dec2018-v1/20000/3DBF1073-BCA5-D64D-9A9D-0B0B43B653F9.root',
       '/store/data/Run2017E/MET/NANOAOD/Nano14Dec2018-v1/20000/41009692-4F4E-9543-9587-9913AE09E31E.root',
       '/store/data/Run2017E/MET/NANOAOD/Nano14Dec2018-v1/20000/4795B345-677C-2A44-AB85-A06E79FEFA16.root',
       '/store/data/Run2017E/MET/NANOAOD/Nano14Dec2018-v1/20000/52A843EE-C7FA-954A-8877-60581E1059A3.root',
       '/store/data/Run2017E/MET/NANOAOD/Nano14Dec2018-v1/20000/565F37C3-4241-5941-BE0F-5C25A69EEAEB.root',
       '/store/data/Run2017E/MET/NANOAOD/Nano14Dec2018-v1/20000/5D442703-073B-1A4E-B1A9-1397381A8607.root',
       '/store/data/Run2017E/MET/NANOAOD/Nano14Dec2018-v1/20000/6274E6E4-834C-A64A-9A30-3431DDCD4D8F.root',
       '/store/data/Run2017E/MET/NANOAOD/Nano14Dec2018-v1/20000/664F2056-CA40-F549-AC89-2EF75646AD87.root',
       '/store/data/Run2017E/MET/NANOAOD/Nano14Dec2018-v1/20000/71F89E79-00DA-D945-AB85-8B0A230DED17.root',
       '/store/data/Run2017E/MET/NANOAOD/Nano14Dec2018-v1/20000/72308915-99F6-524B-823E-6017975103C9.root',
       '/store/data/Run2017E/MET/NANOAOD/Nano14Dec2018-v1/20000/789047A4-EB38-8D4B-9E69-8E8301AFFAC6.root',
       '/store/data/Run2017E/MET/NANOAOD/Nano14Dec2018-v1/20000/80EDB21A-6604-C545-82FB-16E10615C561.root',
       '/store/data/Run2017E/MET/NANOAOD/Nano14Dec2018-v1/20000/80F32D53-E249-0B41-BF2E-2814D765C972.root',
       '/store/data/Run2017E/MET/NANOAOD/Nano14Dec2018-v1/20000/89BA793C-E7BC-3C4A-8395-0768F0A7B645.root',
       '/store/data/Run2017E/MET/NANOAOD/Nano14Dec2018-v1/20000/96AC0AFD-4A37-8444-AC24-A81BC218C35D.root',
       '/store/data/Run2017E/MET/NANOAOD/Nano14Dec2018-v1/20000/990065D2-669D-4C4A-AF0F-F88B1A932A5B.root',
       '/store/data/Run2017E/MET/NANOAOD/Nano14Dec2018-v1/20000/9DAAE6D1-03C3-0247-AECA-0DB16EAE1AF3.root',
       '/store/data/Run2017E/MET/NANOAOD/Nano14Dec2018-v1/20000/B5E406F8-7E04-C44F-BE9B-65EF7D2D1881.root',
       '/store/data/Run2017E/MET/NANOAOD/Nano14Dec2018-v1/20000/B623BED0-FBB3-0E4A-A296-FF125F923E1B.root',
       '/store/data/Run2017E/MET/NANOAOD/Nano14Dec2018-v1/20000/BA22380E-4409-684A-9D6B-95703CA6570C.root',
       '/store/data/Run2017E/MET/NANOAOD/Nano14Dec2018-v1/20000/BE7BBD91-488F-8248-A4E0-A7824BED0387.root',
       '/store/data/Run2017E/MET/NANOAOD/Nano14Dec2018-v1/20000/BF62D695-D8F0-DD4A-88ED-E9C5C9897EBD.root',
       '/store/data/Run2017E/MET/NANOAOD/Nano14Dec2018-v1/20000/CAB32CF0-E1F6-BC4D-AF4C-3664C2E4CD20.root',
       '/store/data/Run2017E/MET/NANOAOD/Nano14Dec2018-v1/20000/CF9F9148-2C5D-2849-9930-04A78771D672.root',
       '/store/data/Run2017E/MET/NANOAOD/Nano14Dec2018-v1/20000/DF598974-6E29-8340-8FB4-A88BCD81DCB9.root',
       '/store/data/Run2017E/MET/NANOAOD/Nano14Dec2018-v1/20000/E055F936-9FBC-1C4C-BAC1-75FA7BB060D4.root',
       '/store/data/Run2017E/MET/NANOAOD/Nano14Dec2018-v1/20000/F1927120-FDD4-AE4F-9931-AD470FE77B03.root',
       '/store/data/Run2017E/MET/NANOAOD/Nano14Dec2018-v1/20000/F347742C-8C29-6A43-BE52-2EDFE6451520.root',
       '/store/data/Run2017E/MET/NANOAOD/Nano14Dec2018-v1/20000/FAA14E70-AEFE-E84D-9452-DDCEF132BD41.root',
       '/store/data/Run2017E/MET/NANOAOD/Nano14Dec2018-v1/20000/FAA6B98F-B4B4-FD48-A07B-E09416538C88.root',
] )