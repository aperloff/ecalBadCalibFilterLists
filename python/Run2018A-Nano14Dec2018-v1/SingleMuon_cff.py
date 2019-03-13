import FWCore.ParameterSet.Config as cms

maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
readFiles = cms.untracked.vstring()
secFiles = cms.untracked.vstring()
source = cms.Source ("PoolSource",fileNames = readFiles, secondaryFileNames = secFiles)
readFiles.extend( [
       '/store/data/Run2018A/SingleMuon/NANOAOD/Nano14Dec2018-v1/20000/00073125-11AF-1C4E-BFBD-36039C8B23C4.root',
       '/store/data/Run2018A/SingleMuon/NANOAOD/Nano14Dec2018-v1/20000/01E7AACD-80A3-3345-8A44-9EE320B56974.root',
       '/store/data/Run2018A/SingleMuon/NANOAOD/Nano14Dec2018-v1/20000/04E157E6-E557-A042-9CD4-5EA7D09B1B8D.root',
       '/store/data/Run2018A/SingleMuon/NANOAOD/Nano14Dec2018-v1/20000/06E81CBD-773D-1145-A9A0-202D7F0EEAAB.root',
       '/store/data/Run2018A/SingleMuon/NANOAOD/Nano14Dec2018-v1/20000/10828DC5-1E5D-7844-838D-6413EFEB78F0.root',
       '/store/data/Run2018A/SingleMuon/NANOAOD/Nano14Dec2018-v1/20000/13C91C64-FF3E-604E-AFCF-DC807DF37C63.root',
       '/store/data/Run2018A/SingleMuon/NANOAOD/Nano14Dec2018-v1/20000/13CFD648-9393-FA43-BE48-60CCBFA3C8E6.root',
       '/store/data/Run2018A/SingleMuon/NANOAOD/Nano14Dec2018-v1/20000/1402C65D-0B70-1340-84A5-3BEA695A4D36.root',
       '/store/data/Run2018A/SingleMuon/NANOAOD/Nano14Dec2018-v1/20000/17CF17FF-ACE6-A944-9021-0C0FC9F25F9B.root',
       '/store/data/Run2018A/SingleMuon/NANOAOD/Nano14Dec2018-v1/20000/1B6967DD-D30C-464E-B80C-86A1CFBF1B62.root',
       '/store/data/Run2018A/SingleMuon/NANOAOD/Nano14Dec2018-v1/20000/1C6DE460-4D1F-C54C-A158-E6AE9CB4D8E6.root',
       '/store/data/Run2018A/SingleMuon/NANOAOD/Nano14Dec2018-v1/20000/21A4ABD5-FFC4-0446-BB08-18666AF6E3B1.root',
       '/store/data/Run2018A/SingleMuon/NANOAOD/Nano14Dec2018-v1/20000/2ACDD14A-1169-9749-B071-21669AA0681F.root',
       '/store/data/Run2018A/SingleMuon/NANOAOD/Nano14Dec2018-v1/20000/2D4D4A5F-C706-384B-9D13-4D8726C4546F.root',
       '/store/data/Run2018A/SingleMuon/NANOAOD/Nano14Dec2018-v1/20000/2D62AA0B-F131-7540-B61C-8ABE6D33203E.root',
       '/store/data/Run2018A/SingleMuon/NANOAOD/Nano14Dec2018-v1/20000/2FCB875A-FAFA-414A-9CAF-4535CC29B269.root',
       '/store/data/Run2018A/SingleMuon/NANOAOD/Nano14Dec2018-v1/20000/308BB070-A759-B745-9543-1D1341604199.root',
       '/store/data/Run2018A/SingleMuon/NANOAOD/Nano14Dec2018-v1/20000/32BEDFC6-105D-DD4A-94A5-1F497E72E77C.root',
       '/store/data/Run2018A/SingleMuon/NANOAOD/Nano14Dec2018-v1/20000/349C69BD-C56C-D647-8709-3475C089E194.root',
       '/store/data/Run2018A/SingleMuon/NANOAOD/Nano14Dec2018-v1/20000/351CDB95-CD2F-F14F-83A0-BACF203B82BE.root',
       '/store/data/Run2018A/SingleMuon/NANOAOD/Nano14Dec2018-v1/20000/36EBFFBA-FA0B-9147-A6FF-A12E422BEC0A.root',
       '/store/data/Run2018A/SingleMuon/NANOAOD/Nano14Dec2018-v1/20000/3BCBF7D2-A69A-3B45-AEA4-1F2161951DAB.root',
       '/store/data/Run2018A/SingleMuon/NANOAOD/Nano14Dec2018-v1/20000/3EE9B1E8-82E6-FC40-ABD3-6BD9E57C9370.root',
       '/store/data/Run2018A/SingleMuon/NANOAOD/Nano14Dec2018-v1/20000/40E86747-FD44-9446-8F0D-E906C5815FD2.root',
       '/store/data/Run2018A/SingleMuon/NANOAOD/Nano14Dec2018-v1/20000/4321BA20-6535-D141-9707-C9CE0271B53D.root',
       '/store/data/Run2018A/SingleMuon/NANOAOD/Nano14Dec2018-v1/20000/4361535F-7145-AA4A-9E78-2113AE7F3BF7.root',
       '/store/data/Run2018A/SingleMuon/NANOAOD/Nano14Dec2018-v1/20000/44D03743-29BC-9C4B-B077-675121AB0CCD.root',
       '/store/data/Run2018A/SingleMuon/NANOAOD/Nano14Dec2018-v1/20000/4677660B-3A1E-004F-816B-71EC22A0BCA4.root',
       '/store/data/Run2018A/SingleMuon/NANOAOD/Nano14Dec2018-v1/20000/49F2978C-75EE-5041-BA6F-7465A91D7504.root',
       '/store/data/Run2018A/SingleMuon/NANOAOD/Nano14Dec2018-v1/20000/4A1F8EA3-6840-594E-883F-DE5B6012107C.root',
       '/store/data/Run2018A/SingleMuon/NANOAOD/Nano14Dec2018-v1/20000/53D71B16-5F04-2642-98FB-727DE7EC502E.root',
       '/store/data/Run2018A/SingleMuon/NANOAOD/Nano14Dec2018-v1/20000/5676AA45-6784-DD4C-A557-1D6CAEFA04DD.root',
       '/store/data/Run2018A/SingleMuon/NANOAOD/Nano14Dec2018-v1/20000/5AAA8656-5C61-614B-8016-EEB1DD6B6FF3.root',
       '/store/data/Run2018A/SingleMuon/NANOAOD/Nano14Dec2018-v1/20000/5C6DED23-FB09-7343-AA8F-155493A9C4EB.root',
       '/store/data/Run2018A/SingleMuon/NANOAOD/Nano14Dec2018-v1/20000/678F4033-832D-8343-B214-45E92906CBDB.root',
       '/store/data/Run2018A/SingleMuon/NANOAOD/Nano14Dec2018-v1/20000/71454F0B-AD19-C84F-8ACC-BE02E2CA1957.root',
       '/store/data/Run2018A/SingleMuon/NANOAOD/Nano14Dec2018-v1/20000/733FE704-7676-1C48-8B52-EEA08D61A0B1.root',
       '/store/data/Run2018A/SingleMuon/NANOAOD/Nano14Dec2018-v1/20000/7681E164-9445-F047-92DC-A2FA662297A1.root',
       '/store/data/Run2018A/SingleMuon/NANOAOD/Nano14Dec2018-v1/20000/7BDE63AE-C809-E74B-B2A3-035402D31645.root',
       '/store/data/Run2018A/SingleMuon/NANOAOD/Nano14Dec2018-v1/20000/7EC362EE-A22A-CD43-A1DB-8D19EA807464.root',
       '/store/data/Run2018A/SingleMuon/NANOAOD/Nano14Dec2018-v1/20000/8599B6C2-3E40-5745-B6B4-A14E2B14E493.root',
       '/store/data/Run2018A/SingleMuon/NANOAOD/Nano14Dec2018-v1/20000/8B288E34-9B64-4740-A632-3887749CF951.root',
       '/store/data/Run2018A/SingleMuon/NANOAOD/Nano14Dec2018-v1/20000/8EDC4257-0BF8-C447-BDA1-0CEC5C9CEBF9.root',
       '/store/data/Run2018A/SingleMuon/NANOAOD/Nano14Dec2018-v1/20000/90BD4759-5653-254D-9674-80A75219ECCB.root',
       '/store/data/Run2018A/SingleMuon/NANOAOD/Nano14Dec2018-v1/20000/962B5AE8-9D62-D049-827E-241C6449563E.root',
       '/store/data/Run2018A/SingleMuon/NANOAOD/Nano14Dec2018-v1/20000/9B02A949-BBE7-1546-9787-379A4837854A.root',
       '/store/data/Run2018A/SingleMuon/NANOAOD/Nano14Dec2018-v1/20000/A0A37770-B5EE-784D-862D-506A1E4DF590.root',
       '/store/data/Run2018A/SingleMuon/NANOAOD/Nano14Dec2018-v1/20000/A0FCABF5-E123-1C43-BC32-3D6B8D883CE4.root',
       '/store/data/Run2018A/SingleMuon/NANOAOD/Nano14Dec2018-v1/20000/A52297C1-C214-224A-B0C2-B4F7EBDA1D1A.root',
       '/store/data/Run2018A/SingleMuon/NANOAOD/Nano14Dec2018-v1/20000/A7B54FA4-0301-8F47-B197-2B4D64F20420.root',
       '/store/data/Run2018A/SingleMuon/NANOAOD/Nano14Dec2018-v1/20000/A88333E6-6D83-1E40-8047-458CEC301FAF.root',
       '/store/data/Run2018A/SingleMuon/NANOAOD/Nano14Dec2018-v1/20000/AF3F3371-C147-BF4C-B48E-F59D46786C3B.root',
       '/store/data/Run2018A/SingleMuon/NANOAOD/Nano14Dec2018-v1/20000/B044E20D-0986-A345-B2C1-64FE51E32FEC.root',
       '/store/data/Run2018A/SingleMuon/NANOAOD/Nano14Dec2018-v1/20000/B11EE02F-B8BA-DE4D-856A-FB457A6CB558.root',
       '/store/data/Run2018A/SingleMuon/NANOAOD/Nano14Dec2018-v1/20000/BA315F98-8502-8548-818F-9AE3DADA713F.root',
       '/store/data/Run2018A/SingleMuon/NANOAOD/Nano14Dec2018-v1/20000/BE732229-75CF-2846-982F-4BA5217AB2C6.root',
       '/store/data/Run2018A/SingleMuon/NANOAOD/Nano14Dec2018-v1/20000/C4D6673E-9BB3-5E4C-AD8F-04C15F62E673.root',
       '/store/data/Run2018A/SingleMuon/NANOAOD/Nano14Dec2018-v1/20000/C8D756FE-A06E-1245-8E42-2B64FAB703A2.root',
       '/store/data/Run2018A/SingleMuon/NANOAOD/Nano14Dec2018-v1/20000/CE214C4C-1B1C-F14B-B839-48BB67CC620C.root',
       '/store/data/Run2018A/SingleMuon/NANOAOD/Nano14Dec2018-v1/20000/CEB36FF6-F451-3741-8A73-CB81DCF570CC.root',
       '/store/data/Run2018A/SingleMuon/NANOAOD/Nano14Dec2018-v1/20000/D375C693-8F28-A446-98F3-A35823E45936.root',
       '/store/data/Run2018A/SingleMuon/NANOAOD/Nano14Dec2018-v1/20000/D3AC69CC-1B31-4C4D-A3CD-B275916C4047.root',
       '/store/data/Run2018A/SingleMuon/NANOAOD/Nano14Dec2018-v1/20000/D60F2796-9BDD-E249-A42D-5E085AD20577.root',
       '/store/data/Run2018A/SingleMuon/NANOAOD/Nano14Dec2018-v1/20000/D7672664-D4D7-534D-A915-1CF2167004BB.root',
       '/store/data/Run2018A/SingleMuon/NANOAOD/Nano14Dec2018-v1/20000/DAE09779-29F0-EB47-AC0C-295F4A04D765.root',
       '/store/data/Run2018A/SingleMuon/NANOAOD/Nano14Dec2018-v1/20000/DF19BD93-D9EF-694C-AB0C-DDCB30FBDCE6.root',
       '/store/data/Run2018A/SingleMuon/NANOAOD/Nano14Dec2018-v1/20000/E4DE9626-917C-1249-B0D4-D9913AD96784.root',
       '/store/data/Run2018A/SingleMuon/NANOAOD/Nano14Dec2018-v1/20000/EF86AAA4-1560-7640-9D56-530A4E6EE91A.root',
       '/store/data/Run2018A/SingleMuon/NANOAOD/Nano14Dec2018-v1/20000/F38E92F4-9E05-0948-B761-99EA7A9A738E.root',
       '/store/data/Run2018A/SingleMuon/NANOAOD/Nano14Dec2018-v1/40000/03F4BE42-2CF9-7B4D-A569-1FBE5130B554.root',
       '/store/data/Run2018A/SingleMuon/NANOAOD/Nano14Dec2018-v1/40000/07748FF2-672F-6845-A8A8-3BFB73D73685.root',
       '/store/data/Run2018A/SingleMuon/NANOAOD/Nano14Dec2018-v1/40000/0979A8B1-B655-B847-9819-291DFF7C7F23.root',
       '/store/data/Run2018A/SingleMuon/NANOAOD/Nano14Dec2018-v1/40000/0DD89AF7-6F55-D54A-8667-EC1536B658F0.root',
       '/store/data/Run2018A/SingleMuon/NANOAOD/Nano14Dec2018-v1/40000/0F56434F-DFC0-254A-820D-EF82232A97CD.root',
       '/store/data/Run2018A/SingleMuon/NANOAOD/Nano14Dec2018-v1/40000/17CE6A14-827B-5642-B6EC-D228D3F5BC57.root',
       '/store/data/Run2018A/SingleMuon/NANOAOD/Nano14Dec2018-v1/40000/1A17C2F2-55E5-614D-9083-F6983F065380.root',
       '/store/data/Run2018A/SingleMuon/NANOAOD/Nano14Dec2018-v1/40000/1B3DBB73-9E14-9E48-916E-EDC20904BD7E.root',
       '/store/data/Run2018A/SingleMuon/NANOAOD/Nano14Dec2018-v1/40000/1D158BC0-460D-4B46-ACB5-1AADA41424AC.root',
       '/store/data/Run2018A/SingleMuon/NANOAOD/Nano14Dec2018-v1/40000/21163FD4-311A-A548-BCC0-29CF9A4C346C.root',
       '/store/data/Run2018A/SingleMuon/NANOAOD/Nano14Dec2018-v1/40000/253A2B4D-4130-7447-87B1-41AF6BEB1DB5.root',
       '/store/data/Run2018A/SingleMuon/NANOAOD/Nano14Dec2018-v1/40000/29977716-54E1-DB4D-9597-8AC2E79C6B63.root',
       '/store/data/Run2018A/SingleMuon/NANOAOD/Nano14Dec2018-v1/40000/3B65F06A-8AA2-D747-AE79-93AF07F89836.root',
       '/store/data/Run2018A/SingleMuon/NANOAOD/Nano14Dec2018-v1/40000/3FC5B09D-28B3-DA45-938B-D902A030ACDC.root',
       '/store/data/Run2018A/SingleMuon/NANOAOD/Nano14Dec2018-v1/40000/45F033D2-BC10-524F-BDC7-7E3F2EBF7D2D.root',
       '/store/data/Run2018A/SingleMuon/NANOAOD/Nano14Dec2018-v1/40000/4800DB15-A0EC-B043-97F7-CFBA0187748E.root',
       '/store/data/Run2018A/SingleMuon/NANOAOD/Nano14Dec2018-v1/40000/4B163A82-CD1A-3345-99DE-0FCA5A5D6056.root',
       '/store/data/Run2018A/SingleMuon/NANOAOD/Nano14Dec2018-v1/40000/5274DD59-A545-8845-8B94-112AEF7A1C2E.root',
       '/store/data/Run2018A/SingleMuon/NANOAOD/Nano14Dec2018-v1/40000/58B37899-84CD-5441-B935-7242EDCC2468.root',
       '/store/data/Run2018A/SingleMuon/NANOAOD/Nano14Dec2018-v1/40000/5E0E72A5-E89F-0B43-95E7-E64285193D52.root',
       '/store/data/Run2018A/SingleMuon/NANOAOD/Nano14Dec2018-v1/40000/6218D173-66EF-BA4A-BAB8-C63AFEF147E4.root',
       '/store/data/Run2018A/SingleMuon/NANOAOD/Nano14Dec2018-v1/40000/64E80095-EF14-184D-A83A-A86C4908250E.root',
       '/store/data/Run2018A/SingleMuon/NANOAOD/Nano14Dec2018-v1/40000/705153D6-7681-3A49-AAF2-D135E08AE23A.root',
       '/store/data/Run2018A/SingleMuon/NANOAOD/Nano14Dec2018-v1/40000/71A21E8E-306E-F14A-8D83-29033BE5699C.root',
       '/store/data/Run2018A/SingleMuon/NANOAOD/Nano14Dec2018-v1/40000/773E6816-71DB-9C46-95B0-9623DABB9B22.root',
       '/store/data/Run2018A/SingleMuon/NANOAOD/Nano14Dec2018-v1/40000/7898CD41-4D41-B346-9034-658448AEC6B1.root',
       '/store/data/Run2018A/SingleMuon/NANOAOD/Nano14Dec2018-v1/40000/7BA52D6E-0A1D-2B42-A8B9-45DBF2247CC4.root',
       '/store/data/Run2018A/SingleMuon/NANOAOD/Nano14Dec2018-v1/40000/7CACB10A-506A-A34D-B3FD-56C4C8BBFA7D.root',
       '/store/data/Run2018A/SingleMuon/NANOAOD/Nano14Dec2018-v1/40000/7D87724A-410E-2643-A074-DBF053C93849.root',
       '/store/data/Run2018A/SingleMuon/NANOAOD/Nano14Dec2018-v1/40000/7F92780C-C82F-7446-A38A-C3867C772670.root',
       '/store/data/Run2018A/SingleMuon/NANOAOD/Nano14Dec2018-v1/40000/8BF94AAE-867C-2D40-80AE-FBC8D21FCC1A.root',
       '/store/data/Run2018A/SingleMuon/NANOAOD/Nano14Dec2018-v1/40000/8C362EFB-A106-4F46-9479-4306C0E71CC3.root',
       '/store/data/Run2018A/SingleMuon/NANOAOD/Nano14Dec2018-v1/40000/9FBCD82B-4E68-F04E-A672-7E793AAE98BB.root',
       '/store/data/Run2018A/SingleMuon/NANOAOD/Nano14Dec2018-v1/40000/A3823C02-5AAD-5A46-9A0B-BBF4EEBEFD47.root',
       '/store/data/Run2018A/SingleMuon/NANOAOD/Nano14Dec2018-v1/40000/AFDD05E1-6E22-EE4E-99B8-584439B23BC8.root',
       '/store/data/Run2018A/SingleMuon/NANOAOD/Nano14Dec2018-v1/40000/B0EF003D-D9E9-A749-9B56-60D3B3A64146.root',
       '/store/data/Run2018A/SingleMuon/NANOAOD/Nano14Dec2018-v1/40000/B1336BE9-0158-6A44-B7FD-EA105E47B161.root',
       '/store/data/Run2018A/SingleMuon/NANOAOD/Nano14Dec2018-v1/40000/B1C1D310-7F52-B54D-825D-C85BB3429EBF.root',
       '/store/data/Run2018A/SingleMuon/NANOAOD/Nano14Dec2018-v1/40000/B2B29463-9D94-2A4A-805C-702101263975.root',
       '/store/data/Run2018A/SingleMuon/NANOAOD/Nano14Dec2018-v1/40000/B557222B-F0F1-1648-BBFA-849520B5208D.root',
       '/store/data/Run2018A/SingleMuon/NANOAOD/Nano14Dec2018-v1/40000/B88C74AA-6E1D-C641-97D9-C430EED6FEA6.root',
       '/store/data/Run2018A/SingleMuon/NANOAOD/Nano14Dec2018-v1/40000/B95B2C21-5D74-8F4F-A730-00650BE28513.root',
       '/store/data/Run2018A/SingleMuon/NANOAOD/Nano14Dec2018-v1/40000/BC40A72D-7573-DD43-8FF2-30B003695CE3.root',
       '/store/data/Run2018A/SingleMuon/NANOAOD/Nano14Dec2018-v1/40000/BDBC91D6-538F-6E49-A147-2612C3B25050.root',
       '/store/data/Run2018A/SingleMuon/NANOAOD/Nano14Dec2018-v1/40000/BEC5EBC5-2A75-0C4E-9BF1-A84137D4C565.root',
       '/store/data/Run2018A/SingleMuon/NANOAOD/Nano14Dec2018-v1/40000/BF81FCD2-3169-B243-81AB-07400AD25457.root',
       '/store/data/Run2018A/SingleMuon/NANOAOD/Nano14Dec2018-v1/40000/C76DEBE5-9AE7-324E-8CA4-E2751764E08C.root',
       '/store/data/Run2018A/SingleMuon/NANOAOD/Nano14Dec2018-v1/40000/C835BCA1-A5C8-9B41-AE6E-B483270A4A4C.root',
       '/store/data/Run2018A/SingleMuon/NANOAOD/Nano14Dec2018-v1/40000/C83FAE15-8ED4-CF4A-BC3A-F264687679AB.root',
       '/store/data/Run2018A/SingleMuon/NANOAOD/Nano14Dec2018-v1/40000/CA7FF7F6-2B6F-9B4B-B64C-C354E7E72FFA.root',
       '/store/data/Run2018A/SingleMuon/NANOAOD/Nano14Dec2018-v1/40000/CDD675FB-B365-7D45-BD6A-62909A8F5FA1.root',
       '/store/data/Run2018A/SingleMuon/NANOAOD/Nano14Dec2018-v1/40000/DBA1EECB-0480-0F4F-8CFF-A74DEF438E70.root',
       '/store/data/Run2018A/SingleMuon/NANOAOD/Nano14Dec2018-v1/40000/E235139E-9D97-CB4F-A182-C53A49C63BA4.root',
       '/store/data/Run2018A/SingleMuon/NANOAOD/Nano14Dec2018-v1/40000/E62B7E11-C2FF-0141-B06A-8796F074B075.root',
       '/store/data/Run2018A/SingleMuon/NANOAOD/Nano14Dec2018-v1/40000/E7D9D626-9AE0-784A-B9B8-8739D5ED32E9.root',
       '/store/data/Run2018A/SingleMuon/NANOAOD/Nano14Dec2018-v1/40000/E9A86E77-8140-BE48-8B72-2938850F94C4.root',
       '/store/data/Run2018A/SingleMuon/NANOAOD/Nano14Dec2018-v1/40000/FA96837C-9D69-8F4B-B9FB-05CA75BFD237.root',
       '/store/data/Run2018A/SingleMuon/NANOAOD/Nano14Dec2018-v1/40000/FAA34830-A3E0-E74B-9D42-37FC2AA64F45.root',
       '/store/data/Run2018A/SingleMuon/NANOAOD/Nano14Dec2018-v1/40000/FCA30DD8-1CDE-DE47-B1FB-F6192CE78748.root',
] )