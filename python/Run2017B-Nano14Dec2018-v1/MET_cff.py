import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/data/Run2017B/MET/NANOAOD/Nano14Dec2018-v1/90000/06753AFF-1336-9248-B567-357F268E8AB8.root',
       '/store/data/Run2017B/MET/NANOAOD/Nano14Dec2018-v1/90000/0792192D-662C-524A-8F7B-2E787E753069.root',
       '/store/data/Run2017B/MET/NANOAOD/Nano14Dec2018-v1/90000/1522BF24-9907-424C-9042-2A6D6864E1B4.root',
       '/store/data/Run2017B/MET/NANOAOD/Nano14Dec2018-v1/90000/1A05BB8C-0A94-524A-8BF4-A69734DF7F90.root',
       '/store/data/Run2017B/MET/NANOAOD/Nano14Dec2018-v1/90000/36343375-6BED-E54C-8ED7-F6AD09986066.root',
       '/store/data/Run2017B/MET/NANOAOD/Nano14Dec2018-v1/90000/36E7F4C3-BDC6-574D-80ED-E81E1F21C1C9.root',
       '/store/data/Run2017B/MET/NANOAOD/Nano14Dec2018-v1/90000/3DA2FCD2-B46B-B54D-AC85-E257BD7005C8.root',
       '/store/data/Run2017B/MET/NANOAOD/Nano14Dec2018-v1/90000/40AEFADD-7A6E-5548-992A-624A9768D860.root',
       '/store/data/Run2017B/MET/NANOAOD/Nano14Dec2018-v1/90000/460535C9-9735-6443-89B6-A5A995C29BAF.root',
       '/store/data/Run2017B/MET/NANOAOD/Nano14Dec2018-v1/90000/5AB85368-24D3-9540-951B-FA8E706B0A71.root',
       '/store/data/Run2017B/MET/NANOAOD/Nano14Dec2018-v1/90000/5B92F9A6-D9AC-7A4F-972A-0DED3B454BEA.root',
       '/store/data/Run2017B/MET/NANOAOD/Nano14Dec2018-v1/90000/5C78F286-6D9F-7543-83B3-6D9E51CF1FC9.root',
       '/store/data/Run2017B/MET/NANOAOD/Nano14Dec2018-v1/90000/5D269098-018A-D34C-8EDD-17DEC35017D1.root',
       '/store/data/Run2017B/MET/NANOAOD/Nano14Dec2018-v1/90000/6089CC5C-13C5-E44A-9780-A64655A31EE9.root',
       '/store/data/Run2017B/MET/NANOAOD/Nano14Dec2018-v1/90000/60B576ED-8CCB-F942-BBBF-2EDCE927C5FA.root',
       '/store/data/Run2017B/MET/NANOAOD/Nano14Dec2018-v1/90000/627AFD38-8F70-1641-95D7-4B060505BC97.root',
       '/store/data/Run2017B/MET/NANOAOD/Nano14Dec2018-v1/90000/796BB8EF-03A8-7E4B-83DA-3EDD4CEFFF6B.root',
       '/store/data/Run2017B/MET/NANOAOD/Nano14Dec2018-v1/90000/85854D30-9061-7246-9D2F-84C7154ABB6C.root',
       '/store/data/Run2017B/MET/NANOAOD/Nano14Dec2018-v1/90000/92B54FA6-1CD3-3142-87A6-89F2C4200E03.root',
       '/store/data/Run2017B/MET/NANOAOD/Nano14Dec2018-v1/90000/9990A9C6-15E4-3949-8196-0532333DB416.root',
       '/store/data/Run2017B/MET/NANOAOD/Nano14Dec2018-v1/90000/9BDE8F07-9CE1-F048-B29A-7335C03075B4.root',
       '/store/data/Run2017B/MET/NANOAOD/Nano14Dec2018-v1/90000/B71C6CE3-3F92-524B-A3FA-1F0A521CABA8.root',
       '/store/data/Run2017B/MET/NANOAOD/Nano14Dec2018-v1/90000/BE05DF48-6480-4643-8F04-3833998A843B.root',
       '/store/data/Run2017B/MET/NANOAOD/Nano14Dec2018-v1/90000/CE5B3E71-AE12-6D47-B408-EE0EF9E37627.root',
       '/store/data/Run2017B/MET/NANOAOD/Nano14Dec2018-v1/90000/F241B51F-2BDF-4746-8F1C-39926B62C475.root',
       '/store/data/Run2017B/MET/NANOAOD/Nano14Dec2018-v1/90000/F875D0F5-436D-0943-B9A2-2E7E54BAB907.root',
       '/store/data/Run2017B/MET/NANOAOD/Nano14Dec2018-v1/90000/F8D89621-0055-3040-AA0A-387519E967CB.root',
] )
