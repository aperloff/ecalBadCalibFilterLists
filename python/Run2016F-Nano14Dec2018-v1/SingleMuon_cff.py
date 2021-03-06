import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/data/Run2016F/SingleMuon/NANOAOD/Nano14Dec2018-v1/280000/03277703-8136-AC4A-A43E-5A7B3BEF06B5.root',
       '/store/data/Run2016F/SingleMuon/NANOAOD/Nano14Dec2018-v1/280000/13AAF6D1-0330-8744-8F56-A3E5995D1104.root',
       '/store/data/Run2016F/SingleMuon/NANOAOD/Nano14Dec2018-v1/280000/1C86AFE5-DC49-6648-B70C-E2BB7230D541.root',
       '/store/data/Run2016F/SingleMuon/NANOAOD/Nano14Dec2018-v1/280000/282093CF-7859-194E-8779-9F9DBA630612.root',
       '/store/data/Run2016F/SingleMuon/NANOAOD/Nano14Dec2018-v1/280000/3924836C-D5DD-4A40-B2AD-AA52B3BDD1CA.root',
       '/store/data/Run2016F/SingleMuon/NANOAOD/Nano14Dec2018-v1/280000/406B1AC9-5BE9-E54C-8034-2B09BEB48C91.root',
       '/store/data/Run2016F/SingleMuon/NANOAOD/Nano14Dec2018-v1/280000/4A37C3A5-6922-8742-8622-BA55B1B821C5.root',
       '/store/data/Run2016F/SingleMuon/NANOAOD/Nano14Dec2018-v1/280000/4D4D54C5-DB46-CE4B-B703-B5DA776B6D0F.root',
       '/store/data/Run2016F/SingleMuon/NANOAOD/Nano14Dec2018-v1/280000/51FD4C9D-439D-4640-ABDB-4B114D4CD609.root',
       '/store/data/Run2016F/SingleMuon/NANOAOD/Nano14Dec2018-v1/280000/705EBC01-6F4A-F943-9834-64387A0D5480.root',
       '/store/data/Run2016F/SingleMuon/NANOAOD/Nano14Dec2018-v1/280000/7631FF58-995C-FE4F-B404-110A8CA18B41.root',
       '/store/data/Run2016F/SingleMuon/NANOAOD/Nano14Dec2018-v1/280000/82657DBD-B544-DE47-BCF6-535DCDA60215.root',
       '/store/data/Run2016F/SingleMuon/NANOAOD/Nano14Dec2018-v1/280000/9ACDE8ED-4F9D-B34F-9983-0C25AAD4B211.root',
       '/store/data/Run2016F/SingleMuon/NANOAOD/Nano14Dec2018-v1/280000/B48CDAC8-0DDD-E044-9A44-3AAA7C3F4EAD.root',
       '/store/data/Run2016F/SingleMuon/NANOAOD/Nano14Dec2018-v1/280000/BCACB00D-CE62-9448-87E0-AD1C37DD9A43.root',
       '/store/data/Run2016F/SingleMuon/NANOAOD/Nano14Dec2018-v1/280000/BD2268C8-F57A-2C48-B443-AD3DC69A10CF.root',
       '/store/data/Run2016F/SingleMuon/NANOAOD/Nano14Dec2018-v1/280000/BEA94406-3B54-0347-800F-FE8982517B39.root',
       '/store/data/Run2016F/SingleMuon/NANOAOD/Nano14Dec2018-v1/280000/C479CC7A-1EE8-F248-9F59-405463FDDFD2.root',
       '/store/data/Run2016F/SingleMuon/NANOAOD/Nano14Dec2018-v1/280000/CBBCD90E-BC2D-C84C-9E8E-E2F8537B83BA.root',
       '/store/data/Run2016F/SingleMuon/NANOAOD/Nano14Dec2018-v1/280000/D1EAF99F-029E-AA49-9164-7AF5C1C9D012.root',
       '/store/data/Run2016F/SingleMuon/NANOAOD/Nano14Dec2018-v1/280000/ED1A456A-0539-F248-A0D3-FA33BED6BE44.root',
       '/store/data/Run2016F/SingleMuon/NANOAOD/Nano14Dec2018-v1/280000/EFF7900D-2B96-BB42-AF70-0487238A3BCC.root',
       '/store/data/Run2016F/SingleMuon/NANOAOD/Nano14Dec2018-v1/280000/F05D9E15-9133-9146-8FDC-A8BA3AD71EAD.root',
       '/store/data/Run2016F/SingleMuon/NANOAOD/Nano14Dec2018-v1/280000/F2C1AF5E-380D-5349-BA13-878653A29B1E.root',
       '/store/data/Run2016F/SingleMuon/NANOAOD/Nano14Dec2018-v1/280000/F31381BA-9AEC-8246-AA12-72296D5D31A8.root',
       '/store/data/Run2016F/SingleMuon/NANOAOD/Nano14Dec2018-v1/280000/F972BC9B-9921-144F-8F98-595D13C6704F.root',
       '/store/data/Run2016F/SingleMuon/NANOAOD/Nano14Dec2018-v1/280000/FA5049DB-F167-D343-9224-AD903550138E.root',
       '/store/data/Run2016F/SingleMuon/NANOAOD/Nano14Dec2018-v1/280000/FA64E1DD-B5E5-4E4A-8BC4-84AF97278748.root',
] )
