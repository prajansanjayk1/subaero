import pandas as pd
import numpy as np
import joblib
import json
import os
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
import warnings
warnings.filterwarnings('ignore')

def run_evaluation():
    # Load dataset
    train_path = 'backend/digital_twin/data/train.csv'
    test_path = 'backend/digital_twin/data/test.csv'
    ground_truth_path = 'backend/digital_twin/data/ground_truth.csv'

    if not os.path.exists(train_path):
        train_path = 'public/dataset/train.csv'
        test_path = 'public/dataset/test.csv'
        ground_truth_path = 'public/dataset/ground_truth.csv'

    test_df = pd.read_csv(test_path).merge(pd.read_csv(ground_truth_path), on=['EngineID', 'Cycle'])

    targets = ['CompressorHealth', 'CombustorHealth', 'TurbineHealth', 'OverallHealth', 'Thrust_N', 'TSFC_g_N_s']
    cols12 = ['Altitude_m', 'Mach', 'Tamb_K', 'Pamb_Pa', 'RPM_rev_min', 'FuelFlow_kg_s', 'P2_Pa', 'T2_K', 'P3_Pa', 'T3_K', 'P4_Pa', 'T4_K']

    wb_dir = 'trained_models_whitebox_12s'
    if not os.path.exists(wb_dir):
        wb_dir = 'trained_models'

    print('=' * 95)
    print(f'100% WHITE-BOX MODEL ACCURACY EVALUATION MATRIX ON HELD-OUT TEST DATA ({len(test_df)} CYCLES across 20 UNSEEN ENGINES):')
    print('=' * 95)

    X_te = test_df[cols12]

    for t in targets:
        y_te = test_df[t]
        model_path = os.path.join(wb_dir, f'{t}.joblib')
        if os.path.exists(model_path):
            model = joblib.load(model_path)
            preds = model.predict(X_te)
            
            mae = mean_absolute_error(y_te, preds)
            rmse = np.sqrt(mean_squared_error(y_te, preds))
            r2 = r2_score(y_te, preds)
            acc = max(0, 100 * (1 - mae)) if t != 'Thrust_N' else max(0, 100 * (1 - mae / 60000.0))
            print(f'  {t:18s} | MAE: {mae:.6f} | RMSE: {rmse:.6f} | R2: {r2:.4f} | Accuracy: {acc:.2f}%')

    print('=' * 95)

if __name__ == '__main__':
    run_evaluation()
