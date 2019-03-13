import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/data/Run2018A/JetHT/NANOAOD/Nano14Dec2018-v1/280000/07D8ECD6-17CC-4F41-95AE-1FB9005F873B.root',
       '/store/data/Run2018A/JetHT/NANOAOD/Nano14Dec2018-v1/280000/0D574A45-F250-BD43-86FC-199A66CEEAEF.root',
       '/store/data/Run2018A/JetHT/NANOAOD/Nano14Dec2018-v1/280000/0E328062-9176-D447-9EC3-10A475DF1F27.root',
       '/store/data/Run2018A/JetHT/NANOAOD/Nano14Dec2018-v1/280000/1012DF8F-8A4D-774A-AF03-F45823B77C8B.root',
       '/store/data/Run2018A/JetHT/NANOAOD/Nano14Dec2018-v1/280000/102D3F56-AF72-9146-AA8F-B8E722226E72.root',
       '/store/data/Run2018A/JetHT/NANOAOD/Nano14Dec2018-v1/280000/133CA559-8839-3540-9316-6546CF3A6CF9.root',
       '/store/data/Run2018A/JetHT/NANOAOD/Nano14Dec2018-v1/280000/1351F357-2252-AC42-A28B-1A4C26905DCF.root',
       '/store/data/Run2018A/JetHT/NANOAOD/Nano14Dec2018-v1/280000/172AEE5C-CF0D-154E-9F8E-581493C915AC.root',
       '/store/data/Run2018A/JetHT/NANOAOD/Nano14Dec2018-v1/280000/1ABD618B-D743-6640-8840-833CC4EFC476.root',
       '/store/data/Run2018A/JetHT/NANOAOD/Nano14Dec2018-v1/280000/1AE495C2-DA55-F54F-8D2D-2DFD6BA7D846.root',
       '/store/data/Run2018A/JetHT/NANOAOD/Nano14Dec2018-v1/280000/1BE923CD-12F4-E94B-BE1B-AA94BB0EA08A.root',
       '/store/data/Run2018A/JetHT/NANOAOD/Nano14Dec2018-v1/280000/1C78C8B7-F063-DC4B-9710-FDB8418EF859.root',
       '/store/data/Run2018A/JetHT/NANOAOD/Nano14Dec2018-v1/280000/1F65B979-B3B3-4C4A-B0DA-1E155050D876.root',
       '/store/data/Run2018A/JetHT/NANOAOD/Nano14Dec2018-v1/280000/1F915985-81CA-C947-BC31-D4790E13541B.root',
       '/store/data/Run2018A/JetHT/NANOAOD/Nano14Dec2018-v1/280000/21A6A076-99C9-2F45-A5B4-E6FCDB879A0C.root',
       '/store/data/Run2018A/JetHT/NANOAOD/Nano14Dec2018-v1/280000/2BF9310F-1EF7-6B48-9670-3E1C28CE476C.root',
       '/store/data/Run2018A/JetHT/NANOAOD/Nano14Dec2018-v1/280000/2FEA0C86-7EEB-E34E-9FA8-16BDF04361DC.root',
       '/store/data/Run2018A/JetHT/NANOAOD/Nano14Dec2018-v1/280000/334E610A-9264-464F-89B5-0CE077EBF9F4.root',
       '/store/data/Run2018A/JetHT/NANOAOD/Nano14Dec2018-v1/280000/36050057-D47B-4F41-B3CF-3FB9198DC82C.root',
       '/store/data/Run2018A/JetHT/NANOAOD/Nano14Dec2018-v1/280000/3755E004-E6B5-1C4D-9096-EC86528E5999.root',
       '/store/data/Run2018A/JetHT/NANOAOD/Nano14Dec2018-v1/280000/384F1B39-1D8B-574F-9B4D-1913FA55CCA4.root',
       '/store/data/Run2018A/JetHT/NANOAOD/Nano14Dec2018-v1/280000/39BAF1EA-1E1C-7546-BE2A-F7FEAA9A410F.root',
       '/store/data/Run2018A/JetHT/NANOAOD/Nano14Dec2018-v1/280000/3B1AACF4-D153-1140-A8EB-B173829C9C9A.root',
       '/store/data/Run2018A/JetHT/NANOAOD/Nano14Dec2018-v1/280000/425BD7D0-E225-5544-AAB7-0623D020E304.root',
       '/store/data/Run2018A/JetHT/NANOAOD/Nano14Dec2018-v1/280000/451CA100-8A98-AC46-83DC-0E7A7A2F4390.root',
       '/store/data/Run2018A/JetHT/NANOAOD/Nano14Dec2018-v1/280000/470E5F2E-4E81-B047-971A-6C2601B5DF2B.root',
       '/store/data/Run2018A/JetHT/NANOAOD/Nano14Dec2018-v1/280000/48A19F08-2B37-3E4F-BDC3-99066DD4C152.root',
       '/store/data/Run2018A/JetHT/NANOAOD/Nano14Dec2018-v1/280000/49089CC1-C052-1444-9233-A667B9744CFF.root',
       '/store/data/Run2018A/JetHT/NANOAOD/Nano14Dec2018-v1/280000/4AFB1A71-7E68-3C46-AAA9-F14A5BED3D85.root',
       '/store/data/Run2018A/JetHT/NANOAOD/Nano14Dec2018-v1/280000/4B6FD6C3-2ECE-4849-BD17-2089CAD2DAE5.root',
       '/store/data/Run2018A/JetHT/NANOAOD/Nano14Dec2018-v1/280000/4EDC829F-684A-D342-A137-5C2F0BBE3791.root',
       '/store/data/Run2018A/JetHT/NANOAOD/Nano14Dec2018-v1/280000/51BB0E9C-DED5-E542-B5CD-A9ABBEC3DF97.root',
       '/store/data/Run2018A/JetHT/NANOAOD/Nano14Dec2018-v1/280000/543A891A-2DC0-7C4C-8CAE-1B3ACC048C88.root',
       '/store/data/Run2018A/JetHT/NANOAOD/Nano14Dec2018-v1/280000/56444375-71D4-ED4A-8A9A-0A6A03C3D27A.root',
       '/store/data/Run2018A/JetHT/NANOAOD/Nano14Dec2018-v1/280000/5A06EBB6-556B-4F40-AA0B-3365FA8C9F6D.root',
       '/store/data/Run2018A/JetHT/NANOAOD/Nano14Dec2018-v1/280000/65CB14CD-12DD-9243-9928-33A3276B829C.root',
       '/store/data/Run2018A/JetHT/NANOAOD/Nano14Dec2018-v1/280000/67CA3F0D-0DB4-254A-B326-D7EEF54DDCF1.root',
       '/store/data/Run2018A/JetHT/NANOAOD/Nano14Dec2018-v1/280000/68BE960F-B5FF-C14F-AB70-FD6D03BF420E.root',
       '/store/data/Run2018A/JetHT/NANOAOD/Nano14Dec2018-v1/280000/6D9964ED-541F-7345-8F37-41A03C02BB84.root',
       '/store/data/Run2018A/JetHT/NANOAOD/Nano14Dec2018-v1/280000/710E6EE8-CD5F-7247-8FEF-C1A43E461571.root',
       '/store/data/Run2018A/JetHT/NANOAOD/Nano14Dec2018-v1/280000/7241BA69-3327-EF44-9295-B2B29CACD09E.root',
       '/store/data/Run2018A/JetHT/NANOAOD/Nano14Dec2018-v1/280000/745C1C67-0AA4-234D-A911-CF695645FB43.root',
       '/store/data/Run2018A/JetHT/NANOAOD/Nano14Dec2018-v1/280000/8B51FBDE-9E0F-1D43-960F-7AEE1CDFF6B5.root',
       '/store/data/Run2018A/JetHT/NANOAOD/Nano14Dec2018-v1/280000/98092205-6603-C44D-839B-8281387BE470.root',
       '/store/data/Run2018A/JetHT/NANOAOD/Nano14Dec2018-v1/280000/A1BDED36-C1E6-8448-885A-EBC383E10E28.root',
       '/store/data/Run2018A/JetHT/NANOAOD/Nano14Dec2018-v1/280000/A75EDC9D-E524-184A-8EA9-A42F1DBC697D.root',
       '/store/data/Run2018A/JetHT/NANOAOD/Nano14Dec2018-v1/280000/ADB58A7F-D257-D444-8BE4-D6B58302AC7D.root',
       '/store/data/Run2018A/JetHT/NANOAOD/Nano14Dec2018-v1/280000/AECB3874-8843-EF46-BE14-257359BB679B.root',
       '/store/data/Run2018A/JetHT/NANOAOD/Nano14Dec2018-v1/280000/B1293005-B6C5-C84E-BD90-CB048B976DCC.root',
       '/store/data/Run2018A/JetHT/NANOAOD/Nano14Dec2018-v1/280000/B3B96F9D-2146-044C-9C0D-BA5941F6629F.root',
       '/store/data/Run2018A/JetHT/NANOAOD/Nano14Dec2018-v1/280000/B54BF814-937B-534C-B14F-B24FEC9FD22C.root',
       '/store/data/Run2018A/JetHT/NANOAOD/Nano14Dec2018-v1/280000/B7A49AD3-6357-854F-B441-3EAD6A3AD5B1.root',
       '/store/data/Run2018A/JetHT/NANOAOD/Nano14Dec2018-v1/280000/BC176EC7-B4BF-5446-9F74-7A9D2C4B6B32.root',
       '/store/data/Run2018A/JetHT/NANOAOD/Nano14Dec2018-v1/280000/C085FE43-0CAC-9046-B1AF-2E4171959D39.root',
       '/store/data/Run2018A/JetHT/NANOAOD/Nano14Dec2018-v1/280000/C19D91B5-FEC7-6A49-A3DB-755B0EE2E5A7.root',
       '/store/data/Run2018A/JetHT/NANOAOD/Nano14Dec2018-v1/280000/C47F5E38-8828-5245-BF5A-F64D2164BF05.root',
       '/store/data/Run2018A/JetHT/NANOAOD/Nano14Dec2018-v1/280000/C544168F-622C-0448-926E-05FD5748C794.root',
       '/store/data/Run2018A/JetHT/NANOAOD/Nano14Dec2018-v1/280000/CA911FBC-1DB9-D147-A6C2-26EA89BC0C85.root',
       '/store/data/Run2018A/JetHT/NANOAOD/Nano14Dec2018-v1/280000/CF4F9131-F29B-664B-9150-0D4EADF21271.root',
       '/store/data/Run2018A/JetHT/NANOAOD/Nano14Dec2018-v1/280000/D1E76AE6-A0A7-D44B-8834-CB47CD250997.root',
       '/store/data/Run2018A/JetHT/NANOAOD/Nano14Dec2018-v1/280000/DB825976-87DE-524F-B26B-CCF866D83004.root',
       '/store/data/Run2018A/JetHT/NANOAOD/Nano14Dec2018-v1/280000/DC219429-9771-FD42-BA42-1AC3390FE3ED.root',
       '/store/data/Run2018A/JetHT/NANOAOD/Nano14Dec2018-v1/280000/DEE9DCDD-F5E0-F340-BCEF-583E18158400.root',
       '/store/data/Run2018A/JetHT/NANOAOD/Nano14Dec2018-v1/280000/E133466B-EBCF-734D-89D8-EFD2C4DE7872.root',
       '/store/data/Run2018A/JetHT/NANOAOD/Nano14Dec2018-v1/280000/E19A597A-9739-9845-8372-5C3DBD965F05.root',
       '/store/data/Run2018A/JetHT/NANOAOD/Nano14Dec2018-v1/280000/E4587545-52A3-E841-B9B5-6FFFD55F640F.root',
       '/store/data/Run2018A/JetHT/NANOAOD/Nano14Dec2018-v1/280000/E4EC1203-F147-4E4F-951B-6D97167CC1BA.root',
       '/store/data/Run2018A/JetHT/NANOAOD/Nano14Dec2018-v1/280000/E9946A21-C934-9848-B965-D2AF6593774B.root',
       '/store/data/Run2018A/JetHT/NANOAOD/Nano14Dec2018-v1/280000/EAA830E0-7235-E34A-8BFF-1A46D45FD896.root',
       '/store/data/Run2018A/JetHT/NANOAOD/Nano14Dec2018-v1/280000/EE901D32-EAAF-1A46-B73E-761B856CE34F.root',
       '/store/data/Run2018A/JetHT/NANOAOD/Nano14Dec2018-v1/280000/F0A132AC-C29F-BF44-B837-538FB25D6135.root',
       '/store/data/Run2018A/JetHT/NANOAOD/Nano14Dec2018-v1/280000/FCC473BB-7E35-8949-B242-C3CCA0E88E01.root',
       '/store/data/Run2018A/JetHT/NANOAOD/Nano14Dec2018-v1/280000/FDF40B56-308C-664B-A9C0-4151C293831C.root',
       '/store/data/Run2018A/JetHT/NANOAOD/Nano14Dec2018-v1/40000/01DB45A1-5276-9A42-82CE-55E04F2CA792.root',
       '/store/data/Run2018A/JetHT/NANOAOD/Nano14Dec2018-v1/40000/0AC23D83-030C-9049-AA1C-C8193AE4C178.root',
       '/store/data/Run2018A/JetHT/NANOAOD/Nano14Dec2018-v1/40000/14139D26-212F-524D-A3BF-0A440E97E8D0.root',
       '/store/data/Run2018A/JetHT/NANOAOD/Nano14Dec2018-v1/40000/1822A599-BD4F-6C44-9192-DF5706893A84.root',
       '/store/data/Run2018A/JetHT/NANOAOD/Nano14Dec2018-v1/40000/1847B1B3-121E-7049-88B8-DAB9C2C2F32B.root',
       '/store/data/Run2018A/JetHT/NANOAOD/Nano14Dec2018-v1/40000/20E4EF05-3F92-784F-8C8C-161DBC19F467.root',
       '/store/data/Run2018A/JetHT/NANOAOD/Nano14Dec2018-v1/40000/2310DDBB-AEA7-4C4F-857C-7E48B22D6A40.root',
       '/store/data/Run2018A/JetHT/NANOAOD/Nano14Dec2018-v1/40000/23420BA0-8156-C74D-8231-8504C8E62174.root',
       '/store/data/Run2018A/JetHT/NANOAOD/Nano14Dec2018-v1/40000/27073DB9-970C-464E-8FC3-A47418DEDBB2.root',
       '/store/data/Run2018A/JetHT/NANOAOD/Nano14Dec2018-v1/40000/287C4846-ECAD-9D4F-BE96-11AD6775974C.root',
       '/store/data/Run2018A/JetHT/NANOAOD/Nano14Dec2018-v1/40000/28E3593D-7CA0-D44D-9ACC-5DDF0453BCE7.root',
       '/store/data/Run2018A/JetHT/NANOAOD/Nano14Dec2018-v1/40000/2912EA1C-25D8-A943-BACD-DCC63B1DE4CE.root',
       '/store/data/Run2018A/JetHT/NANOAOD/Nano14Dec2018-v1/40000/2971FB69-DF25-A247-BEE9-C6F1D1A9212B.root',
       '/store/data/Run2018A/JetHT/NANOAOD/Nano14Dec2018-v1/40000/2F6B0ADD-1A3B-D84F-9E87-DE47366973AB.root',
       '/store/data/Run2018A/JetHT/NANOAOD/Nano14Dec2018-v1/40000/340D003B-5C70-994F-83A0-94DD10CBF1D5.root',
       '/store/data/Run2018A/JetHT/NANOAOD/Nano14Dec2018-v1/40000/3DC9F361-1C5C-6047-B292-5C9236E71C9B.root',
       '/store/data/Run2018A/JetHT/NANOAOD/Nano14Dec2018-v1/40000/428E007A-1621-D542-8238-0A59F8B7478E.root',
       '/store/data/Run2018A/JetHT/NANOAOD/Nano14Dec2018-v1/40000/454FD28A-CCAE-7E4C-9E9F-63D989D52C4F.root',
       '/store/data/Run2018A/JetHT/NANOAOD/Nano14Dec2018-v1/40000/4D98303D-0FC6-0447-A095-00053FC0FE4D.root',
       '/store/data/Run2018A/JetHT/NANOAOD/Nano14Dec2018-v1/40000/505FBBB2-DF30-4842-96FE-1FF83AB8E7D4.root',
       '/store/data/Run2018A/JetHT/NANOAOD/Nano14Dec2018-v1/40000/513669B0-5BB8-5241-B058-67AF05756007.root',
       '/store/data/Run2018A/JetHT/NANOAOD/Nano14Dec2018-v1/40000/51C88102-AE1E-1B48-929F-689C2508D658.root',
       '/store/data/Run2018A/JetHT/NANOAOD/Nano14Dec2018-v1/40000/51E8FDE7-BE59-2C4E-A96C-42FBA122A839.root',
       '/store/data/Run2018A/JetHT/NANOAOD/Nano14Dec2018-v1/40000/52B15884-3F23-CE47-81D9-45C43154E421.root',
       '/store/data/Run2018A/JetHT/NANOAOD/Nano14Dec2018-v1/40000/55F34DDD-1DD1-D641-BFF0-1F35107C3813.root',
       '/store/data/Run2018A/JetHT/NANOAOD/Nano14Dec2018-v1/40000/57E041D4-8840-D049-91FB-08D9BDAB85A0.root',
       '/store/data/Run2018A/JetHT/NANOAOD/Nano14Dec2018-v1/40000/5BC29D6B-921D-5248-8FA0-6F328E081EAC.root',
       '/store/data/Run2018A/JetHT/NANOAOD/Nano14Dec2018-v1/40000/60D0D808-614E-254D-8DDB-1ED7B3C3BC58.root',
       '/store/data/Run2018A/JetHT/NANOAOD/Nano14Dec2018-v1/40000/6D628D6A-60A5-6D48-AD4A-5B7597958239.root',
       '/store/data/Run2018A/JetHT/NANOAOD/Nano14Dec2018-v1/40000/6DB78D31-8F6D-3E45-9B21-DC08867B0370.root',
       '/store/data/Run2018A/JetHT/NANOAOD/Nano14Dec2018-v1/40000/7027AC43-B91C-B84D-A2BB-717FFD47BFDA.root',
       '/store/data/Run2018A/JetHT/NANOAOD/Nano14Dec2018-v1/40000/788BE791-BAE1-244B-85EC-6CA4EC9C3152.root',
       '/store/data/Run2018A/JetHT/NANOAOD/Nano14Dec2018-v1/40000/7CF82423-3E6E-E44E-B7C1-50CC83BB0161.root',
       '/store/data/Run2018A/JetHT/NANOAOD/Nano14Dec2018-v1/40000/81712846-2BAC-364D-8630-C70345590394.root',
       '/store/data/Run2018A/JetHT/NANOAOD/Nano14Dec2018-v1/40000/822B236B-977A-A742-8414-0A47F42D6103.root',
       '/store/data/Run2018A/JetHT/NANOAOD/Nano14Dec2018-v1/40000/8565B247-6910-9943-8C0F-6D3BC9DBEC8A.root',
       '/store/data/Run2018A/JetHT/NANOAOD/Nano14Dec2018-v1/40000/86E34993-4DF9-E642-8B2B-F409CD0B7B97.root',
       '/store/data/Run2018A/JetHT/NANOAOD/Nano14Dec2018-v1/40000/876E6EDC-6F19-4F4C-A93F-9D911B9D6809.root',
       '/store/data/Run2018A/JetHT/NANOAOD/Nano14Dec2018-v1/40000/8A43087E-69E1-5D42-9E34-9569364DE85A.root',
       '/store/data/Run2018A/JetHT/NANOAOD/Nano14Dec2018-v1/40000/8C6FF68E-54BB-CE42-9986-62A7EB14D9E7.root',
       '/store/data/Run2018A/JetHT/NANOAOD/Nano14Dec2018-v1/40000/8C93B9FE-008B-134B-9D02-123E4DBEC8F6.root',
       '/store/data/Run2018A/JetHT/NANOAOD/Nano14Dec2018-v1/40000/90D308EC-CB84-1243-8444-E18DD106E3C6.root',
       '/store/data/Run2018A/JetHT/NANOAOD/Nano14Dec2018-v1/40000/9263B6CD-94BB-C247-AC31-2FA5AE705173.root',
       '/store/data/Run2018A/JetHT/NANOAOD/Nano14Dec2018-v1/40000/92AE6BCB-792E-5C41-B021-21AFABD9812B.root',
       '/store/data/Run2018A/JetHT/NANOAOD/Nano14Dec2018-v1/40000/99FE3E01-4CA9-6A44-B1C2-920FC6ABC273.root',
       '/store/data/Run2018A/JetHT/NANOAOD/Nano14Dec2018-v1/40000/9DFEDFC9-ED27-404A-830F-BBA6C934C916.root',
       '/store/data/Run2018A/JetHT/NANOAOD/Nano14Dec2018-v1/40000/9F1A8A38-DD2A-0F43-A955-BBCE965910A9.root',
       '/store/data/Run2018A/JetHT/NANOAOD/Nano14Dec2018-v1/40000/B14B5190-BE86-7E41-88B6-F8F85F2A1983.root',
       '/store/data/Run2018A/JetHT/NANOAOD/Nano14Dec2018-v1/40000/B7E7B216-73B3-AC42-A6AB-8621ABF125DC.root',
       '/store/data/Run2018A/JetHT/NANOAOD/Nano14Dec2018-v1/40000/BF8F149E-F732-D548-AF9B-B8F8E937DCC3.root',
       '/store/data/Run2018A/JetHT/NANOAOD/Nano14Dec2018-v1/40000/C0EB6758-AC20-FB4A-ABCE-08DFF83A3D39.root',
       '/store/data/Run2018A/JetHT/NANOAOD/Nano14Dec2018-v1/40000/C479CC17-22AE-0A44-8355-06E93509390E.root',
       '/store/data/Run2018A/JetHT/NANOAOD/Nano14Dec2018-v1/40000/CBF0993F-5617-BE43-A674-A327177781C5.root',
       '/store/data/Run2018A/JetHT/NANOAOD/Nano14Dec2018-v1/40000/D8D9077A-8424-DF4C-BB1E-C75EC12E5B3A.root',
       '/store/data/Run2018A/JetHT/NANOAOD/Nano14Dec2018-v1/40000/DCB3AAD7-50F1-CA4B-A1CE-DE81A7AD7388.root',
       '/store/data/Run2018A/JetHT/NANOAOD/Nano14Dec2018-v1/40000/F65ECD87-9E09-FE44-B70A-87F97EAE1DEC.root',
       '/store/data/Run2018A/JetHT/NANOAOD/Nano14Dec2018-v1/40000/F78CF1DE-B944-5F43-BC41-8C0CD73747E7.root',
       '/store/data/Run2018A/JetHT/NANOAOD/Nano14Dec2018-v1/40000/FB8F8DCD-4300-9548-B667-964AA87A7364.root',
       '/store/data/Run2018A/JetHT/NANOAOD/Nano14Dec2018-v1/40000/FE04956B-8CB9-A648-A254-861CD062BA37.root',
       '/store/data/Run2018A/JetHT/NANOAOD/Nano14Dec2018-v1/80000/80BEB9E8-1687-D041-B8A9-E8D79F63B9CA.root',
       '/store/data/Run2018A/JetHT/NANOAOD/Nano14Dec2018-v1/80000/953EB64A-684C-AC43-BBA7-15123FD24543.root',
       '/store/data/Run2018A/JetHT/NANOAOD/Nano14Dec2018-v1/80000/DE774CCF-78F1-C24E-AF66-ADB06B22AA2C.root',
] )