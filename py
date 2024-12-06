#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np

# Function Definitions
def workload_calculation():
    """
    Calculate the workload for the Linac room.
    """
    print("\n--- Workload Calculations ---\n")
    try:
        pa = float(input("Enter the number of patients per day: "))
        gy = float(input("Enter the dose per patient (Gy): "))
        we = float(input("Enter the number of days per week: "))
        w1 = float(input("Enter the fraction of workload (leakage): "))
        wt = float(input("Enter the total number of weeks: "))
        qc = float(input("Enter the quality control percentage: "))
        
        ww = pa * gy * we * w1 * wt  # Raw workload without QC
        qc1 = (qc / 100) * ww         # Additional workload due to QC
        w = ww + qc1                  # Total workload
        
        print(f"\nThe total workload is: {w:.2f} Gy/week\n")
        return w
    except ValueError:
        print("Invalid input. Please enter numeric values.")
        return None

def primary_shielding(w):
    """
    Calculate the thickness of the primary shielding barrier.
    """
    print("\n--- Primary Shielding ---\n")
    try:
        p1 = float(input("Enter the shielding design dose 'P' (Sv/year): "))
        T = float(input("Enter the occupancy factor 'T': "))
        U = float(input("Enter the use factor 'U': "))
        d = float(input("Enter the distance from the primary beam source 'd' (m): "))
        TVL1 = float(input("Enter the first tenth-value layer (TVL1) for the primary barrier: "))
        TVLe = float(input("Enter the subsequent tenth-value layers (TVLe): "))
        
        D = d ** 2
        B = (p1 * D) / (w * T * U)
        n = -np.log10(B)
        thickness = TVL1 + ((n - 1) * TVLe)
        
        print(f"The primary shielding thickness is: {thickness:.2f} cm\n")
    except ValueError:
        print("Invalid input. Please enter numeric values.")

def secondary_shielding(w, ww):
    """
    Calculate the thickness of the secondary shielding barrier.
    """
    print("\n--- Secondary Shielding ---\n")
    try:
        fww = float(input("Enter the workload factor for VMAT or IMRT (%): "))
        p1 = float(input("Enter the shielding design dose 'P' (Sv/year): "))
        T = float(input("Enter the occupancy factor 'T': "))
        L = float(input("Enter the leakage factor 'L': "))
        d = float(input("Enter the distance from the primary beam source 'd' (m): "))
        TVL1 = float(input("Enter the first tenth-value layer (TVL1) for the secondary barrier: "))
        TVLe = float(input("Enter the subsequent tenth-value layers (TVLe): "))
        
        fw = (fww / 100) * ww  # Adjusted workload for VMAT/IMRT
        new_workload = ww + fw
        D = d ** 2
        B = (p1 * D) / (new_workload * T * L)
        n = -np.log10(B)
        thickness = TVL1 + ((n - 1) * TVLe)
        
        print(f"The secondary shielding thickness is: {thickness:.2f} cm\n")
    except ValueError:
        print("Invalid input. Please enter numeric values.")

def shielding_calculations(w, ww):
    """
    Handle shielding calculations based on user input.
    """
    print("\n--- Shielding Calculations ---\n")
    energy = input("Choose the energy (6MV, 10MV, 15MV, 18MV): ").strip()
    if energy not in {"6MV", "10MV", "15MV", "18MV"}:
        print("Invalid energy selection.")
        return

    print("\nAvailable Shielding Types:")
    print("1 --> Primary shielding")
    print("2 --> Secondary shielding")
    # Placeholder for future implementations
    print("3 --> Scatter from Patient Shielding Calculations (Coming Soon)")
    print("4 --> Scatter of the Primary Beam from the Bunker Wall (Coming Soon)")
    print("5 --> Scatter from the Patient (Coming Soon)")
    print("6 --> Scatter of Head Leakage Radiation from the Bunker Walls (Coming Soon)")
    print("7 --> Transmission of Head Leakage Radiation through the Maze Wall (Coming Soon)")
    print("8 --> Total dose rate at the maze entrance and door shielding (Coming Soon)")
    
    types = input("Choose the type of shielding (1-8): ").strip()
    if types == "1":
        primary_shielding(w)
    elif types == "2":
        secondary_shielding(w, ww)
    else:
        print("This shielding type is not yet implemented. Stay tuned!")

# Main Program
def main():
    print("Welcome to the Linac Room Shielding Calculator")
    workload = workload_calculation()
    if workload:
        shielding_calculations(workload, workload)

if __name__ == "__main__":
    main()
