# Change's:
Yazaki, Kuchukov:
0xF869(6)/F7BA(4) < 044a1f04244d0f0963024990200ebc1d8846330a5d301b3a0a0930
0x1F869(6)/1F7BA(4) < 044a1f04244d0f0963024990200ebc1d8846330a5d301b3a0a0930
;
Hardware (AT/MT):
0xC8ED(6)/C8FC(4) < 01 (MT), 00 (AT)
;
AT (fuel cut time, switch):
0xF26F(6)/F1C0(4) (Low. Bank) < 7E (R 1499.904 ms)/2A (T5 499.97 ms)
0x1F26F(6)/1F1C0(4) (Upp. Bank) < 7E (R 1499.904 ms)/2A (T5 499.97 ms)
;
0x13368(6)/13369(4) < 1C35567999 (R)/1E39567999 (T5)
;
Speed limit:
0xC924(6)/C933(4) < FA (250 km/h)
0xC925(6)/C934(4) < FF (255 km/h)
;
Fan:
0xC8F0(6)/C8FF(4) < AA (90 celsius, 1 speed)
0xC8F4(6)/C903(4) < B3 (99 celsius, 2 speed)
;
0xC8F1(6)/C900(4) < 39 (57 km/h, 1 speed)
0xC8F2(6)/C901(4) < 63 (99 km/h, 2 speed)
;
0xC8F6(612)/C905(4) < A8 (88 celsius, ?)
;
Idle 900 RPM at 110 Celsius:
0xD544(6)/D466(4) < 6E6E6D6C6A6968666462615E5955555A
0xD554(6)/D476(4) < 6E6E6D6C6A6968666462615E5955555A
;
Lambda (rear) disable:
0xF374(6)/F2C5(4) < 0
0x1F374(6)/1F2C5(4) < 0
;
0xF671(6)/F5C2(4) < 0
0x1F671(6)/1F5C2(4) < 0
;
0xF680(6)/F5D1(4) < 0
0x1F680(6)/1F5D1(4) < 0
;
0xF667(6)/F5B8(4) < 0
0x1F667(6)/1F5B8(4) < 0
;
0xC908(6)/C917(4) < 0
;
0xF800(6)/F751(4) < 0
0x1F800(6)/1F751(4) < 0
;
0xF803(6)/F754(4) < 0
0x1F803(6)/1F754(4) < 0
;
0xF7FE(6)/F74F(4) < 0
0x1F7FE(6)/1F74F(4) < 0
;
0xF24A(6)/F19B(4) < 0
0x1F24A(6)/1F19B(4) < 0
;
0xF323(6)/F274(4) < 0 (FF (612)?)
0x1F323(6)/1F274(4) < 0 (FF (612)?)
;
0xF326(6)/F277(4) < 0 (FF (612)?)
0x1F326(6)1F277(4) < 0 (FF (612)?)
;
0xF321(6)/F272(4) < 0 (FF (612)?)
0x1F321(6)/1F272(4) < 0 (FF (612)?)
;
Max. TL (11.09 ms):
0xC937(6)/0xC946(4) < E7 (11.088 ms)
;
Rescale to 10.8ms load:
(Low. Bnk)
0xF8CF(6)/F820(4) < 0A1827354352606E7D8B99A8B6C4D3E1
(Up. Bnk)
0x1F8CF(6)/1F820(4) < 0A1827354352606E7D8B99A8B6C4D3E1
;
Load threshold lambda control:
(Low. Bnk)
0xFA79(6)/F9CA(4) < 354343526E605235
(Up. Bnk)
0x1FA79(6)/1F9CA(4) < 354343526E605235
;
Overload TL (ms):
0x142C7(6)/142E8(4) < C6C6C6D0E1E1E7E7
;
Full load correction (WOT enrichment):
0x13E47(6)/13E48(4) < 80808080868D919398A0A3A7A7B0B0B0
;
Target Load Setpoint:
0xE454(6)/E376(4) < 666A6D6E6F6A68625F60625D595653516B7174797D7C7B7B7C7D7F78726B69666E73787D82828284858688817B76737171767B818886888A8D8E8F89827D7B7872777D858D8B8B8F9294968F8884808073787F89928F8F94969899968D8984847479808E97949499999D9D9B928E8888767B81939C99999D9DA2A2A098938B8B777C8298A09F9DA2A2A6A7A69D98908F787D859DA5A4A2A6A7ABADABA49D9693797F88A4AAA9A7ABADB0B2B2AAA49B977B818BAAAFAEADB0B2B6B7B7B0A9A09B7D8693B7B9B7B7B9BBC0C4C4BDB4ABA2808D9BC4C4C1C2C4C4CBD0D3CBC1B8A98292A2D0CFCDCDCDCFD8E0E1D9CEC4B28292A2D0CFCDCDCDCFD8E0E1D9CEC4B2
;
VE (afr):
0x13D47(6)/13D48(4) < 808080808080808080808080808080808080828180808080808080808080808080828381818082818080808080808080838485838282828180808080808080808085868484838281808080808080808080848686878584828080808080808080818486878E8E8E88858280808080808081848688919290908C8681808080808086848586919295989A9A8C8482818080868686878D9495989CA0A09E8F86848386868687898C8D939CA0A2A3A7A79C8F868686888A8A8D8E91A0A0A7A7A8A6AC86868686878788889CA0A0A7A7A8ACAC86868686868686989CA0A0A7A7A8ACAC86868686868686989CA0A0A7A7A8ACAC86868686868686989CA0A0A7A7A8ACAC
;
Intake temp boost corr.:
0xE7D4(6)/E6F6(4) < 9060402C122C406090000000000000009060402C122C406090000000000000009060402C122C406090000000000000009060402C122C406090000000000000009060402C122C406090000000000000009060402C122C406090000000000000009060402C122C406090000000000000009060402C122C406090000000000000009060402C122C406090000000000000009060402C122C406090000000000000009060402C122C406090000000000000009060402C122C406090000000000000009060402C122C406090000000000000009060402C122C406090000000000000009060402C122C406090000000000000009060402C122C40609000000000000000
;
Ign. (anti-lag):
13C77(6) < 1E
13C87(6) < 11
13C97(6) < 10
13CA7(6) < 09
13CB7(6) < 05
13CC7(6) < 01
13CD7(6) < 01
13CE7(6) < 01
13CF7(6) < 01
13D07(6) < 01
13D17(6) < 01
13D27(6) < 01
13CB8(6) < 09
13CC8(6) < 05
13CD8(6) < 05
13CE8(6) < 05
13CF8(6) < 05
13D08(6) < 05
13CD9(6) < 09
13CE9(6) < 09
13CF9(6) < 09
;
Ign. at idle chr. (KLZWL):
0x13D37(6)/13D38(4) < 252525251E1110090501010101010101
;
Global angle WMIN(limit);
0xF25B(6)/F1AC(4) < 85 (-21.75)
0x1F25B(6)/1F1AC(4) < 85 (-21.75)
;
Global angle WMAX(limit):
0xF25C(6)/F1AD(4) < 33 (39.75)
0x1F25C(6)/1F1AD(4) < 33 (39.75)
;
Ignition (95 fuel):
0x13C37(6)/13C38(4) < 242426282928272321212121212121212525282A2B2A2824222222222222222225252B3032302C2B252525252525252522252D32343434332D2A2A2A2A2A2A2A1E272F343636363535332F2E2E2E2E2E1E2C3135363636353534332F2F2E2E2E213132373736363535343331302E2D2D223535373736363535343331302E2D2D233637373736363535343331302E2D2D243737373736363535343331302E2D2D253837373736363535343331302E2D2D263837373736363535343331302E2D2D273837373736363535343331302E2D2D283837373736363535343331302E2D2D293837373736363535343331302E2D2D2A3837373736363535343331302E2D2D
;
Ignition (98 fuel):
0x13C37(6)/13C38(4) < 
242426282928272321212121212121212525282A2B2A2824222222222222222225252B3032302C2B252525252525252522252D32343434332D2A2A2A2A2A2A2A1E2730353737363535332F2E2E2E2E2E1E2D3236373736353534332F2F2E2E2E013233383837373635343331302E2D2D013536383837373635343331302E2D2D010738383837373636353432302E2D2D010738383837373636353432312F2D2D010709383837373636353432312F2E2D050809383837373636353432312F2E2D050809383837373636353432312F2D2D050838383837373535343332312F2D2D053938383837373535343331302E2D2D053938383837373535343331302E2D2D
;
Throttle angle threshold, (20.00, 20.83, ):
0xE8D4(6)/E7F6(4) < 3030303030303030, 3232323232323232, 4848484848484848
;
Sum of retard to enrichment (-11.25):
0xE7FE(4) <
0F0F0F0F0F0F0F0F0F0F0F0F0F0F0F0F0F0F0F0F0F0F0F0F0F0F0F0F0F0F0F0F0F0F0F0F0F0F0F0F0F0F0F0F0F0F0F0F0F0F0F0F0F0F0F0F0F0F0F0F0F0F0F0F0F0F0F0F0F0F0F0F0F0F0F0F0F0F0F0F0F0F0F0F0F0F0F0F0F0F0F0F0F0F0F0F0F0F0F0F0F0F0F0F0F0F0F0F0F0F0F0F0F0F0F0F0F0F0F0F0F0F0F0F0F0F0F0F0F0F0F0F0F0F0F0F0F0F0F0F0F0F0F0F0F0F0F0F0F0F0F0F0F0F0F0F0F0F0F0F0F0F0F0F0F0F0F0F0F0F0F0F0F0F0F0F0F0F0F0F0F0F0F0F0F0F0F0F0F0F0F0F0F0F0F0F0F0F0F0F0F0F0F0F0F0F0F0F0F0F0F0F0F0F0F0F0F0F0F0F0F0F0F0F0F0F0F0F0F0F0F0F0F0F0F0F0F0F0F0F0F0F0F0F0F0F0F0F0F0F0F0F0F0F0F0F
;
Max. boost pressure reduction (min. factor)
0xE9DC(6)/E8FE(4) < FFFFFFFFE6B39A80
;
Preload Table (TCV):
0x142B7(6)/142D8(4) < 63636321212121212121212121212121
;
Boost table's (16T, 0.3bar preload, 1.15 kg, stage 1, 95 fuel)
0xE5D4(6)/E4F6(4) <
55555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555657595A5B5C5E6160626364656768696A6C6D6E70717273757677797A7B7C7E7F80828384858788898A8C8D8E90919293959697999A9B9C9E9FA0A2A3A4A5A7A8A9AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACADAEB0B1B2B3B5B6B7B9BABBBCBEBFC0C2C3C4C5C7C8C9CACCCDCED0D1D2D3D5D6D7D9DADBDCDEDFE0E2E3E4E5E7E8E9EAECEDEEF0F1F2F3F5F6F7F9FAFBFCFE
;
afr 10.6909 (max. enrichment):
0xD1C4(6)/D0E6(4) < 808080808080808080808080808080808080808080808080808080808080808080808080808080808080808080808080808080808080808080808080808080B08080808080808080808080808080B0B080808080868D80808080808080B0B0B080808080868D9193808080A7A7B0B0B080808080868D919380A0A3A7A7B0B0B080808080868D919398A0A3A7A7B0B0B080808080868D919398A0A3A7A7B0B0B080808080868D919398A0A3A7A7B0B0B080808080868D919398A0A3A7A7B0B0B080808080868D919398A0A3A7A7B0B0B080808080868D919398A0A3A7A7B0B0B080808080868D919398A0A3A7A7B0B0B080808080868D919398A0A3A7A7B0B0B0
;
0xD2C4(6)/D1E6(4) < 808080808080808080808080808080808080808080808080808080808080808080808080808080808080808080808080808080808080808080808080808080B08080808080808080808080808080B0B080808080868D80808080808080B0B0B080808080868D9193808080A7A7B0B0B080808080868D919380A0A3A7A7B0B0B080808080868D919398A0A3A7A7B0B0B080808080868D919398A0A3A7A7B0B0B080808080868D919398A0A3A7A7B0B0B080808080868D919398A0A3A7A7B0B0B080808080868D919398A0A3A7A7B0B0B080808080868D919398A0A3A7A7B0B0B080808080868D919398A0A3A7A7B0B0B080808080868D919398A0A3A7A7B0B0B0
