import sys
import os
import json
import joblib
import pandas as pd
import numpy as np

def main():
    print("=" * 85)
    print("SubAero 100% White-Box Direct Telemetry Predictor")
    print("Degree-2 Regularized Polynomial Closed-Form Algebraic Equations (0% Black-Box)")
    print("Exact Input Format: Altitude_m, Mach, Tamb_K, Pamb_Pa, RPM_rev_min, FuelFlow_kg_s, P2_Pa, T2_K, P3_Pa, T3_K, P4_Pa, T4_K")
    print("=" * 85)

    defaults = [10000.0, 0.80, 223.25, 26500.0, 55000.0, 2.85, 40000.0, 250.0, 1200000.0, 750.0, 1150000.0, 1100.0]

    if len(sys.argv) > 1:
        raw_str = " ".join(sys.argv[1:])
    else:
        print("\nEnter your 12 sensor values separated by commas or spaces:")
        print("Example: 10000, 0.8, 223.25, 26500, 55000, 2.85, 40000, 250, 1200000, 750, 1150000, 1100")
        try:
            raw_str = input("\n12 Telemetry Inputs > ").strip()
        except Exception:
            raw_str = ""

    if raw_str:
        raw_tokens = [t.strip() for t in raw_str.replace(',', ' ').split() if t.strip()]
        
        # Auto De-duplication: filter out duplicate adjacent values
        deduped_tokens = []
        for tok in raw_tokens:
            try:
                v = float(tok)
                if not deduped_tokens or abs(v - float(deduped_tokens[-1])) > 1e-4:
                    deduped_tokens.append(tok)
            except ValueError:
                deduped_tokens.append(tok)

        vals = []
        for i in range(len(defaults)):
            if i < len(deduped_tokens):
                try:
                    vals.append(float(deduped_tokens[i]))
                except ValueError:
                    vals.append(defaults[i])
            else:
                vals.append(defaults[i])
    else:
        vals = defaults

    alt, mach, tamb, pamb, rpm, ff, p2, t2, p3, t3, p4, t4 = vals

    # Range safety swap detection
    if ff > 100 and rpm < 100:
        ff, rpm = rpm, ff
    if p2 < 10.0 and t2 > 1000.0:
        p2, t2 = t2, p2

    cols12 = ['Altitude_m', 'Mach', 'Tamb_K', 'Pamb_Pa', 'RPM_rev_min', 'FuelFlow_kg_s', 'P2_Pa', 'T2_K', 'P3_Pa', 'T3_K', 'P4_Pa', 'T4_K']
    df_12 = pd.DataFrame([{
        'Altitude_m': alt,
        'Mach': mach,
        'Tamb_K': tamb,
        'Pamb_Pa': pamb,
        'RPM_rev_min': rpm,
        'FuelFlow_kg_s': ff,
        'P2_Pa': p2,
        'T2_K': t2,
        'P3_Pa': p3,
        'T3_K': t3,
        'P4_Pa': p4,
        'T4_K': t4
    }])[cols12]

    wb_dir = 'trained_models_whitebox_12s'
    if not os.path.exists(wb_dir):
        wb_dir = 'trained_models'

    predictions = {}
    targets = ['OverallHealth', 'CompressorHealth', 'CombustorHealth', 'TurbineHealth', 'Thrust_N', 'TSFC_g_N_s']

    for t in targets:
        model_path = os.path.join(wb_dir, f'{t}.joblib')
        if os.path.exists(model_path):
            m = joblib.load(model_path)
            val_raw = float(m.predict(df_12)[0])
            val = min(0.9999, max(0.10, val_raw)) if 'Health' in t else max(0, val_raw)
            predictions[t] = val

    print("\n" + "=" * 85)
    print("100% WHITE-BOX PREDICTION RESULTS (Degree-2 Polynomial Closed-Form Equations):")
    print("=" * 85)
    print(f"  Inputs: Alt={alt}m, Mach={mach}, Tamb={tamb}K, Pamb={pamb}Pa, RPM={rpm}, Fuel={ff}kg/s, P2={p2}Pa, T2={t2}K, P3={p3}Pa, T3={t3}K, P4={p4}Pa, T4={t4}K")
    print("-" * 85)
    print(f"  1. OVERALL HEALTH    : {predictions['OverallHealth'] * 100:.2f}%  (Health Index: {predictions['OverallHealth']:.4f})")
    print(f"  2. COMPRESSOR HEALTH : {predictions['CompressorHealth'] * 100:.2f}%  (Health Index: {predictions['CompressorHealth']:.4f})")
    print(f"  3. COMBUSTOR HEALTH  : {predictions['CombustorHealth'] * 100:.2f}%  (Health Index: {predictions['CombustorHealth']:.4f})")
    print(f"  4. TURBINE HEALTH    : {predictions['TurbineHealth'] * 100:.2f}%  (Health Index: {predictions['TurbineHealth']:.4f})")
    print(f"  5. THRUST FORCE      : {predictions['Thrust_N']:.2f} N")
    print(f"  6. FUEL TSFC         : {predictions['TSFC_g_N_s']:.6f} g/(N*s)")
    print("=" * 85 + "\n")

if __name__ == '__main__':
    main()
