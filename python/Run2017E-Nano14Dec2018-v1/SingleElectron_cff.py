import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/data/Run2017E/SingleElectron/NANOAOD/Nano14Dec2018-v1/20000/05BF4C32-4D95-494C-8B77-DC047D35A5BF.root',
       '/store/data/Run2017E/SingleElectron/NANOAOD/Nano14Dec2018-v1/20000/2C0A0F4E-4254-0744-8DAE-0ACD21CBCBAB.root',
       '/store/data/Run2017E/SingleElectron/NANOAOD/Nano14Dec2018-v1/20000/334FE3D9-833C-4B4A-A57E-AF72A03E1898.root',
       '/store/data/Run2017E/SingleElectron/NANOAOD/Nano14Dec2018-v1/20000/3F7AE600-8A75-F047-ABE6-5A4950B90EAA.root',
       '/store/data/Run2017E/SingleElectron/NANOAOD/Nano14Dec2018-v1/20000/3FDA1FCD-4362-6D40-8C82-13C8E0769587.root',
       '/store/data/Run2017E/SingleElectron/NANOAOD/Nano14Dec2018-v1/20000/43D7415B-7F6C-5D4E-B72E-9FB47EC1A611.root',
       '/store/data/Run2017E/SingleElectron/NANOAOD/Nano14Dec2018-v1/20000/4B509257-19FC-2A4B-936D-01E4EC69388D.root',
       '/store/data/Run2017E/SingleElectron/NANOAOD/Nano14Dec2018-v1/20000/4B9CC782-1D06-0A4B-AB7A-16EC4A854D2D.root',
       '/store/data/Run2017E/SingleElectron/NANOAOD/Nano14Dec2018-v1/20000/5949A073-9172-CD49-80C6-0C10FC5D1335.root',
       '/store/data/Run2017E/SingleElectron/NANOAOD/Nano14Dec2018-v1/20000/6FB04D7B-0FE6-2B49-B269-8CF27E59AB3F.root',
       '/store/data/Run2017E/SingleElectron/NANOAOD/Nano14Dec2018-v1/20000/780AE96E-5F67-B249-AC0B-39F5EE60BAE8.root',
       '/store/data/Run2017E/SingleElectron/NANOAOD/Nano14Dec2018-v1/20000/7AACE6F7-A147-6D46-AD55-0D8256B4EF9F.root',
       '/store/data/Run2017E/SingleElectron/NANOAOD/Nano14Dec2018-v1/20000/7C4169F3-BF80-054D-AEA7-595543F0C83E.root',
       '/store/data/Run2017E/SingleElectron/NANOAOD/Nano14Dec2018-v1/20000/7D6EB32A-9212-AA43-9A2B-A78D3DBA55A8.root',
       '/store/data/Run2017E/SingleElectron/NANOAOD/Nano14Dec2018-v1/20000/82D4F30E-CC5D-FB48-87F3-F8F0007CDD61.root',
       '/store/data/Run2017E/SingleElectron/NANOAOD/Nano14Dec2018-v1/20000/920DC1AF-4708-1047-94B9-2C5E2E537811.root',
       '/store/data/Run2017E/SingleElectron/NANOAOD/Nano14Dec2018-v1/20000/A15DB8C1-8286-0144-867E-C2D873DE16AF.root',
       '/store/data/Run2017E/SingleElectron/NANOAOD/Nano14Dec2018-v1/20000/A191A2DA-1F7C-4041-A249-462530436E7A.root',
       '/store/data/Run2017E/SingleElectron/NANOAOD/Nano14Dec2018-v1/20000/A25DDEAE-C5A2-784E-B354-5C380DCCF12D.root',
       '/store/data/Run2017E/SingleElectron/NANOAOD/Nano14Dec2018-v1/20000/AE67DB7B-9AD6-EB44-A9B2-DCE0A55EFBE3.root',
       '/store/data/Run2017E/SingleElectron/NANOAOD/Nano14Dec2018-v1/20000/B3DACC69-59E6-6A44-BF19-B68D11F0ADBB.root',
       '/store/data/Run2017E/SingleElectron/NANOAOD/Nano14Dec2018-v1/20000/BD27AE40-6E4E-B94B-9778-D41CE581E9C3.root',
       '/store/data/Run2017E/SingleElectron/NANOAOD/Nano14Dec2018-v1/20000/C4DEE61B-B617-414A-97EA-05AD6C3C4F20.root',
       '/store/data/Run2017E/SingleElectron/NANOAOD/Nano14Dec2018-v1/20000/C70E3740-2F53-884A-B0FD-FD4F03DE9534.root',
       '/store/data/Run2017E/SingleElectron/NANOAOD/Nano14Dec2018-v1/20000/C7486D9A-C05A-9F40-A21D-D2C97350E3E9.root',
       '/store/data/Run2017E/SingleElectron/NANOAOD/Nano14Dec2018-v1/20000/D3CD97FE-398D-0848-9CEB-CF65F7A4427F.root',
       '/store/data/Run2017E/SingleElectron/NANOAOD/Nano14Dec2018-v1/20000/D56B5BE2-945A-F04D-9374-A32FA35B7245.root',
       '/store/data/Run2017E/SingleElectron/NANOAOD/Nano14Dec2018-v1/20000/D5CE9CFC-44CE-E84A-BCD0-7B6B8FCDCFF0.root',
       '/store/data/Run2017E/SingleElectron/NANOAOD/Nano14Dec2018-v1/20000/DFC04C0E-464C-864D-B2CB-6E4ED932914B.root',
       '/store/data/Run2017E/SingleElectron/NANOAOD/Nano14Dec2018-v1/20000/E91C4FDA-DFA3-0C41-81D7-C847427666C0.root',
       '/store/data/Run2017E/SingleElectron/NANOAOD/Nano14Dec2018-v1/20000/EC9A71F9-4BBB-DD47-80B4-8D0F5CA40E02.root',
       '/store/data/Run2017E/SingleElectron/NANOAOD/Nano14Dec2018-v1/20000/F2C2321F-4F46-304F-9EC7-0E0EAE793FE3.root',
       '/store/data/Run2017E/SingleElectron/NANOAOD/Nano14Dec2018-v1/280000/0369D0C7-F0B7-954D-BA6F-D95B58538A0F.root',
       '/store/data/Run2017E/SingleElectron/NANOAOD/Nano14Dec2018-v1/280000/05EA2995-7CA4-9A4A-B8BC-8BEC3E746CD5.root',
       '/store/data/Run2017E/SingleElectron/NANOAOD/Nano14Dec2018-v1/280000/0C77982F-10F7-9A4F-BF57-249773BE537A.root',
       '/store/data/Run2017E/SingleElectron/NANOAOD/Nano14Dec2018-v1/280000/10DE72F3-BA56-7447-B426-60A367BC0AE3.root',
       '/store/data/Run2017E/SingleElectron/NANOAOD/Nano14Dec2018-v1/280000/1398A141-B0F3-C541-9B73-BEC05F18F068.root',
       '/store/data/Run2017E/SingleElectron/NANOAOD/Nano14Dec2018-v1/280000/25ACFE20-46D4-0E40-AE38-FB5B12E56378.root',
       '/store/data/Run2017E/SingleElectron/NANOAOD/Nano14Dec2018-v1/280000/31703DD6-7A9E-B345-9B99-D0F15D47BBED.root',
       '/store/data/Run2017E/SingleElectron/NANOAOD/Nano14Dec2018-v1/280000/3561AB6B-BEC2-FF46-85E1-4733623BD59D.root',
       '/store/data/Run2017E/SingleElectron/NANOAOD/Nano14Dec2018-v1/280000/41B1941C-BA2B-5144-A395-383974193034.root',
       '/store/data/Run2017E/SingleElectron/NANOAOD/Nano14Dec2018-v1/280000/53AA1C35-651D-5B43-9580-0E50A7AF1F60.root',
       '/store/data/Run2017E/SingleElectron/NANOAOD/Nano14Dec2018-v1/280000/61A994DD-C9A3-2E4C-8F5C-FE65C3416985.root',
       '/store/data/Run2017E/SingleElectron/NANOAOD/Nano14Dec2018-v1/280000/6BF57BA0-662D-F84A-BB8D-8F575F3AB5C8.root',
       '/store/data/Run2017E/SingleElectron/NANOAOD/Nano14Dec2018-v1/280000/6C33453C-2017-DE41-907C-BF4535928203.root',
       '/store/data/Run2017E/SingleElectron/NANOAOD/Nano14Dec2018-v1/280000/6EC816A0-97F2-B742-A9FE-5A7B0ED4C818.root',
       '/store/data/Run2017E/SingleElectron/NANOAOD/Nano14Dec2018-v1/280000/99D23F5E-A3CD-1445-9EB9-EB098F49D696.root',
       '/store/data/Run2017E/SingleElectron/NANOAOD/Nano14Dec2018-v1/280000/9BDD2413-36AA-684A-8247-1C0BCF1AD879.root',
       '/store/data/Run2017E/SingleElectron/NANOAOD/Nano14Dec2018-v1/280000/B2361685-1EFD-1048-84B4-20B397D29873.root',
       '/store/data/Run2017E/SingleElectron/NANOAOD/Nano14Dec2018-v1/280000/CC645196-2E41-9D49-9C30-CE393BC00B47.root',
       '/store/data/Run2017E/SingleElectron/NANOAOD/Nano14Dec2018-v1/280000/D0D5D404-0178-AD4F-821A-03F98D55FDD8.root',
       '/store/data/Run2017E/SingleElectron/NANOAOD/Nano14Dec2018-v1/280000/D1567B9E-FE24-1640-98CE-8F107A2C9E55.root',
       '/store/data/Run2017E/SingleElectron/NANOAOD/Nano14Dec2018-v1/280000/E3BC33EA-36BD-9740-B176-A2E9B6C069B4.root',
       '/store/data/Run2017E/SingleElectron/NANOAOD/Nano14Dec2018-v1/280000/E3CFAA71-CF08-0641-A236-206DD17B6684.root',
] )