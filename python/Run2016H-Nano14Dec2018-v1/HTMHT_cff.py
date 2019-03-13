import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/data/Run2016H/HTMHT/NANOAOD/Nano14Dec2018-v1/90000/0227A111-074D-054D-8174-554CAAA2EB12.root',
       '/store/data/Run2016H/HTMHT/NANOAOD/Nano14Dec2018-v1/90000/0753AB4E-6E23-C643-8EBC-DDDB357050D4.root',
       '/store/data/Run2016H/HTMHT/NANOAOD/Nano14Dec2018-v1/90000/0A8B00DB-30ED-274B-A3DF-FFB85AAD7559.root',
       '/store/data/Run2016H/HTMHT/NANOAOD/Nano14Dec2018-v1/90000/146CC765-C65C-D54C-932E-4B1252C03DA8.root',
       '/store/data/Run2016H/HTMHT/NANOAOD/Nano14Dec2018-v1/90000/1C3270A8-E1A1-0645-8E97-69C39503245F.root',
       '/store/data/Run2016H/HTMHT/NANOAOD/Nano14Dec2018-v1/90000/285CD828-FC3C-714C-985A-C1BFB174EC51.root',
       '/store/data/Run2016H/HTMHT/NANOAOD/Nano14Dec2018-v1/90000/2EC07AD4-66B2-0747-AB73-A6EEA91AC5E9.root',
       '/store/data/Run2016H/HTMHT/NANOAOD/Nano14Dec2018-v1/90000/34743309-2732-C54A-BE09-789E01B30065.root',
       '/store/data/Run2016H/HTMHT/NANOAOD/Nano14Dec2018-v1/90000/43472DAB-DFC1-EE46-9B53-0A514434C8D6.root',
       '/store/data/Run2016H/HTMHT/NANOAOD/Nano14Dec2018-v1/90000/46A2B3AE-821D-0042-96DB-19099CD22985.root',
       '/store/data/Run2016H/HTMHT/NANOAOD/Nano14Dec2018-v1/90000/503B9141-D0D8-9945-BB92-AD293842E102.root',
       '/store/data/Run2016H/HTMHT/NANOAOD/Nano14Dec2018-v1/90000/51406055-C83A-624C-BE32-4C70AAED404E.root',
       '/store/data/Run2016H/HTMHT/NANOAOD/Nano14Dec2018-v1/90000/575D59A8-F01E-C448-98A3-F3C00A421A0D.root',
       '/store/data/Run2016H/HTMHT/NANOAOD/Nano14Dec2018-v1/90000/5B44BC10-6147-1843-8B34-909C53F4D452.root',
       '/store/data/Run2016H/HTMHT/NANOAOD/Nano14Dec2018-v1/90000/6451FDCF-5DAA-4145-BE82-B01791AD9519.root',
       '/store/data/Run2016H/HTMHT/NANOAOD/Nano14Dec2018-v1/90000/662FD0BD-24E1-2143-AEC9-6CC4CCED1302.root',
       '/store/data/Run2016H/HTMHT/NANOAOD/Nano14Dec2018-v1/90000/89BCF4A3-7806-FF46-AAB1-E831B246B37D.root',
       '/store/data/Run2016H/HTMHT/NANOAOD/Nano14Dec2018-v1/90000/A4407162-9ABD-BB49-BE8C-C4C363D6994D.root',
       '/store/data/Run2016H/HTMHT/NANOAOD/Nano14Dec2018-v1/90000/B0B39E64-01CE-0548-A409-B35443AAC02E.root',
       '/store/data/Run2016H/HTMHT/NANOAOD/Nano14Dec2018-v1/90000/C6C90B32-48E3-F048-B02C-AF71F0657483.root',
       '/store/data/Run2016H/HTMHT/NANOAOD/Nano14Dec2018-v1/90000/D3054E8A-CC2C-7C45-B690-FE8CD05B50C1.root',
       '/store/data/Run2016H/HTMHT/NANOAOD/Nano14Dec2018-v1/90000/DF576946-0CBF-A143-BD96-057C911E6D84.root',
       '/store/data/Run2016H/HTMHT/NANOAOD/Nano14Dec2018-v1/90000/E7F1587F-087E-4D42-8919-263C8CC594D6.root',
       '/store/data/Run2016H/HTMHT/NANOAOD/Nano14Dec2018-v1/90000/EA74EBF1-4D98-9746-B3E9-CBBEC408A7C6.root',
       '/store/data/Run2016H/HTMHT/NANOAOD/Nano14Dec2018-v1/90000/ECD6138D-46ED-FF43-8ECB-E2DFF2F14D63.root',
       '/store/data/Run2016H/HTMHT/NANOAOD/Nano14Dec2018-v1/90000/EED6C371-C10A-5145-BE27-DD1D48B65A4E.root',
] )