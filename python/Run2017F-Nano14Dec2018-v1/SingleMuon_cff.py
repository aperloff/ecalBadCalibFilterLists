import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/data/Run2017F/SingleMuon/NANOAOD/Nano14Dec2018-v1/20000/33A87A60-B79B-8B45-AA04-B85D99A8A607.root',
       '/store/data/Run2017F/SingleMuon/NANOAOD/Nano14Dec2018-v1/20000/3E1FF6B4-40AC-CE4F-80BE-486226E86ACB.root',
       '/store/data/Run2017F/SingleMuon/NANOAOD/Nano14Dec2018-v1/20000/3E6CB91B-A5D2-2041-896E-2098CF6643E8.root',
       '/store/data/Run2017F/SingleMuon/NANOAOD/Nano14Dec2018-v1/20000/42090D8D-9D80-3C42-8417-EA144FDFE785.root',
       '/store/data/Run2017F/SingleMuon/NANOAOD/Nano14Dec2018-v1/20000/7923B2D5-226F-0A4E-8309-F766F69C540F.root',
       '/store/data/Run2017F/SingleMuon/NANOAOD/Nano14Dec2018-v1/20000/7AD6B4D0-777A-3D4B-955E-ADB3F9E30427.root',
       '/store/data/Run2017F/SingleMuon/NANOAOD/Nano14Dec2018-v1/20000/7E5D8DFB-BC70-2B4B-A1DE-E5A6AE9F3EBF.root',
       '/store/data/Run2017F/SingleMuon/NANOAOD/Nano14Dec2018-v1/20000/888D5508-C245-CE45-AA0F-065A85038EFE.root',
       '/store/data/Run2017F/SingleMuon/NANOAOD/Nano14Dec2018-v1/20000/9D4EAAC0-0DA1-5243-A8D0-953187D50A3F.root',
       '/store/data/Run2017F/SingleMuon/NANOAOD/Nano14Dec2018-v1/280000/0076CC3E-B72D-4148-81A3-04292098E254.root',
       '/store/data/Run2017F/SingleMuon/NANOAOD/Nano14Dec2018-v1/280000/03724CC3-0646-C54B-8842-3EA16E173DA5.root',
       '/store/data/Run2017F/SingleMuon/NANOAOD/Nano14Dec2018-v1/280000/053FE01D-EBED-7C49-84FB-D70F9A2233A5.root',
       '/store/data/Run2017F/SingleMuon/NANOAOD/Nano14Dec2018-v1/280000/08F45190-EC65-C245-8EF9-6912DCC87FE0.root',
       '/store/data/Run2017F/SingleMuon/NANOAOD/Nano14Dec2018-v1/280000/0F2E9CD4-958E-954C-B3E9-4E8AC5F9017E.root',
       '/store/data/Run2017F/SingleMuon/NANOAOD/Nano14Dec2018-v1/280000/0F958727-CC74-A748-82E3-18B2D117AE83.root',
       '/store/data/Run2017F/SingleMuon/NANOAOD/Nano14Dec2018-v1/280000/16AE57B2-E04C-8B45-822D-B67206F4F77C.root',
       '/store/data/Run2017F/SingleMuon/NANOAOD/Nano14Dec2018-v1/280000/16EB1CD5-3BDA-A544-AB1D-AE372B207528.root',
       '/store/data/Run2017F/SingleMuon/NANOAOD/Nano14Dec2018-v1/280000/1C6E12DA-C1BB-4046-A66E-49F23C8F044C.root',
       '/store/data/Run2017F/SingleMuon/NANOAOD/Nano14Dec2018-v1/280000/1C9BAA9A-BB39-EF4C-AD08-F1FA3B16823F.root',
       '/store/data/Run2017F/SingleMuon/NANOAOD/Nano14Dec2018-v1/280000/2263DB1D-59A0-9147-9EDB-1DAFE1F12C9D.root',
       '/store/data/Run2017F/SingleMuon/NANOAOD/Nano14Dec2018-v1/280000/24B1D34D-DF6C-814F-8ECA-0D481F4D82CD.root',
       '/store/data/Run2017F/SingleMuon/NANOAOD/Nano14Dec2018-v1/280000/2914A028-08C8-4F41-B166-5C5A28BE21F1.root',
       '/store/data/Run2017F/SingleMuon/NANOAOD/Nano14Dec2018-v1/280000/29E6ABEE-3CB6-954D-91B5-CD977A162CDC.root',
       '/store/data/Run2017F/SingleMuon/NANOAOD/Nano14Dec2018-v1/280000/2D35516A-D33C-C941-9CBA-14EC46442390.root',
       '/store/data/Run2017F/SingleMuon/NANOAOD/Nano14Dec2018-v1/280000/2D916961-A6AF-714D-A030-2F7EAA858A68.root',
       '/store/data/Run2017F/SingleMuon/NANOAOD/Nano14Dec2018-v1/280000/2F3946E4-A723-654E-969B-077594E617AE.root',
       '/store/data/Run2017F/SingleMuon/NANOAOD/Nano14Dec2018-v1/280000/2FE84182-7DEC-474D-B0E2-1E0FD33F29B5.root',
       '/store/data/Run2017F/SingleMuon/NANOAOD/Nano14Dec2018-v1/280000/3103E8FB-DD0E-9345-819E-F948306AE29F.root',
       '/store/data/Run2017F/SingleMuon/NANOAOD/Nano14Dec2018-v1/280000/348CDD39-6014-E149-9A9F-5EC5F2ED2D59.root',
       '/store/data/Run2017F/SingleMuon/NANOAOD/Nano14Dec2018-v1/280000/35C2A1DE-FD8A-5747-88FF-89696F5A0DA7.root',
       '/store/data/Run2017F/SingleMuon/NANOAOD/Nano14Dec2018-v1/280000/36E50C35-46B4-6D42-B205-69C56E851301.root',
       '/store/data/Run2017F/SingleMuon/NANOAOD/Nano14Dec2018-v1/280000/38135A7E-133F-E24C-A4B7-73A4A5408406.root',
       '/store/data/Run2017F/SingleMuon/NANOAOD/Nano14Dec2018-v1/280000/4121D271-D5C1-D049-B679-FFC849729852.root',
       '/store/data/Run2017F/SingleMuon/NANOAOD/Nano14Dec2018-v1/280000/47E75AD4-072D-5648-BB0E-740F5A031A47.root',
       '/store/data/Run2017F/SingleMuon/NANOAOD/Nano14Dec2018-v1/280000/49420DB4-415F-3346-95E0-9B0EF95CB9DD.root',
       '/store/data/Run2017F/SingleMuon/NANOAOD/Nano14Dec2018-v1/280000/4995CE50-B33F-8C43-B855-C4B03FC85C6D.root',
       '/store/data/Run2017F/SingleMuon/NANOAOD/Nano14Dec2018-v1/280000/4C87599C-8127-EC48-BDDE-A0C1BFE85FE1.root',
       '/store/data/Run2017F/SingleMuon/NANOAOD/Nano14Dec2018-v1/280000/4E8A7764-6066-5740-870D-194C3EB58595.root',
       '/store/data/Run2017F/SingleMuon/NANOAOD/Nano14Dec2018-v1/280000/4F4910AA-2776-D24D-BC5C-87EE5520B711.root',
       '/store/data/Run2017F/SingleMuon/NANOAOD/Nano14Dec2018-v1/280000/50095045-E819-2C4A-8E59-E5EC8F0D6C2C.root',
       '/store/data/Run2017F/SingleMuon/NANOAOD/Nano14Dec2018-v1/280000/55626A24-66C9-B641-94FE-DEDAD80759A0.root',
       '/store/data/Run2017F/SingleMuon/NANOAOD/Nano14Dec2018-v1/280000/55862DD1-BECF-8444-B3A8-0F311AD94ADA.root',
       '/store/data/Run2017F/SingleMuon/NANOAOD/Nano14Dec2018-v1/280000/56991CCF-20FF-2742-8759-5B7791794946.root',
       '/store/data/Run2017F/SingleMuon/NANOAOD/Nano14Dec2018-v1/280000/571F776E-0BBF-0944-B9BA-A8C836ADA3D9.root',
       '/store/data/Run2017F/SingleMuon/NANOAOD/Nano14Dec2018-v1/280000/59C88D23-9B53-A741-8BBC-E8B07E824EFB.root',
       '/store/data/Run2017F/SingleMuon/NANOAOD/Nano14Dec2018-v1/280000/5AF68C7C-55FF-7346-9850-1F111C811968.root',
       '/store/data/Run2017F/SingleMuon/NANOAOD/Nano14Dec2018-v1/280000/5C980020-7798-7B4D-B7B5-54EAA473D79A.root',
       '/store/data/Run2017F/SingleMuon/NANOAOD/Nano14Dec2018-v1/280000/5E63DF83-9954-AE4D-B6D0-C64C4C089607.root',
       '/store/data/Run2017F/SingleMuon/NANOAOD/Nano14Dec2018-v1/280000/604A6B17-2A8C-6847-B670-5A8E2E453B92.root',
       '/store/data/Run2017F/SingleMuon/NANOAOD/Nano14Dec2018-v1/280000/62C086B8-BCDD-A042-AE4C-B69C4DEDA145.root',
       '/store/data/Run2017F/SingleMuon/NANOAOD/Nano14Dec2018-v1/280000/644899F9-29F4-644D-AAC5-A2871EC2B407.root',
       '/store/data/Run2017F/SingleMuon/NANOAOD/Nano14Dec2018-v1/280000/64D5D4D0-7149-F240-997F-4F6A71083FF3.root',
       '/store/data/Run2017F/SingleMuon/NANOAOD/Nano14Dec2018-v1/280000/676411F6-40BF-DB43-94A5-27D08BF95D8E.root',
       '/store/data/Run2017F/SingleMuon/NANOAOD/Nano14Dec2018-v1/280000/676AC9E9-026A-CA47-86B8-50F68952475D.root',
       '/store/data/Run2017F/SingleMuon/NANOAOD/Nano14Dec2018-v1/280000/6991FFC8-FF3B-4041-863A-9EEFBD74A55F.root',
       '/store/data/Run2017F/SingleMuon/NANOAOD/Nano14Dec2018-v1/280000/6C1B91DE-B68D-5949-9A14-DE8C2DB390B7.root',
       '/store/data/Run2017F/SingleMuon/NANOAOD/Nano14Dec2018-v1/280000/6E6E7B60-2347-554C-9685-F6C73BDA3786.root',
       '/store/data/Run2017F/SingleMuon/NANOAOD/Nano14Dec2018-v1/280000/6FBD6741-52E0-474F-ADA2-AC5A4DA12A26.root',
       '/store/data/Run2017F/SingleMuon/NANOAOD/Nano14Dec2018-v1/280000/7400038A-2B44-0B4A-8590-6ACBAAFAB57A.root',
       '/store/data/Run2017F/SingleMuon/NANOAOD/Nano14Dec2018-v1/280000/746A0852-62CC-854A-BEB6-8CABCAE17C75.root',
       '/store/data/Run2017F/SingleMuon/NANOAOD/Nano14Dec2018-v1/280000/767778FE-44EA-2841-87BD-39DDD9D6C28B.root',
       '/store/data/Run2017F/SingleMuon/NANOAOD/Nano14Dec2018-v1/280000/7827EEE5-59BB-AC4B-9B69-53D035259DA7.root',
       '/store/data/Run2017F/SingleMuon/NANOAOD/Nano14Dec2018-v1/280000/7B2780DD-B3A7-754B-B2B0-02759EFA5EAC.root',
       '/store/data/Run2017F/SingleMuon/NANOAOD/Nano14Dec2018-v1/280000/7E322B0D-E7A9-5B43-9EE6-B4F9CA5708A9.root',
       '/store/data/Run2017F/SingleMuon/NANOAOD/Nano14Dec2018-v1/280000/7E92FDA8-2B52-FB45-BB46-343B001C48A1.root',
       '/store/data/Run2017F/SingleMuon/NANOAOD/Nano14Dec2018-v1/280000/835F073D-A4A1-3B4C-B62D-6080CFF4FE5B.root',
       '/store/data/Run2017F/SingleMuon/NANOAOD/Nano14Dec2018-v1/280000/9079EA4F-C3A5-E241-A016-7694C8B12F4C.root',
       '/store/data/Run2017F/SingleMuon/NANOAOD/Nano14Dec2018-v1/280000/92166549-FA76-D84D-B3EA-F499967C4983.root',
       '/store/data/Run2017F/SingleMuon/NANOAOD/Nano14Dec2018-v1/280000/929E5F10-5023-FE48-A919-C38B3A4C0E47.root',
       '/store/data/Run2017F/SingleMuon/NANOAOD/Nano14Dec2018-v1/280000/9432A1FD-9D91-3D41-BE8C-204B81C592AF.root',
       '/store/data/Run2017F/SingleMuon/NANOAOD/Nano14Dec2018-v1/280000/980DC494-E48A-0043-A629-ED9149D908E9.root',
       '/store/data/Run2017F/SingleMuon/NANOAOD/Nano14Dec2018-v1/280000/9A38BC68-B430-2341-8951-9C70D790A826.root',
       '/store/data/Run2017F/SingleMuon/NANOAOD/Nano14Dec2018-v1/280000/9A677586-9D97-2247-A5AB-7E9A16E0A91A.root',
       '/store/data/Run2017F/SingleMuon/NANOAOD/Nano14Dec2018-v1/280000/9B4619AF-F8EA-074D-BB0F-ACD5B3C7A379.root',
       '/store/data/Run2017F/SingleMuon/NANOAOD/Nano14Dec2018-v1/280000/A1169E9A-62AA-984A-9A37-A85BDD0EFC64.root',
       '/store/data/Run2017F/SingleMuon/NANOAOD/Nano14Dec2018-v1/280000/A2877B27-6C91-1F47-A2F5-968E5BA0F9C5.root',
       '/store/data/Run2017F/SingleMuon/NANOAOD/Nano14Dec2018-v1/280000/A2C2F971-A0DD-4741-9560-7099CD501D9F.root',
       '/store/data/Run2017F/SingleMuon/NANOAOD/Nano14Dec2018-v1/280000/A6628EB8-DAB0-0B46-B8A2-51964DC3AFFC.root',
       '/store/data/Run2017F/SingleMuon/NANOAOD/Nano14Dec2018-v1/280000/A727EE26-17BE-7540-9338-5C2822B7C996.root',
       '/store/data/Run2017F/SingleMuon/NANOAOD/Nano14Dec2018-v1/280000/A7A52720-9985-594C-889B-F411FB8F6B45.root',
       '/store/data/Run2017F/SingleMuon/NANOAOD/Nano14Dec2018-v1/280000/A7C0B7A3-D69C-8140-9B82-07F8BB28E433.root',
       '/store/data/Run2017F/SingleMuon/NANOAOD/Nano14Dec2018-v1/280000/A7EFF5DE-B855-DD49-B00A-06AD219A6A51.root',
       '/store/data/Run2017F/SingleMuon/NANOAOD/Nano14Dec2018-v1/280000/A9D7CD12-7896-EB4F-8AB2-9500F807C3B2.root',
       '/store/data/Run2017F/SingleMuon/NANOAOD/Nano14Dec2018-v1/280000/AC9D87B4-21CB-5442-87B1-4BFE1E5471E6.root',
       '/store/data/Run2017F/SingleMuon/NANOAOD/Nano14Dec2018-v1/280000/B0747153-FE27-AA4E-8219-AB88D6E7C27B.root',
       '/store/data/Run2017F/SingleMuon/NANOAOD/Nano14Dec2018-v1/280000/B2368AA4-DF46-A64A-9BBB-E076AE0D1396.root',
       '/store/data/Run2017F/SingleMuon/NANOAOD/Nano14Dec2018-v1/280000/B4353A06-B0AE-8441-AD47-26AE79F6BFD0.root',
       '/store/data/Run2017F/SingleMuon/NANOAOD/Nano14Dec2018-v1/280000/B5D4D504-D5D6-A141-896A-DA14CD707936.root',
       '/store/data/Run2017F/SingleMuon/NANOAOD/Nano14Dec2018-v1/280000/C3A0A0CE-F6EB-E744-BEE2-6C096F293A62.root',
       '/store/data/Run2017F/SingleMuon/NANOAOD/Nano14Dec2018-v1/280000/C7EF7D12-8175-BB4D-9A9B-2A4B9BDC8B62.root',
       '/store/data/Run2017F/SingleMuon/NANOAOD/Nano14Dec2018-v1/280000/CE603670-0804-C94A-A63F-83FCB0FF754A.root',
       '/store/data/Run2017F/SingleMuon/NANOAOD/Nano14Dec2018-v1/280000/D00BCA14-A13D-024F-BF33-82D865E06ADA.root',
       '/store/data/Run2017F/SingleMuon/NANOAOD/Nano14Dec2018-v1/280000/D05FC7D3-5C3F-BB47-A70F-B6DF75873FFD.root',
       '/store/data/Run2017F/SingleMuon/NANOAOD/Nano14Dec2018-v1/280000/D14466E1-ECC3-BD4E-B44E-AF7C2A9FC162.root',
       '/store/data/Run2017F/SingleMuon/NANOAOD/Nano14Dec2018-v1/280000/D1F9E5C9-D569-1C45-A510-279125FE2A79.root',
       '/store/data/Run2017F/SingleMuon/NANOAOD/Nano14Dec2018-v1/280000/D4756BDC-6448-0B49-BC1C-934F1FA4861B.root',
       '/store/data/Run2017F/SingleMuon/NANOAOD/Nano14Dec2018-v1/280000/D82D294F-E868-BB44-93DD-641D81ABF952.root',
       '/store/data/Run2017F/SingleMuon/NANOAOD/Nano14Dec2018-v1/280000/D92B9CCC-87DD-A644-9488-838FA0A813B7.root',
       '/store/data/Run2017F/SingleMuon/NANOAOD/Nano14Dec2018-v1/280000/DB50B124-F64A-DF4A-98D3-E375E8744BEC.root',
       '/store/data/Run2017F/SingleMuon/NANOAOD/Nano14Dec2018-v1/280000/DBD6F0AD-79ED-1647-8687-1BC841AD08C4.root',
       '/store/data/Run2017F/SingleMuon/NANOAOD/Nano14Dec2018-v1/280000/DD3346BD-D1EB-4F44-A63A-62F85CC1E7AF.root',
       '/store/data/Run2017F/SingleMuon/NANOAOD/Nano14Dec2018-v1/280000/E08FDDDE-1DDC-C245-953F-EDCB83AE7415.root',
       '/store/data/Run2017F/SingleMuon/NANOAOD/Nano14Dec2018-v1/280000/E12A6176-3E96-1940-9279-4358F36C7CAC.root',
       '/store/data/Run2017F/SingleMuon/NANOAOD/Nano14Dec2018-v1/280000/E52EE480-994E-A546-8536-90D7790AB1D2.root',
       '/store/data/Run2017F/SingleMuon/NANOAOD/Nano14Dec2018-v1/280000/E5EB3204-EAB0-0042-A144-E73C6C55E7CE.root',
       '/store/data/Run2017F/SingleMuon/NANOAOD/Nano14Dec2018-v1/280000/E6E08FE7-7120-9745-80A2-9BCB30BC0F6B.root',
       '/store/data/Run2017F/SingleMuon/NANOAOD/Nano14Dec2018-v1/280000/E8638610-B650-E34A-BA81-D113563998D0.root',
       '/store/data/Run2017F/SingleMuon/NANOAOD/Nano14Dec2018-v1/280000/EA6A1E1F-7AD3-3245-8B24-7D88142FC64A.root',
       '/store/data/Run2017F/SingleMuon/NANOAOD/Nano14Dec2018-v1/280000/EFF2CB70-66CD-8A4D-B0C4-CBC8A0414B2F.root',
       '/store/data/Run2017F/SingleMuon/NANOAOD/Nano14Dec2018-v1/280000/F311699F-BCE0-EA45-9ECC-D77CB612AA51.root',
       '/store/data/Run2017F/SingleMuon/NANOAOD/Nano14Dec2018-v1/280000/F37D8A26-277B-B14A-B70D-FD8C797EE9DF.root',
       '/store/data/Run2017F/SingleMuon/NANOAOD/Nano14Dec2018-v1/280000/F38C4342-D634-5241-BC55-E20DD749D32E.root',
       '/store/data/Run2017F/SingleMuon/NANOAOD/Nano14Dec2018-v1/280000/FA955F54-8B33-184E-B60A-B51E47DE5C0B.root',
       '/store/data/Run2017F/SingleMuon/NANOAOD/Nano14Dec2018-v1/280000/FACA12DA-8BDA-2449-82B2-9CD86D3D9B8F.root',
       '/store/data/Run2017F/SingleMuon/NANOAOD/Nano14Dec2018-v1/280000/FBD2039F-19A0-8349-A701-2DA65B993696.root',
       '/store/data/Run2017F/SingleMuon/NANOAOD/Nano14Dec2018-v1/280000/FEDD21C9-8ED3-844C-B3F4-3192F4044D36.root',
       '/store/data/Run2017F/SingleMuon/NANOAOD/Nano14Dec2018-v1/280000/FFD34BFF-3B0D-2240-AB20-C34A0F74DA2A.root',
] )
