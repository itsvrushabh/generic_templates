=~=~=~=~=~=~=~=~=~=~=~= PuTTY log 2019.10.16 17:14:18 =~=~=~=~=~=~=~=~=~=~=~=
ter
KRL-NRK-MPL-T4-ACC-RTR-39-45#      terminal lw
KRL-NRK-MPL-T4-ACC-RTR-39-45#      terminal lw e
KRL-NRK-MPL-T4-ACC-RTR-39-45#      terminal length 0
KRL-NRK-MPL-T4-ACC-RTR-39-45#show version
Cisco IOS XE Software, Version 16.09.01a
Cisco IOS Software [Fuji], ASR900 Software (PPC_LINUX_IOSD-UNIVERSALK9-M), Version 16.9.1a, RELEASE SOFTWARE (fc1)
Technical Support: http://www.cisco.com/techsupport
Copyright (c) 1986-2018 by Cisco Systems, Inc.
Compiled Thu 26-Jul-18 18:10 by mcpre


Cisco IOS-XE software, Copyright (c) 2005-2018 by cisco Systems, Inc.
All rights reserved.  Certain components of Cisco IOS-XE software are
licensed under the GNU General Public License ("GPL") Version 2.0.  The
software code licensed under GPL Version 2.0 is free software that comes
with ABSOLUTELY NO WARRANTY.  You can redistribute and/or modify such
GPL code under the terms of GPL Version 2.0.  For more details, see the
documentation or "License Notice" file accompanying the IOS-XE software,
or the applicable URL provided on the flyer accompanying the IOS-XE
software.


ROM: IOS-XE ROMMON

KRL-NRK-MPL-T4-ACC-RTR-39-45 uptime is 5 weeks, 5 days, 16 hours, 49 minutes
Uptime for this control processor is 5 weeks, 5 days, 16 hours, 55 minutes
System returned to ROM by reload
System restarted at 00:24:34 IST Fri Sep 6 2019
System image file is "bootflash:asr900rsp3-universalk9.16.09.01a.SPA.bin"
Last reload reason: Reload Command



This product contains cryptographic features and is subject to United
States and local country laws governing import, export, transfer and
use. Delivery of Cisco cryptographic products does not imply
third-party authority to import, export, distribute or use encryption.
Importers, exporters, distributors and users are responsible for
compliance with U.S. and local country laws. By using this product you
agree to comply with applicable laws and regulations. If you are unable
to comply with U.S. and local laws, return this product immediately.

A summary of U.S. laws governing Cisco cryptographic products may be found at:
http://www.cisco.com/wwl/export/crypto/tool/stqrg.html

If you require further assistance please contact us by sending email to
export@cisco.com.

License Level: metroaggrservices
License Type: Permanent
Next reload license Level: metroaggrservices

cisco ASR-903 (RSP3_400) processor (revision RSP3_400) with 1953664K/6147K bytes of memory.
Processor board ID FOX2245PFTF
16 Gigabit Ethernet interfaces
2 Ten Gigabit Ethernet interfaces
1 Channelized OC3/STM-1 port
32768K bytes of non-volatile configuration memory.
8388608K bytes of physical memory.
5703875K bytes of eUSB flash at bootflash:.

Configuration register is 0x2102

KRL-NRK-MPL-T4-ACC-RTR-39-45#Show platform
Chassis type: ASR-903

Slot      Type                State                 Insert time (ago) 
--------- ------------------- --------------------- ----------------- 
 0/0      A900-IMA8S1Z        ok                    5w5d          
 0/1      A900-IMA8S1Z        ok                    5w5d          
 0/5      A900-IMA3G-IMSG     ok                    5w5d          
R0        A900-RSP3C-400-S    ok, active            5w5d          
R1        A900-RSP3C-400-S    ok, standby           5w5d          
F0                            ok, active            5w5d          
F1                            ok, standby           5w5d          
P0        A900-PWR1200-D      ok                    5w5d          
P1        A900-PWR1200-D      ok                    5w5d          
P2        A903-FAN-E          ok                    5w5d          

Slot      CPLD Version        Firmware Version                        
--------- ------------------- --------------------------------------- 
R0        1802052C            15.6(20r)S                          
R1        1802052C            15.6(20r)S                          
F0        1802052C            15.6(20r)S                          
F1        1802052C            15.6(20r)S                          

KRL-NRK-MPL-T4-ACC-RTR-39-45#show redundancy
Redundant System Information :
------------------------------
       Available system uptime = 5 weeks, 5 days, 16 hours, 50 minutes
Switchovers system experienced = 0
              Standby failures = 0
        Last switchover reason = none

                 Hardware Mode = Duplex
    Configured Redundancy Mode = sso
     Operating Redundancy Mode = sso
              Maintenance Mode = Disabled
                Communications = Up

Current Processor Information :
-------------------------------
               Active Location = slot 6
        Current Software state = ACTIVE
       Uptime in current state = 5 weeks, 5 days, 16 hours, 49 minutes
                 Image Version = Cisco IOS Software [Fuji], ASR900 Software (PPC_LINUX_IOSD-UNIVERSALK9-M), Version 16.9.1a, RELEASE SOFTWARE (fc1)
Technical Support: http://www.cisco.com/techsupport
Copyright (c) 1986-2018 by Cisco Systems, Inc.
Compiled Thu 26-Jul-18 18:10 by mcpre
                          BOOT = bootflash:asr900rsp3-universalk9.16.09.01a.SPA.bin,1;
        Configuration register = 0x2102

Peer Processor Information :
----------------------------
              Standby Location = slot 7
        Current Software state = STANDBY HOT 
       Uptime in current state = 5 weeks, 5 days, 16 hours, 42 minutes
                 Image Version = Cisco IOS Software [Fuji], ASR900 Software (PPC_LINUX_IOSD-UNIVERSALK9-M), Version 16.9.1a, RELEASE SOFTWARE (fc1)
Technical Support: http://www.cisco.com/techsupport
Copyright (c) 1986-2018 by Cisco Systems, Inc.
Compiled Thu 26-Jul-18 18:10 by mcpre
                          BOOT = bootflash:asr900rsp3-universalk9.16.09.01a.SPA.bin,1;
                   CONFIG_FILE = 
        Configuration register = 0x2102


KRL-NRK-MPL-T4-ACC-RTR-39-45#show license
Index 1 Feature: metroaggrservices              
	Period left: Life time
	License Type: Permanent
	License State: Active, In Use
	License Count: Non-Counted
	License Priority: Medium
Index 2 Feature: metroipservices                
	Period left: Not Activated
	Period Used: 0  minute  0  second  
	License Type: EvalRightToUse
	License State: Active, Not in Use, EULA not accepted
	License Count: Non-Counted
	License Priority: None
Index 3 Feature: metroservices                  
	Period left: Not Activated
	Period Used: 0  minute  0  second  
	License Type: EvalRightToUse
	License State: Active, Not in Use, EULA not accepted
	License Count: Non-Counted
	License Priority: None
Index 4 Feature: atm                            
	Period left: Not Activated
	Period Used: 0  minute  0  second  
	License Type: EvalRightToUse
	License State: Active, Not in Use, EULA not accepted
	License Count: Non-Counted
	License Priority: None
Index 5 Feature: oc3                            
	Period left: Life time
	License Type: Permanent
	License State: Active, In Use
	License Count: 4/4/0  (Active/In-use/Violation)
	License Priority: Medium
Index 6 Feature: oc12                           
Index 7 Feature: 1588                           
Index 8 Feature: ipsec                          
Index 9 Feature: oc48                           
Index 10 Feature: oc192                          

KRL-NRK-MPL-T4-ACC-RTR-39-45#show license feature
Feature name             Enforcement  Evaluation  Subscription   Enabled  RightToUse 
metroaggrservices        yes          yes         no             yes      yes        
metroipservices          yes          yes         no             no       yes        
metroservices            no           yes         no             no       yes        
atm                      yes          yes         no             no       yes        
oc3                      yes          yes         no             yes      no         
oc12                     yes          yes         no             no       no         
1588                     yes          yes         no             no       no         
ipsec                    yes          no          no             no       no         
oc48                     yes          yes         no             no       no         
oc192                    yes          yes         no             no       no         

KRL-NRK-MPL-T4-ACC-RTR-39-45#show license detail
Index: 1 	Feature: atm                               Version: 1.0
	License Type: EvalRightToUse
	License State: Active, Not in Use, EULA not accepted
	    Evaluation total period: 8  weeks 4  days 
	    Evaluation period left: 8  weeks 4  days 
	    Period used: 0  minute  0  second  
	Lock type: Non Node locked
	Vendor info: <UDI><PID>NOTLOCKED</PID><SN>NOTLOCKED</SN></UDI><T>RTU</T>
	License Addition: Additive
	License Generation version: 0x8200000
	License Count: Non-Counted
	License Priority: None
	Store Index: 3
	Store Name: Built-In License Storage
Index: 2 	Feature: metroaggrservices                 Version: 1.0
	License Type: Permanent
	License State: Active, In Use
	Lock type: Node locked
	Vendor info: <PID>ASR-903</PID><SN>FOX2245PFTF</SN>
	License Addition: Exclusive
	License Generation version: 0x8100000
	License Count: Non-Counted
	License Priority: Medium
	Store Index: 0
	Store Name: Primary License Storage
Index: 3 	Feature: metroaggrservices                 Version: 1.0
	License Type: EvalRightToUse
	License State: Inactive
	    Evaluation total period: 8  weeks 4  days 
	    Evaluation period left: 8  weeks 4  days 
	    Period used: 0  minute  0  second  
	Lock type: Non Node locked
	Vendor info: <UDI><PID>NOTLOCKED</PID><SN>NOTLOCKED</SN></UDI><T>RTU</T>
	License Addition: Additive
	License Generation version: 0x8200000
	License Count: Non-Counted
	License Priority: None
	Store Index: 0
	Store Name: Built-In License Storage
Index: 4 	Feature: metroipservices                   Version: 1.0
	License Type: EvalRightToUse
	License State: Active, Not in Use, EULA not accepted
	    Evaluation total period: 8  weeks 4  days 
	    Evaluation period left: 8  weeks 4  days 
	    Period used: 0  minute  0  second  
	Lock type: Non Node locked
	Vendor info: <UDI><PID>NOTLOCKED</PID><SN>NOTLOCKED</SN></UDI><T>RTU</T>
	License Addition: Additive
	License Generation version: 0x8200000
	License Count: Non-Counted
	License Priority: None
	Store Index: 1
	Store Name: Built-In License Storage
Index: 5 	Feature: metroservices                     Version: 1.0
	License Type: EvalRightToUse
	License State: Active, Not in Use, EULA not accepted
	    Evaluation total period: 8  weeks 4  days 
	    Evaluation period left: 8  weeks 4  days 
	    Period used: 0  minute  0  second  
	Lock type: Non Node locked
	Vendor info: <UDI><PID>NOTLOCKED</PID><SN>NOTLOCKED</SN></UDI><T>RTU</T>
	License Addition: Additive
	License Generation version: 0x8200000
	License Count: Non-Counted
	License Priority: None
	Store Index: 2
	Store Name: Built-In License Storage
Index: 6 	Feature: oc3                               Version: 1.0
	License Type: Permanent
	License State: Active, In Use
	Lock type: Node locked
	Vendor info: <UDI><PID>ASR-903</PID><SN>FOX2245PFTF</SN></UDI>
	License Addition: Exclusive
	License Generation version: 0x8100000
	License Count: 4/4/0  (Active/In-use/Violation)
	License Priority: Medium
	Store Index: 1
	Store Name: Primary License Storage

KRL-NRK-MPL-T4-ACC-RTR-39-45#show inventory
NAME: "Chassis", DESCR: "ASR 903 Series Router Chassis"
PID: ASR-903           , VID: V01  , SN: FOX2245PFTF

NAME: "IM subslot 0/0", DESCR: "8-port Gigabit Ethernet & 1-port Ten Gigabit Ethernet SFP Interface Module"
PID: A900-IMA8S1Z      , VID: V01  , SN: FOC2251NGVT

NAME: "subslot 0/0 transceiver 0", DESCR: "GE LX"
PID: GLC-LH-SMD          , VID: V01  , SN: ACW224515GS     

NAME: "subslot 0/0 transceiver 1", DESCR: "GE LX"
PID: GLC-LH-SMD          , VID: V01  , SN: ACW224515GR     

NAME: "subslot 0/0 transceiver 2", DESCR: "GE T"
PID: GLC-TE              , VID: V01  , SN: AVC224728LZ     

NAME: "subslot 0/0 transceiver 8", DESCR: "GE LX"
PID: GLC-LH-SMD          , VID: V01  , SN: ACW224515G3     

NAME: "IM subslot 0/1", DESCR: "8-port Gigabit Ethernet & 1-port Ten Gigabit Ethernet SFP Interface Module"
PID: A900-IMA8S1Z      , VID: V01  , SN: FOC2251NLSY

NAME: "subslot 0/1 transceiver 0", DESCR: "GE LX"
PID: GLC-LH-SMD          , VID: V01  , SN: ACW224516A7     

NAME: "subslot 0/1 transceiver 8", DESCR: "OC3 LR-1/STM1 L-1.1"
PID: ONS-SI-155-L1       , VID: V03  , SN: OPM22460UZ6     

NAME: "IM subslot 0/5", DESCR: "ASR 900 Combo 4 port DS3 12 DS1 and 4 OCx"
PID: A900-IMA3G-IMSG   , VID: V01  , SN: FOC2301PFRA

NAME: "subslot 0/5 transceiver 16", DESCR: "GE LX"
PID: GLC-LH-SMD          , VID: V01  , SN: ACW224515GQ     

NAME: "subslot 0/5 transceiver 17", DESCR: "GE T"
PID: GLC-TE              , VID: V01  , SN: AVC224728LA     

NAME: "module R0", DESCR: "ASR 900 Route Switch Processor 3, 400G, XL Scale"
PID: A900-RSP3C-400-S  , VID: V04  , SN: FOC2302PN5Z

NAME: "module R1", DESCR: "ASR 900 Route Switch Processor 3, 400G, XL Scale"
PID: A900-RSP3C-400-S  , VID: V04  , SN: FOC2302P83P

NAME: "Power Supply Module 0", DESCR: "ASR 900 1200W DC Power Supply"
PID: A900-PWR1200-D    , VID: V01  , SN: LIT22492YP5

NAME: "Power Supply Module 1", DESCR: "ASR 900 1200W DC Power Supply"
PID: A900-PWR1200-D    , VID: V01  , SN: LIT22492YJT

NAME: "Fan Tray", DESCR: "ASR 903 FAN Tray"
PID: A903-FAN-E        , VID: V03  , SN: FOC2237P05P


KRL-NRK-MPL-T4-ACC-RTR-39-45#show environment

Number of Critical alarms:  0
Number of Major alarms:     0
Number of Minor alarms:     0

 Slot        Sensor          Current State   Reading        Threshold(Minor,Major,Critical,Shutdown)
 ----------  --------------  --------------- ------------   ---------------------------------------
 P0          PEM Iout        Normal          15   A      	na
 P0          PEM Vout        Normal          12   V DC   	na
 P0          PEM Vin         Normal          53   V DC   	na
 P0          Temp: Temp 1    Normal          42   Celsius	(110,115,120,125)(Celsius)
 P0          Temp: Temp 2    Normal          39   Celsius	(110,115,120,125)(Celsius)
 P1          PEM Iout        Normal          16   A      	na
 P1          PEM Vout        Normal          12   V DC   	na
 P1          PEM Vin         Normal          53   V DC   	na
 P1          Temp: Temp 1    Normal          35   Celsius	(110,115,120,125)(Celsius)
 P1          Temp: Temp 2    Normal          30   Celsius	(110,115,120,125)(Celsius)
 P2          Temp: FC PWM1   Fan Speed 65%   24   Celsius	(-3 ,16 ,31 )(Celsius)
 R0          Temp: ARAD+0    Normal          32   Celsius	(95 ,102,108,112)(Celsius)
 R0          Temp: N-Inlet   Normal          32   Celsius	(70 ,75 ,80 ,100)(Celsius)
 R0          Temp: ARAD+1    Normal          49   Celsius	(95 ,102,108,112)(Celsius)
 R0          Temp: N-Outlet  Normal          49   Celsius	(80 ,85 ,90 ,105)(Celsius)
 R0          VCPU : VX2      Normal          843  mV     	na
 R0          VCPU : VP1      Normal          1794 mV     	na
 R0          VCPU : VP2      Normal          1196 mV     	na
 R0          VCPU : VP3      Normal          898  mV     	na
 R0          VCPU : VP4      Normal          898  mV     	na
 R0          VCPU : VH       Normal          12139mV     	na
 R0          Temp: CPU       Normal          28   Celsius	(75 ,80 ,85 ,95 )(Celsius)
 R0          Temp: C-Inlet   Normal          28   Celsius	(67 ,70 ,75 ,80 )(Celsius)
 R0          Temp: PCIe Sw   Normal          35   Celsius	(75 ,80 ,85 ,95 )(Celsius)
 R0          Temp: C-Outlet  Normal          35   Celsius	(80 ,85 ,90 ,100)(Celsius)
 R0          A-TPS1-1        Normal          2501 mV     	na
 R0          A-TPS1-2        Normal          992  mV     	na
 R0          A-TPS2-1        Normal          990  mV     	na
 R0          A-TPS2-2        Normal          1478 mV     	na
 R0          A-TPS3-1        Normal          990  mV     	na
 R0          A-TPS3-2        Normal          1476 mV     	na
 R0          A-TPS4-1        Normal          998  mV     	na
 R0          A-TPS5-1        Normal          996  mV     	na
 R0          A-VH            Normal          11888mV     	na
 R0          A-VP2           Normal          1801 mV     	na
 R0          A-VP3           Normal          3307 mV     	na
 R0          A-VP4           Normal          1045 mV     	na
 R0          A-VAUX1         Normal          1199 mV     	na
 R0          A-VAUX2         Normal          1798 mV     	na
 R1          Temp: ARAD+0    Normal          31   Celsius	(95 ,102,108,112)(Celsius)
 R1          Temp: N-Inlet   Normal          31   Celsius	(70 ,75 ,80 ,100)(Celsius)
 R1          Temp: ARAD+1    Normal          49   Celsius	(95 ,102,108,112)(Celsius)
 R1          Temp: N-Outlet  Normal          49   Celsius	(80 ,85 ,90 ,105)(Celsius)
 R1          VCPU : VX2      Normal          844  mV     	na
 R1          VCPU : VP1      Normal          1794 mV     	na
 R1          VCPU : VP2      Normal          1198 mV     	na
 R1          VCPU : VP3      Normal          898  mV     	na
 R1          VCPU : VP4      Normal          896  mV     	na
 R1          VCPU : VH       Normal          12144mV     	na
 R1          Temp: CPU       Normal          29   Celsius	(75 ,80 ,85 ,95 )(Celsius)
 R1          Temp: C-Inlet   Normal          29   Celsius	(67 ,70 ,75 ,80 )(Celsius)
 R1          Temp: PCIe Sw   Normal          36   Celsius	(75 ,80 ,85 ,95 )(Celsius)
 R1          Temp: C-Outlet  Normal          36   Celsius	(80 ,85 ,90 ,100)(Celsius)
 R1          A-TPS1-1        Normal          2492 mV     	na
 R1          A-TPS1-2        Normal          990  mV     	na
 R1          A-TPS2-1        Normal          996  mV     	na
 R1          A-TPS2-2        Normal          1484 mV     	na
 R1          A-TPS3-1        Normal          994  mV     	na
 R1          A-TPS3-2        Normal          1484 mV     	na
 R1          A-TPS4-1        Normal          998  mV     	na
 R1          A-TPS5-1        Normal          996  mV     	na
 R1          A-VH            Normal          11888mV     	na
 R1          A-VP2           Normal          1804 mV     	na
 R1          A-VP3           Normal          3305 mV     	na
 R1          A-VP4           Normal          1046 mV     	na
 R1          A-VAUX1         Normal          1199 mV     	na
 R1          A-VAUX2         Normal          1802 mV     	na


KRL-NRK-MPL-T4-ACC-RTR-39-45#show facility-alarm status
System Totals  Critical: 1  Major: 0  Minor: 0

Source                     Time                   Severity      Syslog String                  Description [Index]
------                     ------                 --------      -------------                  -------------------
GigabitEthernet0           Sep 06 2019 00:09:37   CRITICAL      ETHERNET_PORT_LINK_DOWN        Physical Port Link Down [1]
GigabitEthernet0/0/1       Sep 06 2019 00:11:00   INFO          ETHERNET_PORT_ADMIN_DOWN       Physical Port Administrative State Down [2]
GigabitEthernet0/0/2       Oct 11 2019 18:41:07   INFO          ETHERNET_PORT_ADMIN_DOWN       Physical Port Administrative State Down [2]
xcvr container 0/0/3       Oct 01 2019 13:35:29   INFO          XCVR_MISSING                   Transceiver Missing [0]
xcvr container 0/0/4       Sep 06 2019 00:10:32   INFO          XCVR_MISSING                   Transceiver Missing [0]
xcvr container 0/0/5       Sep 06 2019 00:10:32   INFO          XCVR_MISSING                   Transceiver Missing [0]
xcvr container 0/0/6       Sep 06 2019 00:10:32   INFO          XCVR_MISSING                   Transceiver Missing [0]
xcvr container 0/0/7       Sep 06 2019 00:10:32   INFO          XCVR_MISSING                   Transceiver Missing [0]
TenGigabitEthernet0/0/8    Sep 06 2019 00:11:00   INFO          ETHERNET_PORT_ADMIN_DOWN       Physical Port Administrative State Down [2]
xcvr container 0/1/1       Sep 06 2019 00:10:31   INFO          XCVR_MISSING                   Transceiver Missing [0]
xcvr container 0/1/2       Sep 06 2019 00:10:31   INFO          XCVR_MISSING                   Transceiver Missing [0]
xcvr container 0/1/3       Sep 06 2019 00:10:31   INFO          XCVR_MISSING                   Transceiver Missing [0]
xcvr container 0/1/4       Sep 06 2019 00:10:31   INFO          XCVR_MISSING                   Transceiver Missing [0]
xcvr container 0/1/5       Sep 06 2019 00:10:31   INFO          XCVR_MISSING                   Transceiver Missing [0]
xcvr container 0/1/6       Sep 06 2019 00:10:31   INFO          XCVR_MISSING                   Transceiver Missing [0]
xcvr container 0/1/7       Sep 06 2019 00:10:31   INFO          XCVR_MISSING                   Transceiver Missing [0]
TenGigabitEthernet0/1/8    Oct 01 2019 15:21:03   INFO          ETHERNET_PORT_ADMIN_DOWN       Physical Port Administrative State Down [2]

KRL-NRK-MPL-T4-ACC-RTR-39-45#show crypto key mypubkey rsa
% Key pair was generated at: 08:46:04 IST Oct 2 2019
Key name: KRL-NRK-MPL-T4-ACC-RTR-39-45.bharti.com
Key type: RSA KEYS
 Storage Device: not specified
 Usage: General Purpose Key
 Key is not exportable. Redundancy enabled.
 Key Data:
  30819F30 0D06092A 864886F7 0D010101 05000381 8D003081 89028181 00B6579A 
  FF919204 63666C97 743A52D0 E203B7B0 E6295666 137936C5 F5B5BB1C ADC16C75 
  7D82F979 FAA28F9D AF1DF93A D5511CC6 DBD8DC42 09990834 E410D3AF 10B6D1BE 
  13B064CC 04947DEC D208DDE5 25DC2B56 81B0D184 DF320E57 C0B07877 CEBF0F78 
  AE258326 BC041652 2FE2ED65 2A040785 D53E1598 FB0D7074 DED2ED75 93020301 
  0001
% Key pair was generated at: 08:46:09 IST Oct 2 2019
Key name: KRL-NRK-MPL-T4-ACC-RTR-39-45.bharti.com.server
Key type: RSA KEYS
Temporary key
 Usage: Encryption Key
 Key is not exportable.
 Key Data:
  307C300D 06092A86 4886F70D 01010105 00036B00 30680261 00EAF17B 3A7D113D 
  9EC0644C 89F9FF30 F1803B08 3F63379D 9DFD5503 45CE8928 BC98DE75 16922FD0 
  B1D7C4ED 51EB5D7B CCD1A23B 3DA997BA 919D25B6 3F3E14B8 3886D899 560FA1F0 
  12DCE135 30821777 291E13BD 0BECED93 3D323D58 133EF23F 57020301 0001
KRL-NRK-MPL-T4-ACC-RTR-39-45#show logging
Syslog logging: enabled (0 messages dropped, 1 messages rate-limited, 0 flushes, 0 overruns, xml disabled, filtering disabled)

No Active Message Discriminator.



No Inactive Message Discriminator.


    Console logging: disabled
    Monitor logging: level debugging, 0 messages logged, xml disabled,
                     filtering disabled
    Buffer logging:  level debugging, 346 messages logged, xml disabled,
                    filtering disabled
    Exception Logging: size (4096 bytes)
    Count and timestamp logging messages: disabled
    Persistent logging: disabled

No active filter modules.

    Trap logging: level debugging, 330 message lines logged
        Logging to 202.56.230.23  (udp port 514, audit disabled,
              link up),
              79 message lines logged, 
              0 message lines rate-limited, 
              0 message lines dropped-by-MD, 
              xml disabled, sequence number disabled
              filtering disabled
        Logging to 10.3.170.155  (udp port 514, audit disabled,
              link up),
              80 message lines logged, 
              0 message lines rate-limited, 
              0 message lines dropped-by-MD, 
              xml disabled, sequence number disabled
              filtering disabled
        Logging to 10.3.170.158  (udp port 514, audit disabled,
              link up),
              80 message lines logged, 
              0 message lines rate-limited, 
              0 message lines dropped-by-MD, 
              xml disabled, sequence number disabled
              filtering disabled
        Logging to 10.3.169.160  (udp port 514, audit disabled,
              link up),
              80 message lines logged, 
              0 message lines rate-limited, 
              0 message lines dropped-by-MD, 
              xml disabled, sequence number disabled
              filtering disabled
        Logging Source-Interface:       VRF Name:
        Loopback0                       

Log Buffer (4096 bytes):
7)
000315: Oct 14 11:48:55.034 IST: %SEC_LOGIN-5-LOGIN_SUCCESS: Login Success [user: admin] [Source: 61.95.140.252] [localport: 23] at 11:48:55 IST Mon Oct 14 2019
000316: Oct 14 11:50:31.257 IST: %SEC_LOGIN-5-LOGIN_SUCCESS: Login Success [user: admin] [Source: 61.95.140.252] [localport: 23] at 11:50:31 IST Mon Oct 14 2019
000317: Oct 14 12:03:05.716 IST: %SEC_LOGIN-5-LOGIN_SUCCESS: Login Success [user: 64809nav] [Source: 182.79.246.42] [localport: 22] at 12:03:05 IST Mon Oct 14 2019
000318: Oct 14 12:27:38.112 IST: %SEC_LOGIN-5-LOGIN_SUCCESS: Login Success [user: kiwicat] [Source: 202.123.37.77] [localport: 23] at 12:27:38 IST Mon Oct 14 2019
000319: Oct 14 12:32:28.891 IST: %SEC_LOGIN-5-LOGIN_SUCCESS: Login Success [user: ciscoin] [Source: 61.95.140.252] [localport: 23] at 12:32:28 IST Mon Oct 14 2019
000320: Oct 14 12:33:58.658 IST: %SYS-5-CONFIG_I: Configured from console by kiwicat on vty0 (202.123.37.77)
000321: Oct 14 13:09:48.610 IST: %SEC_LOGIN-5-LOGIN_SUCCESS: Login Success [user: ciscoin] [Source: 61.95.140.252] [localport: 23] at 13:09:48 IST Mon Oct 14 2019
000322: Oct 14 13:10:51.258 IST: %LICENSE-6-EULA_ACCEPT_ALL: The Right to Use End User License Agreement is accepted
000323: Oct 14 13:11:08.992 IST: %SYS-5-CONFIG_I: Configured from console by ciscoin on vty0 (61.95.140.252)
000324: Oct 14 13:14:21.765 IST: %SYS-5-CONFIG_I: Configured from console by ciscoin on vty0 (61.95.140.252)
000325: Oct 14 13:15:04.853 IST: %SDH-2-ALARM: SDH 0/5/16: SONET_LINK_DOWN asserted
000326: Oct 14 13:15:05.203 IST: %SDH-2-ALARM: SDH 0/5/16: SONET_LINK_DOWN cleared
000327: Oct 14 13:15:07.463 IST: %SDH-2-ALARM: SDH 0/5/16: SLOS asserted
000328: Oct 14 13:15:07.463 IST: %CONTROLLER-5-UPDOWN: Controller SDH 0/5/16, changed state to down
000329: Oct 14 13:15:07.464 IST: %SDH-2-ALARM: SDH 0/5/16: SONET_LINK_DOWN asserted
000330: Oct 14 13:15:32.112 IST: %SYS-5-CONFIG_I: Configured from console by ciscoin on vty0 (61.95.140.252)
000331: Oct 15 11:38:11.003 IST: %SEC_LOGIN-5-LOGIN_SUCCESS: Login Success [user: A1SAWJ7G] [Source: 182.79.246.38] [localport: 23] at 11:38:11 IST Tue Oct 15 2019
000332: Oct 15 11:41:04.016 IST: %PARSER-5-HIDDEN: Warning!!! ' quit ' is a hidden command. Use of this command is not recommended/supported and will be removed in future.
000333: Oct 15 14:48:40.703 IST: %SDH-2-ALARM: SDH 0/5/16: SLOS cleared
000334: Oct 15 14:48:40.704 IST: %CONTROLLER-5-UPDOWN: Controller SDH 0/5/16, changed state to up
000335: Oct 15 14:48:40.705 IST: %SDH-2-ALARM: SDH 0/5/16: SONET_LINK_DOWN cleared
000336: Oct 15 14:48:40.705 IST: %SDH-2-ALARM: SDH 0/5/16.1 PATH : PAIS cleared
000337: Oct 15 15:14:10.679 IST: %SEC_LOGIN-5-LOGIN_SUCCESS: Login Success [user: kiwicat] [Source: 202.123.37.77] [localport: 23] at 15:14:10 IST Tue Oct 15 2019
000338: Oct 15 15:49:38.627 IST: %SEC_LOGIN-5-LOGIN_SUCCESS: Login Success [user: kiwicat] [Source: 182.79.246.58] [localport: 23] at 15:49:38 IST Tue Oct 15 2019
000339: Oct 16 09:17:10.970 IST: %SEC_LOGIN-5-LOGIN_SUCCESS: Login Success [user: kiwicat] [Source: 202.123.37.77] [localport: 23] at 09:17:10 IST Wed Oct 16 2019
000340: Oct 16 09:17:39.771 IST: %SEC_LOGIN-5-LOGIN_SUCCESS: Login Success [user: 213496sha] [Source: 202.123.37.77] [localport: 23] at 09:17:39 IST Wed Oct 16 2019
000341: Oct 16 09:17:53.355 IST: %SEC_LOGIN-5-LOGIN_SUCCESS: Login Success [user: kiwicat] [Source: 202.123.37.77] [localport: 23] at 09:17:53 IST Wed Oct 16 2019
000342: Oct 16 09:33:29.516 IST: %SEC_LOGIN-5-LOGIN_SUCCESS: Login Success [user: 213496sha] [Source: 202.123.37.77] [localport: 23] at 09:33:29 IST Wed Oct 16 2019
000343: Oct 16 09:33:44.908 IST: %SEC_LOGIN-5-LOGIN_SUCCESS: Login Success [user: 213496sha] [Source: 202.123.37.77] [localport: 23] at 09:33:44 IST Wed Oct 16 2019
000344: Oct 16 10:00:46.437 IST: %SEC_LOGIN-5-LOGIN_SUCCESS: Login Success [user: 2366kri] [Source: 61.95.140.252] [localport: 23] at 10:00:46 IST Wed Oct 16 2019
000345: Oct 16 17:12:57.522 IST: %SEC_LOGIN-5-LOGIN_SUCCESS: Login Success [user: 2366kri] [Source: 61.95.140.252] [localport: 23] at 17:12:57 IST Wed Oct 16 2019
KRL-NRK-MPL-T4-ACC-RTR-39-45#show ip int b
Interface              IP-Address      OK? Method Status                Protocol
GigabitEthernet0/0/0   172.23.251.14   YES manual up                    up      
GigabitEthernet0/0/1   unassigned      YES NVRAM  administratively down down    
GigabitEthernet0/0/2   unassigned      YES NVRAM  administratively down down    
GigabitEthernet0/0/3   unassigned      YES NVRAM  administratively down down    
GigabitEthernet0/0/4   unassigned      YES NVRAM  administratively down down    
GigabitEthernet0/0/5   unassigned      YES unset  administratively down down    
GigabitEthernet0/0/6   unassigned      YES NVRAM  administratively down down    
GigabitEthernet0/0/7   unassigned      YES NVRAM  administratively down down    
Te0/0/8                unassigned      YES NVRAM  administratively down down    
GigabitEthernet0/1/0   172.23.251.16   YES manual up                    up      
GigabitEthernet0/1/1   unassigned      YES NVRAM  administratively down down    
GigabitEthernet0/1/2   unassigned      YES NVRAM  administratively down down    
GigabitEthernet0/1/3   unassigned      YES NVRAM  administratively down down    
GigabitEthernet0/1/4   unassigned      YES NVRAM  administratively down down    
GigabitEthernet0/1/5   unassigned      YES NVRAM  administratively down down    
GigabitEthernet0/1/6   unassigned      YES NVRAM  administratively down down    
GigabitEthernet0/1/7   unassigned      YES NVRAM  administratively down down    
Te0/1/8                unassigned      YES NVRAM  administratively down down    
GigabitEthernet0       unassigned      YES NVRAM  down                  down    
Loopback0              116.119.39.45   YES manual up                    up      
KRL-NRK-MPL-T4-ACC-RTR-39-45#show clock
17:15:19.078 IST Wed Oct 16 2019
KRL-NRK-MPL-T4-ACC-RTR-39-45#show ntp status
Clock is synchronized, stratum 4, reference is 202.56.230.29  
nominal freq is 250.0000 Hz, actual freq is 249.9973 Hz, precision is 2**10
ntp uptime is 123928300 (1/100 of seconds), resolution is 4016
reference time is E1515967.F020C730 (14:25:03.938 IST Wed Oct 16 2019)
clock offset is -2.9812 msec, root delay is 8.43 msec
root dispersion is 205.77 msec, peer dispersion is 1.07 msec
loopfilter state is 'CTRL' (Normal Controlled Loop), drift is 0.000010492 s/s
system poll interval is 1024, last update was 10219 sec ago.
KRL-NRK-MPL-T4-ACC-RTR-39-45#show isis neighbors

System Id       Type Interface     IP Address      State Holdtime Circuit Id
KRL-MPL-LTE-PE- L2   Gi0/0/0       172.23.251.15   UP    24       00
KRL-MPL-LTE-PE- L2   Gi0/1/0       172.23.251.17   UP    26       00
KRL-NRK-MPL-T4-ACC-RTR-39-45#show ip bgp summary
BGP router identifier 116.119.39.45, local AS number 9730
BGP table version is 56065, main routing table version 56065
1827 network entries using 263088 bytes of memory
3709 path entries using 326392 bytes of memory
1819 multipath network entries and 3638 multipath paths
1537/1537 BGP path/bestpath attribute entries using 258216 bytes of memory
3087 BGP rrinfo entries using 115080 bytes of memory
8 BGP AS-PATH entries using 192 bytes of memory
1518 BGP community entries using 36432 bytes of memory
0 BGP route-map cache entries using 0 bytes of memory
0 BGP filter-list cache entries using 0 bytes of memory
BGP using 999400 total bytes of memory
BGP activity 2367/540 prefixes, 22383/18674 paths, scan interval 60 secs

Neighbor        V           AS MsgRcvd MsgSent   TblVer  InQ OutQ Up/Down  State/PfxRcd
172.23.20.89    4         9730   58007   22709    56065    0    0 2w0d         1855
172.23.20.90    4         9730   56801   22724    56065    0    0 2w0d         1853
KRL-NRK-MPL-T4-ACC-RTR-39-45#show running | sec isis
 ip router isis 
 isis circuit-type level-2-only
 isis network point-to-point 
 isis metric 640 level-2
 isis authentication mode md5
 isis authentication key-chain bharti
 no isis hello padding always
 no isis hello padding always
 ip router isis 
 isis circuit-type level-2-only
 isis network point-to-point 
 isis metric 640 level-2
 isis authentication mode md5
 isis authentication key-chain bharti
 no isis hello padding always
router isis
 net 49.5005.1161.1903.9045.00
 is-type level-2-only
 authentication mode md5 level-2
 authentication key-chain bharti level-2
 metric-style wide
 fast-flood 10
 set-overload-bit on-startup wait-for-bgp
 max-lsp-lifetime 65535
 lsp-refresh-interval 65000
 spf-interval 5 50 200
 prc-interval 5 50 200
 lsp-gen-interval 5 50 200
 no hello padding
 log-adjacency-changes
 nsf cisco
 passive-interface Loopback0
 maximum-paths 32
 mpls ldp sync
 mpls traffic-eng router-id Loopback0
 mpls traffic-eng level-2
 mpls traffic-eng multicast-intact
KRL-NRK-MPL-T4-ACC-RTR-39-45#show runnin | sec bgp
 set-overload-bit on-startup wait-for-bgp
router bgp 9730
 bgp router-id 116.119.39.45
 bgp log-neighbor-changes
 bgp graceful-restart
 no bgp default ipv4-unicast
 neighbor LU_RR peer-group
 neighbor LU_RR remote-as 9730
 neighbor LU_RR update-source Loopback0
 neighbor 172.23.20.89 peer-group LU_RR
 neighbor 172.23.20.90 peer-group LU_RR
 !
 address-family ipv4
  bgp additional-paths select all
  bgp additional-paths select backup
  bgp additional-paths receive
  bgp nexthop route-map Next_Hop_Min_32
  bgp nexthop trigger delay 0
  network 116.119.39.45 mask 255.255.255.255
  neighbor LU_RR send-community both
  neighbor LU_RR next-hop-self all
  neighbor LU_RR send-label
  neighbor 172.23.20.89 activate
  neighbor 172.23.20.90 activate
  maximum-paths ibgp 2
 exit-address-family
KRL-NRK-MPL-T4-ACC-RTR-39-45#show mpls ldp neighbor
    Peer LDP Ident: 202.123.37.77:0; Local LDP Ident 116.119.39.45:0
	TCP connection: 202.123.37.77.49561 - 116.119.39.45.646
	State: Oper; Msgs sent/rcvd: 23734/24935; Downstream
	Up time: 2w0d
	LDP discovery sources:
	  GigabitEthernet0/0/0, Src IP addr: 172.23.251.15
	  Targeted Hello 116.119.39.45 -> 202.123.37.77, active, passive
        Addresses bound to peer LDP Ident:
          202.123.37.77   116.119.2.219   172.16.4.47     182.79.152.10   
          10.71.93.13     10.3.6.5        10.56.74.25     10.78.22.22     
          172.29.11.51    182.79.158.136  10.20.6.5       172.16.19.226   
          116.119.37.250  10.7.7.5        10.4.7.5        10.52.52.1      
          10.34.1.17      172.29.200.11   172.23.251.15   172.23.20.89    
          172.23.251.18   172.29.200.25   
    Peer LDP Ident: 202.123.37.107:0; Local LDP Ident 116.119.39.45:0
	TCP connection: 202.123.37.107.22421 - 116.119.39.45.646
	State: Oper; Msgs sent/rcvd: 23706/24864; Downstream
	Up time: 2w0d
	LDP discovery sources:
	  GigabitEthernet0/1/0, Src IP addr: 172.23.251.17
	  Targeted Hello 116.119.39.45 -> 202.123.37.107, active, passive
        Addresses bound to peer LDP Ident:
          202.123.37.107  116.119.2.218   172.16.4.46     182.79.152.11   
          172.29.11.50    172.16.4.48     172.29.11.57    182.79.165.88   
          172.29.200.12   172.29.200.30   172.23.251.17   172.23.20.90    
          172.23.251.19   172.16.16.238   116.119.40.122  
KRL-NRK-MPL-T4-ACC-RTR-39-45#sh
KRL-NRK-MPL-T4-ACC-RTR-39-45#show int
KRL-NRK-MPL-T4-ACC-RTR-39-45#show interfaces tr
KRL-NRK-MPL-T4-ACC-RTR-39-45#show interfaces transceiver de
KRL-NRK-MPL-T4-ACC-RTR-39-45#show interfaces transceiver detail 
mA: milliamperes, dBm: decibels (milliwatts), NA or N/A: not applicable.
++ : high alarm, +  : high warning, -  : low warning, -- : low alarm.
A2D readouts (if they differ), are reported in parentheses.
The threshold values are calibrated.

                                High Alarm  High Warn  Low Warn   Low Alarm
             Temperature        Threshold   Threshold  Threshold  Threshold
Port         (Celsius)          (Celsius)   (Celsius)  (Celsius)  (Celsius)
---------    -----------------  ----------  ---------  ---------  ---------
Gi0/0/0      43.8                   89.0       85.0       -5.0       -9.0
Gi0/0/1      40.8                   89.0       85.0       -5.0       -9.0
Te0/0/8      39.9                   89.0       85.0       -5.0       -9.0
Gi0/1/0      41.7                   89.0       85.0       -5.0       -9.0
Te0/1/8      44.2                   98.0       96.0      -42.0      -43.0

                                High Alarm  High Warn  Low Warn   Low Alarm
             Voltage            Threshold   Threshold  Threshold  Threshold
Port         (Volts)            (Volts)     (Volts)    (Volts)    (Volts)
---------    -----------------  ----------  ---------  ---------  ---------
Gi0/0/0      3.25                   3.60       3.50       3.10       3.00
Gi0/0/1      3.27                   3.60       3.50       3.10       3.00
Te0/0/8      3.26                   3.60       3.50       3.10       3.00
Gi0/1/0      3.24                   3.60       3.50       3.10       3.00
Te0/1/8      3.25                   3.51       3.49       3.11       3.10

                                High Alarm  High Warn  Low Warn   Low Alarm
             Current            Threshold   Threshold  Threshold  Threshold
Port         (milliamperes)     (mA)        (mA)       (mA)       (mA)
---------    -----------------  ----------  ---------  ---------  ---------
Gi0/0/0       9.3                   60.0       50.0        1.0        0.5
Gi0/0/1       0.0                   60.0       50.0        1.0        0.5
Te0/0/8       0.0                   60.0       50.0        1.0        0.5
Gi0/1/0       9.9                   60.0       50.0        1.0        0.5
Te0/1/8       0.0                   65.0       60.0        5.5        4.5

             Optical            High Alarm  High Warn  Low Warn   Low Alarm
             Transmit Power     Threshold   Threshold  Threshold  Threshold
Port         (dBm)              (dBm)       (dBm)      (dBm)      (dBm)
---------    -----------------  ----------  ---------  ---------  ---------
Gi0/0/0      -5.6                    1.0       -3.0       -9.5      -13.5
Gi0/0/1       N/A                    1.0       -3.0       -9.5      -13.5
Te0/0/8       N/A                    1.0       -3.0       -9.5      -13.5
Gi0/1/0      -5.6                    1.0       -3.0       -9.5      -13.5
Te0/1/8       N/A                    0.5        0.0       -5.0       -5.5

             Optical            High Alarm  High Warn  Low Warn   Low Alarm
             Receive Power      Threshold   Threshold  Threshold  Threshold
Port         (dBm)              (dBm)       (dBm)      (dBm)      (dBm)
---------    -----------------  ----------  ---------  ---------  ---------
Gi0/0/0      -7.9                    1.0       -3.0      -19.0      -23.0
Gi0/0/1       N/A                    1.0       -3.0      -19.0      -23.0
Te0/0/8       N/A                    1.0       -3.0      -19.0      -23.0
Gi0/1/0      -9.3                    1.0       -3.0      -19.0      -23.0
Te0/1/8       N/A                   -4.0       -5.5      -35.2      -37.0


KRL-NRK-MPL-T4-ACC-RTR-39-45#show key chain
Key-chain bharti:
    key 100 -- text "btsol"
        accept lifetime (always valid) - (always valid) [valid now]
        send lifetime (always valid) - (always valid) [valid now]
KRL-NRK-MPL-T4-ACC-RTR-39-45#show ntp associations

  address         ref clock       st   when   poll reach  delay  offset   disp
 ~172.30.1.92     .STEP.          16      -   1024     0  0.000   0.000 15937.
*~202.56.230.29   172.30.1.92      3    791   1024   377  7.849  -2.981  1.071
 ~172.27.58.29    .STEP.          16      -   1024     0  0.000   0.000 15937.
 * sys.peer, # selected, + candidate, - outlyer, x falseticker, ~ configured
KRL-NRK-MPL-T4-ACC-RTR-39-45#show user
    Line       User       Host(s)              Idle       Location
*  2 vty 0     2366kri    idle                 00:00:00 61.95.140.252

  Interface    User               Mode         Idle     Peer Address

KRL-NRK-MPL-T4-ACC-RTR-39-45#show tacacs

Tacacs+ Server -  public  :
            Server address: 202.123.47.40
               Server port: 49
              Socket opens:        540
             Socket closes:        540
             Socket aborts:          0
             Socket errors:          0
           Socket Timeouts:          0
   Failed Connect Attempts:         50
        Total Packets Sent:        553
        Total Packets Recv:        299
             Server Status: Alive
Continous Authc fail count:          0
Continous Authz fail count:          2


Tacacs+ Server -  public  :
            Server address: 202.123.44.134
               Server port: 49
              Socket opens:         58
             Socket closes:         58
             Socket aborts:          0
             Socket errors:          0
           Socket Timeouts:          0
   Failed Connect Attempts:        165
        Total Packets Sent:          0
        Total Packets Recv:          0
             Server Status: Alive
Continous Authc fail count:          0
Continous Authz fail count:          0

KRL-NRK-MPL-T4-ACC-RTR-39-45#show access-list MPLS_Loopbacks
Standard IP access list MPLS_Loopbacks
    10 permit 63.218.164.7
    20 permit 63.218.144.13
    30 permit 202.123.47.0, wildcard bits 0.0.0.255 (187 matches)
    40 permit 202.123.37.0, wildcard bits 0.0.0.255 (222 matches)
    50 permit 125.62.169.0, wildcard bits 0.0.0.255
    60 permit 203.101.87.0, wildcard bits 0.0.0.255
    70 permit 125.62.160.128, wildcard bits 0.0.0.127
    80 permit 202.123.42.0, wildcard bits 0.0.0.255 (233 matches)
    90 permit 202.123.43.0, wildcard bits 0.0.0.255 (270 matches)
    100 permit 202.123.34.0, wildcard bits 0.0.0.255 (213 matches)
    110 permit 202.123.39.0, wildcard bits 0.0.0.255
    120 permit 116.119.39.0, wildcard bits 0.0.0.255 (5 matches)
    130 permit 172.23.20.0, wildcard bits 0.0.0.255 (6 matches)
KRL-NRK-MPL-T4-ACC-RTR-39-45#show interface desc
Interface                      Status         Protocol Description
Gi0/0/0                        up             up       #MPLS#BACK-TO-BACK##CONNECTED-TO-$KRL-MPL-LTE-PE-RTR-37-77$-$Gi0/0/0/5$##CMR:1680710#
Gi0/0/1                        admin down     down     
Gi0/0/2                        admin down     down     
Gi0/0/3                        admin down     down     
Gi0/0/4                        admin down     down     
Gi0/0/5                        admin down     down     
Gi0/0/6                        admin down     down     
Gi0/0/7                        admin down     down     
Te0/0/8                        admin down     down     
Gi0/1/0                        up             up       #MPLS#BACK-TO-BACK##CONNECTED-TO-$KRL-MPL-LTE-PE-RTR-37-77$-$Gi0/0/0/5$##CMR:1680710#
Gi0/1/1                        admin down     down     
Gi0/1/2                        admin down     down     
Gi0/1/3                        admin down     down     
Gi0/1/4                        admin down     down     
Gi0/1/5                        admin down     down     
Gi0/1/6                        admin down     down     
Gi0/1/7                        admin down     down     
Te0/1/8                        admin down     down     
Gi0                            down           down     
Lo0                            up             up       KRL-NRK-MPL-T4-ACC-RTR-39-45-Loopback0
KRL-NRK-MPL-T4-ACC-RTR-39-45#sh
KRL-NRK-MPL-T4-ACC-RTR-39-45#show  run int Gi0/0/0
Building configuration...

Current configuration : 529 bytes
!
interface GigabitEthernet0/0/0
 description #MPLS#BACK-TO-BACK##CONNECTED-TO-$KRL-MPL-LTE-PE-RTR-37-77$-$Gi0/0/0/5$##CMR:1680710#
 mtu 9216
 ip address 172.23.251.14 255.255.255.254
 ip router isis 
 load-interval 30
 carrier-delay msec 30
 negotiation auto
 mpls ip
 mpls label protocol ldp
 isis circuit-type level-2-only
 isis network point-to-point 
 isis metric 640 level-2
 isis authentication mode md5
 isis authentication key-chain bharti
 no isis hello padding always
 ip rsvp bandwidth
 ip rsvp signalling hello
end

KRL-NRK-MPL-T4-ACC-RTR-39-45#show  run int Gi0/0/0/0 1/0
Building configuration...

Current configuration : 529 bytes
!
interface GigabitEthernet0/1/0
 description #MPLS#BACK-TO-BACK##CONNECTED-TO-$KRL-MPL-LTE-PE-RTR-37-77$-$Gi0/0/0/5$##CMR:1680710#
 mtu 9216
 ip address 172.23.251.16 255.255.255.254
 ip router isis 
 load-interval 30
 carrier-delay msec 30
 negotiation auto
 mpls ip
 mpls label protocol ldp
 isis circuit-type level-2-only
 isis network point-to-point 
 isis metric 640 level-2
 isis authentication mode md5
 isis authentication key-chain bharti
 no isis hello padding always
 ip rsvp bandwidth
 ip rsvp signalling hello
end

KRL-NRK-MPL-T4-ACC-RTR-39-45#show  run int Gi0/1/0 0/0 un int Gi0/0/0  int Gi0/0/0  int Gi0/0/0 int Gi0/0/0   int Gi0/0/0 hssho  int Gi0/0/0login as: ciscopartner
Pre-authentication banner message from server:
| *****************************************************************************
> ***********************
| -----------------------------------------------------------------------------
> -----------------------
| 
|                                            CSP Collector
| 
| Please use below url to access CSP Collector appliance GUI
| IPv4 URL : https://192.168.1.100:8001
| 
| -----------------------------------------------------------------------------
> -----------------------
| *****************************************************************************
> ***********************
End of banner message from server
Keyboard-interactive authentication prompts from server:
| Password: 
End of keyboard-interactive prompts from server
