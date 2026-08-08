import os
import json
import joblib
import numpy as np
import pandas as pd

def run_interactive_tester():
    print("=" * 80)
    print("SubAero: Interactive Telemetry Test Console")
    print("Choose input option:")
    print("  [1] Enter custom sensor telemetry manually")
    print("  [2] Select a real engine cycle row from held-out test.csv")
    print("=" * 80)

    test_path = 'backend/digital_twin/data/test.csv'
    gt_path = 'backend/digital_twin/data/ground_truth.csv'
    if not os.path.exists(test_path):
        test_path = 'public/dataset/train.csv'
        gt_path = 'public/dataset/ground_truth.csv'

    test_df = pd.read_csv(test_path).merge(pd.read_csv(gt_path), on=['EngineID', 'Cycle'])

    try:
        opt = input("Select Option [1/2] (default: 2): ").strip()
    except Exception:
        opt = "2"

    if opt == "1":
        defaults = {
            'Altitude_m': 10000.0,
            'Mach': 0.80,
            'Tamb_K': 223.25,
            'Pamb_Pa': 26500.0,
            'RPM_rev_min': 55000.0,
            'FuelFlow_kg_s': 2.85,
            'P2_Pa': 40000.0,
            'T2_K': 250.0,
            'P3_Pa': 1200000.0,
            'T3_K': 750.0,
            'P4_Pa': 1150000.0,
            'T4_K': 1100.0,
            'Cycle': 150
        }
        user_inputs = {}
        print("\n--- Custom Telemetry Input ---")
        for key, def_val in defaults.items():
            try:
                val_str = input(f"Enter {key:15s} [default: {def_val}]: ").strip()
                user_inputs[key] = float(val_str) if val_str else float(def_val)
            except Exception:
                user_inputs[key] = float(def_val)
        df_input = pd.DataFrame([user_inputs])
        true_labels = None
    else:
        sample_idx = 50
        try:
            row_num_str = input(f"Enter row index from test.csv [0-{len(test_df)-1}] (default: 50): ").strip()
            sample_idx = int(row_num_str) if row_num_str else 50
        except Exception:
            sample_idx = 50
        
        sample_row = test_df.iloc[sample_idx]
        features_all = ['Altitude_m', 'Mach', 'Tamb_K', 'Pamb_Pa', 'RPM_rev_min', 'FuelFlow_kg_s', 'P2_Pa', 'T2_K', 'P3_Pa', 'T3_K', 'P4_Pa', 'T4_K', 'Cycle']
        user_inputs = {k: float(sample_row[k]) for k in features_all}
        df_input = pd.DataFrame([user_inputs])
        
        true_labels = {
            'OverallHealth': float(sample_row['OverallHealth']),
            'CompressorHealth': float(sample_row['CompressorHealth']),
            'CombustorHealth': float(sample_row['CombustorHealth']),
            'TurbineHealth': float(sample_row['TurbineHealth']),
            'Thrust_N': float(sample_row['Thrust_N']),
            'TSFC_g_N_s': float(sample_row['TSFC_g_N_s'])
        }

    print("\n" + "=" * 80)
    print("INPUT TELEMETRY POINT:")
    print("-" * 80)
    for k, v in user_inputs.items():
        print(f"  * {k:15s} : {v}")

    if true_labels:
        print("\n" + "=" * 80)
        print("GROUND TRUTH ACTUAL VALUES (from test.csv):")
        print("-" * 80)
        for k, v in true_labels.items():
            if 'Health' in k:
                print(f"  * {k:18s} : {v * 100:.2f}%  (Actual Index: {v:.4f})")
            elif k == 'Thrust_N':
                print(f"  * {k:18s} : {v:.2f} N")
            else:
                print(f"  * {k:18s} : {v:.6f} g/(N*s)")

    wb_dir = 'trained_models'
    heavy_dir = 'trained_models/heavy_ensemble'
    feat_cols_path = os.path.join(wb_dir, 'feature_columns.json')
    with open(feat_cols_path) as f:
        feature_columns_list = json.load(f)

    targets = ['CompressorHealth', 'CombustorHealth', 'TurbineHealth', 'OverallHealth', 'Thrust_N', 'TSFC_g_N_s']

    print("\n" + "=" * 80)
    print("1. POLYNOMIAL RIDGE MODEL PREDICTIONS (100% White-Box):")
    print("-" * 80)

    wb_preds = {}
    X_wb = df_input[feature_columns_list]

    for t in targets:
        model_path = os.path.join(wb_dir, f'{t}.joblib')
        if os.path.exists(model_path):
            model = joblib.load(model_path)
            val_raw = float(model.predict(X_wb)[0])
            val = min(0.9999, max(0.10, val_raw)) if 'Health' in t else max(0, val_raw)
            wb_preds[t] = val
            
            err_str = ""
            if true_labels:
                actual = true_labels[t]
                err = abs(val - actual)
                acc = max(0, 100 * (1 - err)) if t != 'Thrust_N' else max(0, 100 * (1 - err / 60000.0))
                err_str = f" | Error: {err:.4f} | Row Accuracy: {acc:.2f}%"

            if 'Health' in t:
                print(f"  * {t:18s} : {val * 100:.2f}%{err_str}")
            elif t == 'Thrust_N':
                print(f"  * {t:18s} : {val:.2f} N{err_str}")
            else:
                print(f"  * {t:18s} : {val:.6f} g/(N*s){err_str}")

    print("\n" + "=" * 80)
    print("2. HEAVY ML ENSEMBLE PREDICTIONS (LightGBM + XGBoost + CatBoost + ExtraTrees + Ridge):")
    print("-" * 80)

    heavy_preds = {}
    features_health = ['Altitude_m', 'Mach', 'Tamb_K', 'Pamb_Pa', 'RPM_rev_min', 'FuelFlow_kg_s', 'P2_Pa', 'T2_K', 'P3_Pa', 'T3_K', 'P4_Pa', 'T4_K', 'Cycle']
    features_perf   = ['Altitude_m', 'Mach', 'Tamb_K', 'Pamb_Pa', 'RPM_rev_min', 'FuelFlow_kg_s', 'P2_Pa', 'T2_K', 'P3_Pa', 'T3_K', 'P4_Pa', 'T4_K']

    for t in targets:
        is_health = 'Health' in t
        X_ens = df_input[features_health if is_health else features_perf]
        
        lgb_path = os.path.join(heavy_dir, f'{t}_lgb.joblib')
        if os.path.exists(lgb_path):
            p_lgb = float(joblib.load(os.path.join(heavy_dir, f'{t}_lgb.joblib')).predict(X_ens)[0])
            p_xgb = float(joblib.load(os.path.join(heavy_dir, f'{t}_xgb.joblib')).predict(X_ens)[0])
            p_cb  = float(joblib.load(os.path.join(heavy_dir, f'{t}_cb.joblib')).predict(X_ens)[0])
            p_et  = float(joblib.load(os.path.join(heavy_dir, f'{t}_et.joblib')).predict(X_ens)[0])
            p_ridge = wb_preds[t]

            val_raw = 0.25 * p_lgb + 0.25 * p_xgb + 0.25 * p_cb + 0.15 * p_et + 0.10 * p_ridge
            val = min(0.9999, max(0.10, val_raw)) if 'Health' in t else max(0, val_raw)
            heavy_preds[t] = val

            err_str = ""
            if true_labels:
                actual = true_labels[t]
                err = abs(val - actual)
                acc = max(0, 100 * (1 - err)) if t != 'Thrust_N' else max(0, 100 * (1 - err / 60000.0))
                err_str = f" | Error: {err:.4f} | Row Accuracy: {acc:.2f}%"

            if 'Health' in t:
                print(f"  * {t:18s} : {val * 100:.2f}%{err_str}")
            elif t == 'Thrust_N':
                print(f"  * {t:18s} : {val:.2f} N{err_str}")
            else:
                print(f"  * {t:18s} : {val:.6f} g/(N*s){err_str}")

    print("=" * 80 + "\n")

if __name__ == '__main__':
    run_interactive_tester()
