Router#show platform 
Chassis type: ASR1002             

Slot      Type                State                 Insert time (ago) 
—------- —---------------— —------------------- —--------------- 
0         ASR1002-SIP10       ok                    00:19:49      
 0/0      4XGE-BUILT-IN       ok                    00:16:08      
R0        ASR1002-RP1         ok, active            00:19:49      
F0        ASR1000-ESP5        init, active          00:19:49      
P0        ASR1002-PWR-AC      ok                    00:19:05      
P1        ASR1002-PWR-AC      ps, fail              00:19:04      

Slot      CPLD Version        Firmware Version                        
—------- —---------------— —------------------------------------- 
0         07120202            12.2(33r)XNC                        
R0        08011017            12.2(33r)XNC                        
F0        07091401            12.2(33r)XNB

# Problem
F0        ASR1000-ESP5        init, active          00:19:49 

# fixed by
hw-module slot F0 reload
reload

# after fixed
Router#show platform               
Chassis type: ASR1002             

Slot      Type                State                 Insert time (ago) 
—------- —---------------— —------------------- —--------------- 
0         ASR1002-SIP10       ok                    00:08:40      
 0/0      4XGE-BUILT-IN       ok                    00:07:06      
R0        ASR1002-RP1         ok, active            00:08:40      
F0        ASR1000-ESP5        ok, active            00:08:40      
P0        ASR1002-PWR-AC      ok                    00:07:51      
P1        ASR1002-PWR-AC      ps, fail              00:07:50      

Slot      CPLD Version        Firmware Version                        
—------- —---------------— —------------------------------------- 
0         07120202            12.2(33r)XNC                        
R0        08011017            12.2(33r)XNC                        
F0        07091401            12.2(33r)XNB