#ASTRA (AIR SHEILDING & THREAT RESPONSE ALGORITHM) VERSION 1.0

import time
import random

print("Initializing Radar System...")
time.sleep(3)
print("Scanning airspace for unidentified objects...\n")
time.sleep(3)

#simulating radar detections
threat_detected = random.choice([True, False])
if threat_detected:
    print("ALERT: Incoming Missile Detected!!")
    time.sleep(1.5)

    #threat level
    threat_level = random.choice(["LOW", "MEDIUM", "HIGH", "CRITICAL"])
    print(f"AI Analysis Complete: Threat Level = {threat_level}")
    time.sleep(1)

    if threat_level in ["HIGH", "CRITICAL"]:
        print("\nAttemptting to lock on target...")
        time.sleep(2)
        lock_success = random.choice([True])

        if lock_success:
            print("Target LOCKED successfully.")
            time.sleep(1)
            print("\nRequesting Permission to Launch Defence MIssile...")
            time.sleep(1)
            permission = input("Grant Permission? (yes/no): ").strip().lower()

            if permission == "yes":
                print("\nPermission Granted. Launching Missile Interceptor...")
                for i in range(5,0,-1):
                    print(f"Launching in {1}...")
                    time.sleep(1)
                    print("Interceptor Launched. Tracking Missile...")
                    time.sleep(2)
                    print("Target Neutralized. Airspace Secure.")
            else:
                print("\nPermission Denied. No Action Taken.") 
                print("WARNING! Enemy missile may breach defence.")
        else:
            print("Lock Failed. Unable to track target")  
            print("Suggest activating manual defence mode.")   

    else:
        print("LOW threat level. Monitoring continues...")  
        time.sleep(1.5)      
        print("Situation under control.")   

else:
    print("No threats detected Airspace is clear.")               

input("\npress enter to exit...")
