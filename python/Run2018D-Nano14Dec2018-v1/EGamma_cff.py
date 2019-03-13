import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/data/Run2018D/EGamma/NANOAOD/Nano14Dec2018_ver2-v1/210000/3A5D497C-ADCD-EB47-9CD2-9E3B97E51789.root',
       '/store/data/Run2018D/EGamma/NANOAOD/Nano14Dec2018_ver2-v1/280000/05371338-2BC6-8547-85C4-50D432AB7BA1.root',
       '/store/data/Run2018D/EGamma/NANOAOD/Nano14Dec2018_ver2-v1/280000/0664AB5B-C12F-254F-9854-241226A2E4F3.root',
       '/store/data/Run2018D/EGamma/NANOAOD/Nano14Dec2018_ver2-v1/280000/0726107C-DABE-8C40-A1C4-1ED495619EDE.root',
       '/store/data/Run2018D/EGamma/NANOAOD/Nano14Dec2018_ver2-v1/280000/10E9FA32-9AC0-4745-9BCE-187B72DCB692.root',
       '/store/data/Run2018D/EGamma/NANOAOD/Nano14Dec2018_ver2-v1/280000/12C7CF3C-BB1D-3041-98C8-E23FDC78DE4C.root',
       '/store/data/Run2018D/EGamma/NANOAOD/Nano14Dec2018_ver2-v1/280000/14DF6BD1-14B1-1346-889F-AA6DCAA0D210.root',
       '/store/data/Run2018D/EGamma/NANOAOD/Nano14Dec2018_ver2-v1/280000/1552CFC1-4870-A64D-BE8E-D652CFF8D0AE.root',
       '/store/data/Run2018D/EGamma/NANOAOD/Nano14Dec2018_ver2-v1/280000/16D99C2E-D8A6-004F-B1E5-3577CD169D53.root',
       '/store/data/Run2018D/EGamma/NANOAOD/Nano14Dec2018_ver2-v1/280000/1906794F-7579-9F48-8FEE-73619BE3C8B8.root',
       '/store/data/Run2018D/EGamma/NANOAOD/Nano14Dec2018_ver2-v1/280000/19C8CE99-C19D-1B44-8AE3-095DF1F99C34.root',
       '/store/data/Run2018D/EGamma/NANOAOD/Nano14Dec2018_ver2-v1/280000/1B762EEA-BEFC-3B48-A62A-0B2330C7DC3A.root',
       '/store/data/Run2018D/EGamma/NANOAOD/Nano14Dec2018_ver2-v1/280000/1C1BAEC8-0F6A-4D44-8FD0-3EB5B5D07927.root',
       '/store/data/Run2018D/EGamma/NANOAOD/Nano14Dec2018_ver2-v1/280000/2013BF79-A4E4-2642-B330-8F16CF77874E.root',
       '/store/data/Run2018D/EGamma/NANOAOD/Nano14Dec2018_ver2-v1/280000/21402AB6-437C-FF4B-9A44-AC446C0D7412.root',
       '/store/data/Run2018D/EGamma/NANOAOD/Nano14Dec2018_ver2-v1/280000/259F4850-9266-D448-905D-2BEB9B0F6A1D.root',
       '/store/data/Run2018D/EGamma/NANOAOD/Nano14Dec2018_ver2-v1/280000/2780F906-FB9D-924A-8029-77283D474500.root',
       '/store/data/Run2018D/EGamma/NANOAOD/Nano14Dec2018_ver2-v1/280000/2802D4BD-3982-0843-8A5F-BD3B1D7240C6.root',
       '/store/data/Run2018D/EGamma/NANOAOD/Nano14Dec2018_ver2-v1/280000/2FB1836D-657B-1E42-BD9F-47133168592C.root',
       '/store/data/Run2018D/EGamma/NANOAOD/Nano14Dec2018_ver2-v1/280000/3067F545-5563-B740-88EE-C35112D576AC.root',
       '/store/data/Run2018D/EGamma/NANOAOD/Nano14Dec2018_ver2-v1/280000/30F9C25A-5BB5-624F-AFAA-26D8B3E8EA9D.root',
       '/store/data/Run2018D/EGamma/NANOAOD/Nano14Dec2018_ver2-v1/280000/328DD0A7-8D2E-D741-8F11-829C08A8A9C4.root',
       '/store/data/Run2018D/EGamma/NANOAOD/Nano14Dec2018_ver2-v1/280000/37093DAF-BF67-7443-99FD-E0E7051792E2.root',
       '/store/data/Run2018D/EGamma/NANOAOD/Nano14Dec2018_ver2-v1/280000/42F3F11B-889C-E241-83A1-78B65F5DB606.root',
       '/store/data/Run2018D/EGamma/NANOAOD/Nano14Dec2018_ver2-v1/280000/44F5D745-5FA4-B840-A5BE-BF0C138D1D89.root',
       '/store/data/Run2018D/EGamma/NANOAOD/Nano14Dec2018_ver2-v1/280000/47D2D37C-EF43-144D-9549-17C29A999D4B.root',
       '/store/data/Run2018D/EGamma/NANOAOD/Nano14Dec2018_ver2-v1/280000/4825D146-4298-2A43-AA14-4230EDC5343D.root',
       '/store/data/Run2018D/EGamma/NANOAOD/Nano14Dec2018_ver2-v1/280000/48A08B73-ECA9-6047-9F76-67225A59E5DD.root',
       '/store/data/Run2018D/EGamma/NANOAOD/Nano14Dec2018_ver2-v1/280000/4D2158CC-3957-E54C-9B2F-9DA8574F989E.root',
       '/store/data/Run2018D/EGamma/NANOAOD/Nano14Dec2018_ver2-v1/280000/4D7871C6-6F49-2D4C-859B-B97E291083C0.root',
       '/store/data/Run2018D/EGamma/NANOAOD/Nano14Dec2018_ver2-v1/280000/54EDAD20-7A8E-B24E-9A9D-F12F84710004.root',
       '/store/data/Run2018D/EGamma/NANOAOD/Nano14Dec2018_ver2-v1/280000/5BD3E733-496E-3E4C-8570-D75200834605.root',
       '/store/data/Run2018D/EGamma/NANOAOD/Nano14Dec2018_ver2-v1/280000/5C7DC03D-9868-FF4C-A910-3D3E9C8D78D1.root',
       '/store/data/Run2018D/EGamma/NANOAOD/Nano14Dec2018_ver2-v1/280000/5EA087D0-2C26-0649-A7F6-EBC676E32F81.root',
       '/store/data/Run2018D/EGamma/NANOAOD/Nano14Dec2018_ver2-v1/280000/61EDEA4D-8622-1445-A163-9DAF42AF9FCF.root',
       '/store/data/Run2018D/EGamma/NANOAOD/Nano14Dec2018_ver2-v1/280000/620D96C9-2D0C-1044-8EF9-F2258E779ACB.root',
       '/store/data/Run2018D/EGamma/NANOAOD/Nano14Dec2018_ver2-v1/280000/6409D6F7-758C-C14D-86D1-D475281F47C7.root',
       '/store/data/Run2018D/EGamma/NANOAOD/Nano14Dec2018_ver2-v1/280000/652597AE-3652-1E4A-959C-FE14EDAD7727.root',
       '/store/data/Run2018D/EGamma/NANOAOD/Nano14Dec2018_ver2-v1/280000/68D238DF-EA13-0F45-8A97-9562090C44AE.root',
       '/store/data/Run2018D/EGamma/NANOAOD/Nano14Dec2018_ver2-v1/280000/693419B7-5285-2943-9038-9F6C97178926.root',
       '/store/data/Run2018D/EGamma/NANOAOD/Nano14Dec2018_ver2-v1/280000/6CDEC063-979E-A545-BA24-D5CA062BE77B.root',
       '/store/data/Run2018D/EGamma/NANOAOD/Nano14Dec2018_ver2-v1/280000/6EEDFC69-77D3-DF4D-85C4-579C8FD30FE9.root',
       '/store/data/Run2018D/EGamma/NANOAOD/Nano14Dec2018_ver2-v1/280000/6EEE1395-86B9-8D4B-B897-156363C9708E.root',
       '/store/data/Run2018D/EGamma/NANOAOD/Nano14Dec2018_ver2-v1/280000/6F83D7B9-1DCD-D24C-B639-2EE47578BABB.root',
       '/store/data/Run2018D/EGamma/NANOAOD/Nano14Dec2018_ver2-v1/280000/71D80A51-1465-4F4D-9D09-7F6499CCC446.root',
       '/store/data/Run2018D/EGamma/NANOAOD/Nano14Dec2018_ver2-v1/280000/74BB49EF-FF6A-B14B-B3F4-B92150C50A68.root',
       '/store/data/Run2018D/EGamma/NANOAOD/Nano14Dec2018_ver2-v1/280000/757CC01A-89AD-D04C-914E-88A08159E265.root',
       '/store/data/Run2018D/EGamma/NANOAOD/Nano14Dec2018_ver2-v1/280000/75CFE68E-7D8C-614A-A8C3-B95A49A0B208.root',
       '/store/data/Run2018D/EGamma/NANOAOD/Nano14Dec2018_ver2-v1/280000/7677418C-0DA6-EC43-B961-D9032D6C2946.root',
       '/store/data/Run2018D/EGamma/NANOAOD/Nano14Dec2018_ver2-v1/280000/775BF1C4-66AD-3B43-AC19-55849A47A030.root',
       '/store/data/Run2018D/EGamma/NANOAOD/Nano14Dec2018_ver2-v1/280000/77C94BA2-7DC4-3C40-BD19-8E0B0FFDEA75.root',
       '/store/data/Run2018D/EGamma/NANOAOD/Nano14Dec2018_ver2-v1/280000/7A4AD695-550E-2445-8931-4244EF33B5C9.root',
       '/store/data/Run2018D/EGamma/NANOAOD/Nano14Dec2018_ver2-v1/280000/7ADE32E6-73AB-0A4A-BF7E-4AD6296B9833.root',
       '/store/data/Run2018D/EGamma/NANOAOD/Nano14Dec2018_ver2-v1/280000/7B25C7DA-8797-4D4F-A20D-582BFF0CC3FE.root',
       '/store/data/Run2018D/EGamma/NANOAOD/Nano14Dec2018_ver2-v1/280000/7D4BC219-24F3-E546-8BDB-197075E5DE6E.root',
       '/store/data/Run2018D/EGamma/NANOAOD/Nano14Dec2018_ver2-v1/280000/7E027E3A-BC2E-0641-BB96-48756DA35882.root',
       '/store/data/Run2018D/EGamma/NANOAOD/Nano14Dec2018_ver2-v1/280000/8101CDF6-8980-8346-8DAB-0C79AE529CCA.root',
       '/store/data/Run2018D/EGamma/NANOAOD/Nano14Dec2018_ver2-v1/280000/836F152C-86B7-0746-817C-CF8E567278AF.root',
       '/store/data/Run2018D/EGamma/NANOAOD/Nano14Dec2018_ver2-v1/280000/8553512A-3F6E-8143-A992-08C156C56B4A.root',
       '/store/data/Run2018D/EGamma/NANOAOD/Nano14Dec2018_ver2-v1/280000/85AA10DE-286C-FC43-8E1F-21ACB3DC2145.root',
       '/store/data/Run2018D/EGamma/NANOAOD/Nano14Dec2018_ver2-v1/280000/85D83141-D941-294E-8068-19188679AAEC.root',
       '/store/data/Run2018D/EGamma/NANOAOD/Nano14Dec2018_ver2-v1/280000/8A85DD2A-D6A1-5A49-A5D1-2C8F55AB0497.root',
       '/store/data/Run2018D/EGamma/NANOAOD/Nano14Dec2018_ver2-v1/280000/8BA1D14A-83B1-944F-AFFA-FA7E00896A0C.root',
       '/store/data/Run2018D/EGamma/NANOAOD/Nano14Dec2018_ver2-v1/280000/8CB8B84A-07FD-D949-925C-95CA6A065F3A.root',
       '/store/data/Run2018D/EGamma/NANOAOD/Nano14Dec2018_ver2-v1/280000/8DABB630-09D5-A742-9478-BD96404586D3.root',
       '/store/data/Run2018D/EGamma/NANOAOD/Nano14Dec2018_ver2-v1/280000/8E1F22EA-A076-0F4C-8B22-5E22EC40056E.root',
       '/store/data/Run2018D/EGamma/NANOAOD/Nano14Dec2018_ver2-v1/280000/8E578F52-9E5B-0547-B5D7-A61085609ADE.root',
       '/store/data/Run2018D/EGamma/NANOAOD/Nano14Dec2018_ver2-v1/280000/8FD25FF8-1F8A-0747-A8A7-26E6395AF103.root',
       '/store/data/Run2018D/EGamma/NANOAOD/Nano14Dec2018_ver2-v1/280000/903B72D6-3B0D-3843-A205-6177191FF6CB.root',
       '/store/data/Run2018D/EGamma/NANOAOD/Nano14Dec2018_ver2-v1/280000/91A60BAF-56D6-1449-BA94-407DCC984FE5.root',
       '/store/data/Run2018D/EGamma/NANOAOD/Nano14Dec2018_ver2-v1/280000/921CCE05-0271-114F-B04D-83E1FD6CE82E.root',
       '/store/data/Run2018D/EGamma/NANOAOD/Nano14Dec2018_ver2-v1/280000/976714A6-21DC-864A-86F3-D43181B4CEB3.root',
       '/store/data/Run2018D/EGamma/NANOAOD/Nano14Dec2018_ver2-v1/280000/990E9A9A-DB0C-AD44-B673-0A778DEF423B.root',
       '/store/data/Run2018D/EGamma/NANOAOD/Nano14Dec2018_ver2-v1/280000/A0DCFD23-45CE-4443-8E0A-29A76CF46635.root',
       '/store/data/Run2018D/EGamma/NANOAOD/Nano14Dec2018_ver2-v1/280000/A2D276EF-3A6F-B84F-9750-EB12D4C67EDF.root',
       '/store/data/Run2018D/EGamma/NANOAOD/Nano14Dec2018_ver2-v1/280000/A306112C-93DB-1044-9118-357B9BBF544F.root',
       '/store/data/Run2018D/EGamma/NANOAOD/Nano14Dec2018_ver2-v1/280000/AA99CAEA-E040-D444-87A9-85A8C898C6CC.root',
       '/store/data/Run2018D/EGamma/NANOAOD/Nano14Dec2018_ver2-v1/280000/AB406CE1-F003-1847-ABAE-7739CC5FB9CF.root',
       '/store/data/Run2018D/EGamma/NANOAOD/Nano14Dec2018_ver2-v1/280000/AE01F257-776E-4142-9C77-026564FEEF36.root',
       '/store/data/Run2018D/EGamma/NANOAOD/Nano14Dec2018_ver2-v1/280000/AF064C1C-4815-D04C-8A24-B650D6B6BFF0.root',
       '/store/data/Run2018D/EGamma/NANOAOD/Nano14Dec2018_ver2-v1/280000/B1DC243C-4172-9F40-81CF-39974D188300.root',
       '/store/data/Run2018D/EGamma/NANOAOD/Nano14Dec2018_ver2-v1/280000/B3D023C5-6387-7245-BA4B-5E3AC8C1019C.root',
       '/store/data/Run2018D/EGamma/NANOAOD/Nano14Dec2018_ver2-v1/280000/B88B7A2E-E90C-A34F-8495-91D99D0E97E8.root',
       '/store/data/Run2018D/EGamma/NANOAOD/Nano14Dec2018_ver2-v1/280000/B9CA6D8F-D063-DF4A-95B8-6B935FF8AA93.root',
       '/store/data/Run2018D/EGamma/NANOAOD/Nano14Dec2018_ver2-v1/280000/BB79B958-CEAD-0848-AC3A-587CCF1D6862.root',
       '/store/data/Run2018D/EGamma/NANOAOD/Nano14Dec2018_ver2-v1/280000/C12CA2E1-4AFD-564D-815B-529EEA444580.root',
       '/store/data/Run2018D/EGamma/NANOAOD/Nano14Dec2018_ver2-v1/280000/C4C1E88D-CC9A-1C44-A00D-E086E2524ADC.root',
       '/store/data/Run2018D/EGamma/NANOAOD/Nano14Dec2018_ver2-v1/280000/C5A9BB4B-70BB-C046-BEF4-3AA9FB1A28A8.root',
       '/store/data/Run2018D/EGamma/NANOAOD/Nano14Dec2018_ver2-v1/280000/C6DC945E-60D1-B64C-9A2C-0B9103412CA7.root',
       '/store/data/Run2018D/EGamma/NANOAOD/Nano14Dec2018_ver2-v1/280000/C8195891-D2AB-3D49-A57A-3763BA27DCEB.root',
       '/store/data/Run2018D/EGamma/NANOAOD/Nano14Dec2018_ver2-v1/280000/CC2AF3DE-A814-D740-884E-1ECA52D4D20E.root',
       '/store/data/Run2018D/EGamma/NANOAOD/Nano14Dec2018_ver2-v1/280000/CF51184A-90CC-A74D-87AA-2CA45627A5D0.root',
       '/store/data/Run2018D/EGamma/NANOAOD/Nano14Dec2018_ver2-v1/280000/D0901A8F-A82E-5C40-B39B-60F3EAE2C1CD.root',
       '/store/data/Run2018D/EGamma/NANOAOD/Nano14Dec2018_ver2-v1/280000/D5836BD4-5E5C-064C-829A-FE7718EB0169.root',
       '/store/data/Run2018D/EGamma/NANOAOD/Nano14Dec2018_ver2-v1/280000/D6A19621-FE65-D545-96C0-9EC248E82EE7.root',
       '/store/data/Run2018D/EGamma/NANOAOD/Nano14Dec2018_ver2-v1/280000/D7D68BA4-5939-9F40-8113-79C3A4E67D51.root',
       '/store/data/Run2018D/EGamma/NANOAOD/Nano14Dec2018_ver2-v1/280000/D90C360B-A0EC-6043-AE5D-FC3DD069FF59.root',
       '/store/data/Run2018D/EGamma/NANOAOD/Nano14Dec2018_ver2-v1/280000/D9409F25-FC18-1F44-B168-E333333F618F.root',
       '/store/data/Run2018D/EGamma/NANOAOD/Nano14Dec2018_ver2-v1/280000/D9AA0428-BA3A-FE4D-8223-79B8ACED5A64.root',
       '/store/data/Run2018D/EGamma/NANOAOD/Nano14Dec2018_ver2-v1/280000/DAB1A95A-49EC-1E49-88A0-09C7B7D9EA05.root',
       '/store/data/Run2018D/EGamma/NANOAOD/Nano14Dec2018_ver2-v1/280000/DBECE2CF-07F8-6B42-B1FB-211E67354501.root',
       '/store/data/Run2018D/EGamma/NANOAOD/Nano14Dec2018_ver2-v1/280000/DDE966F5-6F11-3249-8B6B-D4AB4ED1BD14.root',
       '/store/data/Run2018D/EGamma/NANOAOD/Nano14Dec2018_ver2-v1/280000/DF5BB24C-0723-5344-9251-768237A1915E.root',
       '/store/data/Run2018D/EGamma/NANOAOD/Nano14Dec2018_ver2-v1/280000/E078508B-549D-BF4F-AD08-3EF92FFD17C6.root',
       '/store/data/Run2018D/EGamma/NANOAOD/Nano14Dec2018_ver2-v1/280000/E0E3C723-1083-9840-A9F3-2D3940C63FA8.root',
       '/store/data/Run2018D/EGamma/NANOAOD/Nano14Dec2018_ver2-v1/280000/E1DAB5B0-683A-B34F-8F5C-F8C91F00FE34.root',
       '/store/data/Run2018D/EGamma/NANOAOD/Nano14Dec2018_ver2-v1/280000/E44F6E52-D37E-5749-B03F-5C99CFD85673.root',
       '/store/data/Run2018D/EGamma/NANOAOD/Nano14Dec2018_ver2-v1/280000/E4741356-07F1-5345-8CD0-733BA3B17ADB.root',
       '/store/data/Run2018D/EGamma/NANOAOD/Nano14Dec2018_ver2-v1/280000/E49B78E2-8D21-EF4E-8C5B-F3467D9FEE22.root',
       '/store/data/Run2018D/EGamma/NANOAOD/Nano14Dec2018_ver2-v1/280000/E5496B7C-05F0-CD46-AF48-EAF143DC415C.root',
       '/store/data/Run2018D/EGamma/NANOAOD/Nano14Dec2018_ver2-v1/280000/E6684E59-2AB9-6243-AB0A-A8E1B77EB70C.root',
       '/store/data/Run2018D/EGamma/NANOAOD/Nano14Dec2018_ver2-v1/280000/E7114B0B-9868-B446-8B11-02E3D5087FF7.root',
       '/store/data/Run2018D/EGamma/NANOAOD/Nano14Dec2018_ver2-v1/280000/E808D2DF-B6C8-8E4C-833F-057528DB29A7.root',
       '/store/data/Run2018D/EGamma/NANOAOD/Nano14Dec2018_ver2-v1/280000/EEC164BC-44E9-C746-856E-E20DB7F0DA66.root',
       '/store/data/Run2018D/EGamma/NANOAOD/Nano14Dec2018_ver2-v1/280000/F012AB63-D49B-AE40-BB61-B2562B2EF873.root',
       '/store/data/Run2018D/EGamma/NANOAOD/Nano14Dec2018_ver2-v1/280000/F254FFB1-8486-6646-9EA6-78EE4A3D1553.root',
       '/store/data/Run2018D/EGamma/NANOAOD/Nano14Dec2018_ver2-v1/280000/F30834D9-2DAC-4A40-99E1-5E1547E9FE3E.root',
       '/store/data/Run2018D/EGamma/NANOAOD/Nano14Dec2018_ver2-v1/280000/FB096B82-9ECF-1C46-80AD-111B9692B97E.root',
       '/store/data/Run2018D/EGamma/NANOAOD/Nano14Dec2018_ver2-v1/280000/FB518A8D-EA64-6341-9AE2-8A44CBEDDFED.root',
       '/store/data/Run2018D/EGamma/NANOAOD/Nano14Dec2018_ver2-v1/280000/FD60A9BA-20C2-424D-853B-F9F50293A71D.root',
       '/store/data/Run2018D/EGamma/NANOAOD/Nano14Dec2018_ver2-v1/280000/FE00D8CF-A8CA-4847-A7DB-1C2EB8951D26.root',
       '/store/data/Run2018D/EGamma/NANOAOD/Nano14Dec2018_ver2-v1/280000/FE5DD4E3-FF73-3F4F-AB4D-01657C731F52.root',
       '/store/data/Run2018D/EGamma/NANOAOD/Nano14Dec2018_ver2-v1/30000/4FFAE261-F1EF-5D49-9D97-C7921EBC0232.root',
       '/store/data/Run2018D/EGamma/NANOAOD/Nano14Dec2018_ver2-v1/40000/009BEE38-4273-1B41-9099-B0A44D7EAE2A.root',
       '/store/data/Run2018D/EGamma/NANOAOD/Nano14Dec2018_ver2-v1/40000/09A6B96B-6745-CA4F-8103-471D79A8279D.root',
       '/store/data/Run2018D/EGamma/NANOAOD/Nano14Dec2018_ver2-v1/40000/0C369107-14C1-2B45-BF15-51B1B901BB0B.root',
       '/store/data/Run2018D/EGamma/NANOAOD/Nano14Dec2018_ver2-v1/40000/14080D30-B131-1245-BB78-8CAC3B0C5F57.root',
       '/store/data/Run2018D/EGamma/NANOAOD/Nano14Dec2018_ver2-v1/40000/1733E7BA-ABCF-3E4E-8B52-E25E5A5B9CF1.root',
       '/store/data/Run2018D/EGamma/NANOAOD/Nano14Dec2018_ver2-v1/40000/18439766-70C5-804F-B8AE-19D20989E7A5.root',
       '/store/data/Run2018D/EGamma/NANOAOD/Nano14Dec2018_ver2-v1/40000/18686C3A-9C02-1742-A977-05818D1CCAAF.root',
       '/store/data/Run2018D/EGamma/NANOAOD/Nano14Dec2018_ver2-v1/40000/18F55BF4-9321-7647-9FF3-F9CC903F6133.root',
       '/store/data/Run2018D/EGamma/NANOAOD/Nano14Dec2018_ver2-v1/40000/19915706-4ABB-114A-B097-1947DB7AA22A.root',
       '/store/data/Run2018D/EGamma/NANOAOD/Nano14Dec2018_ver2-v1/40000/1BF4189B-E526-844C-870A-A3AA357FC727.root',
       '/store/data/Run2018D/EGamma/NANOAOD/Nano14Dec2018_ver2-v1/40000/1E949E1C-C351-D042-AEBE-BD7B5636ED17.root',
       '/store/data/Run2018D/EGamma/NANOAOD/Nano14Dec2018_ver2-v1/40000/209E8231-4B4E-C442-BC9C-88C9D4983B9D.root',
       '/store/data/Run2018D/EGamma/NANOAOD/Nano14Dec2018_ver2-v1/40000/21146E44-5228-8542-91E6-272221444726.root',
       '/store/data/Run2018D/EGamma/NANOAOD/Nano14Dec2018_ver2-v1/40000/222451D5-4987-D742-BA40-29F527BDCA84.root',
       '/store/data/Run2018D/EGamma/NANOAOD/Nano14Dec2018_ver2-v1/40000/228AA5F6-4322-6546-BD7E-E06DF311EE4A.root',
       '/store/data/Run2018D/EGamma/NANOAOD/Nano14Dec2018_ver2-v1/40000/2307C0A5-9BBB-7C43-A36D-531D5BFF22A4.root',
       '/store/data/Run2018D/EGamma/NANOAOD/Nano14Dec2018_ver2-v1/40000/23785B30-0D8F-4E46-9C4B-7102CD0B5F7E.root',
       '/store/data/Run2018D/EGamma/NANOAOD/Nano14Dec2018_ver2-v1/40000/23A3F4E9-3EE0-8C4B-A5DF-FBE8BA6C640B.root',
       '/store/data/Run2018D/EGamma/NANOAOD/Nano14Dec2018_ver2-v1/40000/244E83F9-9583-DF4A-A242-4D1839B4091A.root',
       '/store/data/Run2018D/EGamma/NANOAOD/Nano14Dec2018_ver2-v1/40000/29D6742E-BBC0-2846-9AEB-6D500922223D.root',
       '/store/data/Run2018D/EGamma/NANOAOD/Nano14Dec2018_ver2-v1/40000/2C893819-9AF6-7F4E-B2A1-AA42597390D8.root',
       '/store/data/Run2018D/EGamma/NANOAOD/Nano14Dec2018_ver2-v1/40000/2D0A7049-9F09-4B4C-8D94-88426077196B.root',
       '/store/data/Run2018D/EGamma/NANOAOD/Nano14Dec2018_ver2-v1/40000/2E94EB22-B7F2-AF45-B9FF-CCB29B8C3DAB.root',
       '/store/data/Run2018D/EGamma/NANOAOD/Nano14Dec2018_ver2-v1/40000/30FC1FEC-4231-AB4D-8878-0B94CFC53746.root',
       '/store/data/Run2018D/EGamma/NANOAOD/Nano14Dec2018_ver2-v1/40000/32CAFC30-410C-8D42-8282-A108BB02B971.root',
       '/store/data/Run2018D/EGamma/NANOAOD/Nano14Dec2018_ver2-v1/40000/353940EC-4E5F-3C42-A3C5-C9AE23B68775.root',
       '/store/data/Run2018D/EGamma/NANOAOD/Nano14Dec2018_ver2-v1/40000/356576C9-F9DF-834C-8E3B-2C9FD70C55CD.root',
       '/store/data/Run2018D/EGamma/NANOAOD/Nano14Dec2018_ver2-v1/40000/38B97B63-2C17-E84F-B469-01C87A77BCF3.root',
       '/store/data/Run2018D/EGamma/NANOAOD/Nano14Dec2018_ver2-v1/40000/3996EF19-C733-A749-8C50-DAE37B9084F7.root',
       '/store/data/Run2018D/EGamma/NANOAOD/Nano14Dec2018_ver2-v1/40000/3EC9F622-BEA3-D149-86E5-A77E1C4C07C3.root',
       '/store/data/Run2018D/EGamma/NANOAOD/Nano14Dec2018_ver2-v1/40000/3FF9EDD4-3AEC-3141-BAAB-50CC65FE22B0.root',
       '/store/data/Run2018D/EGamma/NANOAOD/Nano14Dec2018_ver2-v1/40000/429C1951-4D5F-764C-9E3D-907AEE771EFD.root',
       '/store/data/Run2018D/EGamma/NANOAOD/Nano14Dec2018_ver2-v1/40000/45931725-9BF7-AF44-8CC9-5F89FD91A745.root',
       '/store/data/Run2018D/EGamma/NANOAOD/Nano14Dec2018_ver2-v1/40000/4A7CC43F-E7DB-6C4B-9A77-6B6E95B5973F.root',
       '/store/data/Run2018D/EGamma/NANOAOD/Nano14Dec2018_ver2-v1/40000/4B62C188-B06F-474E-B93E-CE180F818D82.root',
       '/store/data/Run2018D/EGamma/NANOAOD/Nano14Dec2018_ver2-v1/40000/50F3089B-42C8-1D40-9CAE-B7CEF6CEEF22.root',
       '/store/data/Run2018D/EGamma/NANOAOD/Nano14Dec2018_ver2-v1/40000/5167CAA9-DF8F-FF45-92DC-6F1FDA6BC32A.root',
       '/store/data/Run2018D/EGamma/NANOAOD/Nano14Dec2018_ver2-v1/40000/52691A2F-933D-2641-BA92-5D125C43FAF2.root',
       '/store/data/Run2018D/EGamma/NANOAOD/Nano14Dec2018_ver2-v1/40000/53CA87E2-7DED-3043-A15D-FC25CFBAFC11.root',
       '/store/data/Run2018D/EGamma/NANOAOD/Nano14Dec2018_ver2-v1/40000/5695D4FA-BF2E-824F-A840-CD5587D262A5.root',
       '/store/data/Run2018D/EGamma/NANOAOD/Nano14Dec2018_ver2-v1/40000/57C0AAB6-DB4D-4F4F-993F-9FF459BA9A36.root',
       '/store/data/Run2018D/EGamma/NANOAOD/Nano14Dec2018_ver2-v1/40000/58B98311-3AEA-0240-B9FF-2D6CB4EAB0C7.root',
       '/store/data/Run2018D/EGamma/NANOAOD/Nano14Dec2018_ver2-v1/40000/59237B48-7DBC-8044-AC81-340C61AF5BAE.root',
       '/store/data/Run2018D/EGamma/NANOAOD/Nano14Dec2018_ver2-v1/40000/5BA313E9-80CB-C54C-A077-6363ED8135E9.root',
       '/store/data/Run2018D/EGamma/NANOAOD/Nano14Dec2018_ver2-v1/40000/6480E357-DAA0-8845-A035-095952BB2EF6.root',
       '/store/data/Run2018D/EGamma/NANOAOD/Nano14Dec2018_ver2-v1/40000/66230BBE-03EC-534B-A199-1C897AD5C40A.root',
       '/store/data/Run2018D/EGamma/NANOAOD/Nano14Dec2018_ver2-v1/40000/66E55D73-CE70-5B42-9D30-F35BE34CD6EB.root',
       '/store/data/Run2018D/EGamma/NANOAOD/Nano14Dec2018_ver2-v1/40000/6701FE6F-F771-3944-841F-BF20FD874B00.root',
       '/store/data/Run2018D/EGamma/NANOAOD/Nano14Dec2018_ver2-v1/40000/67AC7BDC-0D80-AE43-BA3C-41B9FD874497.root',
       '/store/data/Run2018D/EGamma/NANOAOD/Nano14Dec2018_ver2-v1/40000/686DB80A-4505-7943-B279-353B57DFC308.root',
       '/store/data/Run2018D/EGamma/NANOAOD/Nano14Dec2018_ver2-v1/40000/6892B67A-E5BB-3C43-9B09-AE304EE5F236.root',
       '/store/data/Run2018D/EGamma/NANOAOD/Nano14Dec2018_ver2-v1/40000/6B5548FB-71EB-5741-A54B-43A020FA45AA.root',
       '/store/data/Run2018D/EGamma/NANOAOD/Nano14Dec2018_ver2-v1/40000/6B968E7C-FDE1-3A4B-8525-EB0CAC16B3A4.root',
       '/store/data/Run2018D/EGamma/NANOAOD/Nano14Dec2018_ver2-v1/40000/6EE26994-6271-5945-9484-3B0E6BD19301.root',
       '/store/data/Run2018D/EGamma/NANOAOD/Nano14Dec2018_ver2-v1/40000/72479A5B-B889-DB49-9A77-E92EA4053C1B.root',
       '/store/data/Run2018D/EGamma/NANOAOD/Nano14Dec2018_ver2-v1/40000/7283EB08-E221-E948-9A73-11CC422FD973.root',
       '/store/data/Run2018D/EGamma/NANOAOD/Nano14Dec2018_ver2-v1/40000/73199CC5-37EB-E242-B9D1-0BA8EE7BBE01.root',
       '/store/data/Run2018D/EGamma/NANOAOD/Nano14Dec2018_ver2-v1/40000/76ACB40B-31F2-0C43-AED3-9E9FF37B4A09.root',
       '/store/data/Run2018D/EGamma/NANOAOD/Nano14Dec2018_ver2-v1/40000/7A0C9431-7671-A941-B777-1024DC03F2CD.root',
       '/store/data/Run2018D/EGamma/NANOAOD/Nano14Dec2018_ver2-v1/40000/7D5B200C-3230-E64F-B6AA-3BC129FFD43F.root',
       '/store/data/Run2018D/EGamma/NANOAOD/Nano14Dec2018_ver2-v1/40000/7F9D4339-8B85-C84D-9881-9E8011183FCC.root',
       '/store/data/Run2018D/EGamma/NANOAOD/Nano14Dec2018_ver2-v1/40000/83118664-FED6-0242-B275-4622102269F5.root',
       '/store/data/Run2018D/EGamma/NANOAOD/Nano14Dec2018_ver2-v1/40000/847D8F8A-BE61-8D4B-854A-7DFEF1798038.root',
       '/store/data/Run2018D/EGamma/NANOAOD/Nano14Dec2018_ver2-v1/40000/9060DC3B-74E1-AB45-ADB3-DE3BF54430F8.root',
       '/store/data/Run2018D/EGamma/NANOAOD/Nano14Dec2018_ver2-v1/40000/94C7C5B8-643E-FD4A-B015-C53245C56FC3.root',
       '/store/data/Run2018D/EGamma/NANOAOD/Nano14Dec2018_ver2-v1/40000/965D143D-F072-3546-8984-F236DD50E1EC.root',
       '/store/data/Run2018D/EGamma/NANOAOD/Nano14Dec2018_ver2-v1/40000/97FD5DF2-4497-2B4C-A650-19609EE0FDDA.root',
       '/store/data/Run2018D/EGamma/NANOAOD/Nano14Dec2018_ver2-v1/40000/996EB1D3-9DA9-5644-9F8D-6E03AA3B66FE.root',
       '/store/data/Run2018D/EGamma/NANOAOD/Nano14Dec2018_ver2-v1/40000/9BF6981F-2520-6C41-B032-693E7036D41D.root',
       '/store/data/Run2018D/EGamma/NANOAOD/Nano14Dec2018_ver2-v1/40000/9E334760-9DB8-BE43-84CC-CE84A10912E8.root',
       '/store/data/Run2018D/EGamma/NANOAOD/Nano14Dec2018_ver2-v1/40000/A0A93666-A960-AF45-8D48-DE23AE38DD64.root',
       '/store/data/Run2018D/EGamma/NANOAOD/Nano14Dec2018_ver2-v1/40000/A231FC6C-E2E0-5E4C-A73A-737A9A16E9EE.root',
       '/store/data/Run2018D/EGamma/NANOAOD/Nano14Dec2018_ver2-v1/40000/A39B1E04-28DE-9D4C-B5B6-47FDB0F682EE.root',
       '/store/data/Run2018D/EGamma/NANOAOD/Nano14Dec2018_ver2-v1/40000/A50B6F30-05EE-7441-8D71-C4EFE04D620A.root',
       '/store/data/Run2018D/EGamma/NANOAOD/Nano14Dec2018_ver2-v1/40000/A5D06632-8C12-7B4C-89B2-5AACA2270880.root',
       '/store/data/Run2018D/EGamma/NANOAOD/Nano14Dec2018_ver2-v1/40000/AB9781DA-855A-3146-A17E-97EC4F6C9F52.root',
       '/store/data/Run2018D/EGamma/NANOAOD/Nano14Dec2018_ver2-v1/40000/B2AB53FC-E772-394F-ADFC-5C3775513DE2.root',
       '/store/data/Run2018D/EGamma/NANOAOD/Nano14Dec2018_ver2-v1/40000/B40219E2-32DC-2D4F-9C9B-89EFC675C2E0.root',
       '/store/data/Run2018D/EGamma/NANOAOD/Nano14Dec2018_ver2-v1/40000/B4CF3FD7-6F3E-F044-A57E-39ED56A7A5C4.root',
       '/store/data/Run2018D/EGamma/NANOAOD/Nano14Dec2018_ver2-v1/40000/B7BD6FE0-185B-E640-8FDD-1D3A0A9E1A1D.root',
       '/store/data/Run2018D/EGamma/NANOAOD/Nano14Dec2018_ver2-v1/40000/C0EED7AA-0FB7-6A4C-BF61-B8DF82780598.root',
       '/store/data/Run2018D/EGamma/NANOAOD/Nano14Dec2018_ver2-v1/40000/C1E44B25-3BD2-B146-8F36-B454452AA346.root',
       '/store/data/Run2018D/EGamma/NANOAOD/Nano14Dec2018_ver2-v1/40000/C9196ED8-1CEC-954D-9AA4-BCA7BAA1A236.root',
       '/store/data/Run2018D/EGamma/NANOAOD/Nano14Dec2018_ver2-v1/40000/CC2215BD-02BF-F844-B083-8F8CB818A02D.root',
       '/store/data/Run2018D/EGamma/NANOAOD/Nano14Dec2018_ver2-v1/40000/CCFA4398-729B-A041-8E8F-8C24C63595C4.root',
       '/store/data/Run2018D/EGamma/NANOAOD/Nano14Dec2018_ver2-v1/40000/CEECD4E3-BB20-EA4F-B21B-E1A3DA5D705F.root',
       '/store/data/Run2018D/EGamma/NANOAOD/Nano14Dec2018_ver2-v1/40000/CF0EFEE7-A674-314B-B3FC-002FB79C2225.root',
       '/store/data/Run2018D/EGamma/NANOAOD/Nano14Dec2018_ver2-v1/40000/DE5CD594-1CD6-E542-8467-FCF7AFD88FF0.root',
       '/store/data/Run2018D/EGamma/NANOAOD/Nano14Dec2018_ver2-v1/40000/DE6CD7DC-A465-BD4E-B2FA-C28EADBDEC5E.root',
       '/store/data/Run2018D/EGamma/NANOAOD/Nano14Dec2018_ver2-v1/40000/DEFCED51-0D98-1445-8471-E6C9FC9217DC.root',
       '/store/data/Run2018D/EGamma/NANOAOD/Nano14Dec2018_ver2-v1/40000/E395D28A-473C-C64C-B3F2-69C0E537B1E3.root',
       '/store/data/Run2018D/EGamma/NANOAOD/Nano14Dec2018_ver2-v1/40000/E3AC8A5F-400D-234E-949B-E8C8C63054F5.root',
       '/store/data/Run2018D/EGamma/NANOAOD/Nano14Dec2018_ver2-v1/40000/E4DF3649-B5B6-9C4C-A8E0-214446F0C634.root',
       '/store/data/Run2018D/EGamma/NANOAOD/Nano14Dec2018_ver2-v1/40000/E827F8D6-493D-1B42-A3C5-B30E1FFD90B0.root',
       '/store/data/Run2018D/EGamma/NANOAOD/Nano14Dec2018_ver2-v1/40000/E83FC85C-DB8A-794E-A43D-E4F7E6C6AD1D.root',
       '/store/data/Run2018D/EGamma/NANOAOD/Nano14Dec2018_ver2-v1/40000/EFA524DA-66BF-964A-B1E5-28B8BE311D2A.root',
       '/store/data/Run2018D/EGamma/NANOAOD/Nano14Dec2018_ver2-v1/40000/EFBC74D1-EB8A-4946-B68B-4401F0706D72.root',
       '/store/data/Run2018D/EGamma/NANOAOD/Nano14Dec2018_ver2-v1/40000/F0B1AEAB-47D8-E04A-9F84-26D9124B161C.root',
       '/store/data/Run2018D/EGamma/NANOAOD/Nano14Dec2018_ver2-v1/40000/F23995B3-CC8A-6B41-BBEA-D14C3D99A00B.root',
       '/store/data/Run2018D/EGamma/NANOAOD/Nano14Dec2018_ver2-v1/40000/F380CE26-17DE-2646-866B-675BB9EBF1C7.root',
       '/store/data/Run2018D/EGamma/NANOAOD/Nano14Dec2018_ver2-v1/40000/F3E7D28A-DDB8-AB41-8D9D-AAF6FB3BF8F0.root',
       '/store/data/Run2018D/EGamma/NANOAOD/Nano14Dec2018_ver2-v1/40000/F42456E1-CBFD-1249-9578-4FC1D8D9D4DF.root',
       '/store/data/Run2018D/EGamma/NANOAOD/Nano14Dec2018_ver2-v1/40000/F51C7A87-E004-524A-AFFB-BAE0BC99760C.root',
       '/store/data/Run2018D/EGamma/NANOAOD/Nano14Dec2018_ver2-v1/40000/F6411B8C-BC32-4640-AF93-3419313AA92A.root',
       '/store/data/Run2018D/EGamma/NANOAOD/Nano14Dec2018_ver2-v1/40000/F83756C6-C7D8-7B44-8381-8B0E6268D2B1.root',
       '/store/data/Run2018D/EGamma/NANOAOD/Nano14Dec2018_ver2-v1/40000/FB2DAF36-254D-3E4B-B6B9-F56EFF66A173.root',
       '/store/data/Run2018D/EGamma/NANOAOD/Nano14Dec2018_ver2-v1/40000/FC924B52-57B2-A94A-9913-26C3202AE9BC.root',
       '/store/data/Run2018D/EGamma/NANOAOD/Nano14Dec2018_ver2-v1/40000/FCF6EB41-7029-E545-B243-D0C3F6C96874.root',
       '/store/data/Run2018D/EGamma/NANOAOD/Nano14Dec2018_ver2-v1/80000/06FA5E4E-6396-0648-80C2-C3C4DE60C72C.root',
       '/store/data/Run2018D/EGamma/NANOAOD/Nano14Dec2018_ver2-v1/80000/0D10D54B-18F4-B446-87B2-3B4091F3CBDB.root',
       '/store/data/Run2018D/EGamma/NANOAOD/Nano14Dec2018_ver2-v1/80000/19229DEF-19BA-C14C-95A3-4D019EF399FB.root',
       '/store/data/Run2018D/EGamma/NANOAOD/Nano14Dec2018_ver2-v1/80000/1DD25F8A-9680-414D-9568-5228723B58F8.root',
       '/store/data/Run2018D/EGamma/NANOAOD/Nano14Dec2018_ver2-v1/80000/291E68DF-8AC4-F14C-8882-B3DB478E78DD.root',
       '/store/data/Run2018D/EGamma/NANOAOD/Nano14Dec2018_ver2-v1/80000/2A2A5EC0-BD59-7448-B5C8-0018984441C0.root',
       '/store/data/Run2018D/EGamma/NANOAOD/Nano14Dec2018_ver2-v1/80000/2BF31101-CD3C-8642-9D4E-1F5664A40483.root',
       '/store/data/Run2018D/EGamma/NANOAOD/Nano14Dec2018_ver2-v1/80000/3B2E9235-7487-CA41-A6F1-CEDC5BA5FD09.root',
       '/store/data/Run2018D/EGamma/NANOAOD/Nano14Dec2018_ver2-v1/80000/485BC05E-8516-114A-AE10-A6E6D251E78A.root',
       '/store/data/Run2018D/EGamma/NANOAOD/Nano14Dec2018_ver2-v1/80000/58201783-3E35-2C47-A66E-FD19FDDF897D.root',
       '/store/data/Run2018D/EGamma/NANOAOD/Nano14Dec2018_ver2-v1/80000/61B6D547-6FC7-064D-A53E-60AD8E296801.root',
       '/store/data/Run2018D/EGamma/NANOAOD/Nano14Dec2018_ver2-v1/80000/63874000-9D10-394A-95AD-6C69D04247FF.root',
       '/store/data/Run2018D/EGamma/NANOAOD/Nano14Dec2018_ver2-v1/80000/73F35101-AB86-234A-8F52-465A9430E4A4.root',
       '/store/data/Run2018D/EGamma/NANOAOD/Nano14Dec2018_ver2-v1/80000/7D1985FB-4CB8-3D43-807C-D8E56C98FEDF.root',
       '/store/data/Run2018D/EGamma/NANOAOD/Nano14Dec2018_ver2-v1/80000/7EC45F56-4E30-E443-B700-D98B98291706.root',
       '/store/data/Run2018D/EGamma/NANOAOD/Nano14Dec2018_ver2-v1/80000/82649709-FAD7-4B4E-A153-697D8ED4522C.root',
       '/store/data/Run2018D/EGamma/NANOAOD/Nano14Dec2018_ver2-v1/80000/90B9F989-B312-DB43-99C0-781833153264.root',
       '/store/data/Run2018D/EGamma/NANOAOD/Nano14Dec2018_ver2-v1/80000/972C08DB-7FD3-A749-8F95-7DF7FEA823CF.root',
       '/store/data/Run2018D/EGamma/NANOAOD/Nano14Dec2018_ver2-v1/80000/AD63FD40-D6A7-9141-9DDD-5FEF7E5E3911.root',
       '/store/data/Run2018D/EGamma/NANOAOD/Nano14Dec2018_ver2-v1/80000/B109005B-88B2-3349-849A-E0EB04A9BF8B.root',
       '/store/data/Run2018D/EGamma/NANOAOD/Nano14Dec2018_ver2-v1/80000/B414F87B-9C95-0D4B-9723-B2BC4E86CE17.root',
       '/store/data/Run2018D/EGamma/NANOAOD/Nano14Dec2018_ver2-v1/80000/C00B18FE-8721-EF49-97FD-EEE178FE4443.root',
       '/store/data/Run2018D/EGamma/NANOAOD/Nano14Dec2018_ver2-v1/80000/C44CF7CA-6622-A941-BBEC-9654DCD23872.root',
       '/store/data/Run2018D/EGamma/NANOAOD/Nano14Dec2018_ver2-v1/80000/DD5759C9-CE19-4048-8665-6FB2000283A0.root',
] )
readFiles.extend( [
       '/store/data/Run2018D/EGamma/NANOAOD/Nano14Dec2018_ver2-v1/80000/E21B8996-9319-9243-99B2-ED95256C8779.root',
       '/store/data/Run2018D/EGamma/NANOAOD/Nano14Dec2018_ver2-v1/80000/E403F96C-3903-214E-A67C-EE677CA1AFBF.root',
       '/store/data/Run2018D/EGamma/NANOAOD/Nano14Dec2018_ver2-v1/80000/F04CA384-918C-6A40-8515-92AB78B2C2A6.root',
       '/store/data/Run2018D/EGamma/NANOAOD/Nano14Dec2018_ver2-v1/80000/FABA655D-1593-4E4E-8393-10B9A77FB888.root',
] )