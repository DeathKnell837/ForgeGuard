# Changelog: model input size changed from 128 x 128 to 224 x 224 (October 22, 2026)

This note is for anyone working on this repository later, including an AI coding assistant. Read it before changing preprocessing, the models or the reported numbers.

## Summary

- Every CNN input in the system is now **224 x 224 x 3** (ELA image, quality 90, scale 15, normalized to 0-1). It was 128 x 128.
- All three models (Basic CNN, MobileNetV2, ResNet50) were **retrained at 224 x 224** with the repository's own training code, dataset and split. The old 128 x 128 model files were replaced at the same paths, in the same `.keras` format.
- The benchmark JSON the app reads was regenerated from the new models, and the README and model specification tables now show the new numbers.
- **Do not change the input size back to 128.** The approved manuscript specifies 224 x 224.

## Why it changed

- The manuscript (`thesis-docs/THESIS1UNGAB_BACANTO.docx`, Image Preprocessing) and its architecture diagram specify resizing each receipt to **224 x 224 pixels** and normalizing to 0-1, the standard input resolution of the ImageNet-pretrained MobileNetV2 and ResNet50.
- The code had drifted to 128 x 128: the training notebooks used `IMG_SIZE = (128, 128)`, so the deployed models were trained at 128, and the app showed "128x128 ELA Target" and "Input Target: 128 x 128 px".
- The thesis review caught the mismatch between the manuscript and the system. The system was aligned to the approved manuscript ahead of the conformity-of-revisions signature.
- The models had to be retrained, not just relabeled: the Basic CNN's dense layer is sized to the flattened feature map, so a model trained at 128 cannot take a 224 input.

## How the models were retrained

- Script: `thesis-system/training/train.py` (the same pipeline as `ForgeGuard_Model_Training.ipynb`, which trained the previous models).
- Dataset: `thesis-system/dataset`, the same balanced quota selection as before: 227 authentic and 228 forged receipts (455 total), plus 621 unseen forgeries kept out as a stress-test holdout.
- Split: 70/15/15 stratified, `random_state=42`. Train 318, validation 68, test 69 (34 authentic, 35 forged).
- Same hyperparameters as the previous models: 20 epochs, batch size 16, Adam with default settings (lr 0.001), binary cross-entropy, ImageNet weights frozen for MobileNetV2 and ResNet50. The only change is the input size.
- Seed fixed with `tf.keras.utils.set_random_seed(42)`.
- Trained on CPU (TensorFlow 2.21, Keras 3.15). Model files are saved without optimizer state, because the app loads them with `compile=False`. That keeps `basic_cnn.keras` (11.2M parameters at 224) at about 45 MB instead of 134 MB, under GitHub's 100 MB file limit.
- After training, `thesis-system/evaluate_balanced_5seeds.py` was rerun to regenerate the benchmark JSON the app displays.

## New results vs old

### 5-seed balanced evaluation (what the app shows)

`thesis-system/evaluate_balanced_5seeds.py`: seeds 42, 101, 202, 303, 404; N = 225 per seed (112 authentic, 56 edited, 57 AI-generated). Mean values.

| Model | Condition | Accuracy (old 128 -> new 224) | Precision | Recall | F1-score | Latency (new) |
|:---|:---|:---|:---|:---|:---|:---|
| Basic CNN | Standard | 91.82% -> **94.58%** (+/- 0.99) | 98.16% -> **100.00%** | 85.31% -> **89.20%** | 91.25% -> **94.28%** | 52.28 ms |
| MobileNetV2 | Standard | 82.22% -> **82.93%** (+/- 1.53) | 78.57% -> **94.53%** | 89.03% -> **70.09%** | 83.44% -> **80.47%** | 56.21 ms |
| ResNet50 | Standard | 53.42% -> **49.78%** (+/- 0.00) | 51.89% -> **0.00%** | 100.00% -> **0.00%** | 68.32% -> **0.00%** | 79.11 ms |
| Basic CNN | Compressed | 91.73% -> **96.36%** (+/- 1.03) | 98.57% -> **100.00%** | 84.78% -> **92.74%** | 91.12% -> **96.22%** | 34.25 ms |
| MobileNetV2 | Compressed | 87.82% -> **89.87%** (+/- 1.33) | 88.50% -> **100.00%** | 87.08% -> **79.82%** | 87.78% -> **88.76%** | 38.48 ms |
| ResNet50 | Compressed | 49.24% -> **49.78%** (+/- 0.00) | 49.72% -> **0.00%** | 93.98% -> **0.00%** | 65.03% -> **0.00%** | 61.34 ms |

### Held-out test split from training

`train.py` test split: N = 69 (34 authentic, 35 forged). Unseen holdout: 621 forgeries never used in training. Old values are the 128 x 128 run in `thesis-system/models/colab_run/`.

| Model | Accuracy (old -> new) | Precision | Recall | F1-score | Latency (new) | Unseen holdout recall (old -> new) |
|:---|:---|:---|:---|:---|:---|:---|
| Basic CNN | 98.55% -> **97.10%** | 100.00% -> **100.00%** | 97.14% -> **94.29%** | 98.55% -> **97.06%** | 9.10 ms | 89.21% -> **84.70%** |
| MobileNetV2 | 92.75% -> **95.65%** | 96.88% -> **97.06%** | 88.57% -> **94.29%** | 92.54% -> **95.65%** | 35.17 ms | 66.99% -> **72.30%** |
| ResNet50 | 52.17% -> **49.28%** | 51.47% -> **0.00%** | 100.00% -> **0.00%** | 67.96% -> **0.00%** | 63.74 ms | 99.03% -> **0.00%** |

The split metrics are saved in `thesis-system/models/train_split_metrics_224.json`.

### Notes on the results

- **Basic CNN** is still the best model, and its benchmark accuracy went up from 91.82% to 94.58%.
- **ResNet50** with a frozen ImageNet base does not learn the ELA signal at either size. At 128 it called almost everything Forged; at 224 it calls everything Authentic. Either way it is near 50% accuracy, which is chance level for this balanced test.
- **Latency is not comparable** with the old numbers: the new numbers were measured on the retraining machine's CPU, not on the fixed benchmark machine the manuscript describes. Re-measure on that machine before reporting latency or memory.
- The 5-seed benchmark draws its test sets from the full dataset pool, so it includes some receipts the models were trained on. The `train.py` test split and the unseen holdout have no such overlap.

## Files changed

Models and metrics:
- `thesis-system/models/basic_cnn.keras`, `mobilenetv2.keras`, `resnet50.keras`: retrained at 224 (input shape `(None, 224, 224, 3)`).
- `models/*.keras` (root copy): the same three files.
- `thesis-system/models/evaluation_metrics.json`, `models/evaluation_metrics.json`, `01_System_Prototype/03_Prototype_Files/evaluation_metrics.json`: regenerated 5-seed benchmark.
- `thesis-system/models/train_split_metrics_224.json` (new): `train.py` test-split and holdout metrics.

Code:
- `thesis-system/training/train.py` and its copy `01_System_Prototype/05_Other_Development_Files/train.py`: 224 (it already said 224), 20 epochs to match how the deployed models were trained (was 50, within the manuscript's 50-epoch ceiling), fixed seed 42, optimizer state stripped on save.
- `thesis-system/training/ForgeGuard_Model_Training.ipynb`, `thesis-system/ForgeGuard_Model_Training.ipynb`, `01_System_Prototype/05_Other_Development_Files/ForgeGuard_Model_Training.ipynb`, `thesis-system/training/ForgeGuard_Full_Dataset_Colab.ipynb`: `IMG_SIZE` and model input shapes 128 -> 224.
- `thesis-system/webapp/app.py` and `01_System_Prototype/01_Source_Code/app.py`: UI labels now read "224x224 ELA Target" and "Input Target: 224 x 224 px"; Basic CNN parameter label ~3.3M -> ~11.2M. Inference already reads the size from the loaded model, so it now uses 224.
- `thesis-system/evaluate_balanced_5seeds.py` and its copy in `01_System_Prototype/05_Other_Development_Files/`: Basic CNN parameter label -> ~11.2M.
- `preprocessing/ela.py` (`convert_ela_to_array` default) and `preprocessing/cnn_inference.py` (root legacy modules): 128 -> 224. `thesis-system/preprocessing/ela.py` already used 224.
- `thesis-system/tests/test_batch_evaluation.py`: fallback size 128 -> 224.

Docs:
- `README.md`, `thesis-system/README.md`: benchmark tables, badges and model summaries use the new numbers, and link to this file.
- `01_System_Prototype/03_Prototype_Files/MODEL_SPECIFICATIONS.md`: parameter counts at 224 and new results tables. The old table there (98.5%, 98.0%, 97.5% and so on) did not come from any model in this repository and was removed.
- `01_System_Prototype/README.md`: Basic CNN summary line.
- `thesis-docs/Chapter3_System_Architecture_and_Methodology.md`, `thesis-docs/FORGEGUARD_MASTER_DEFENSE_GUIDE.md`, `thesis-docs/forgeguard_lucidchart_import.txt`, `01_System_Prototype/06_Screenshots_with_Descriptions/SCREENSHOT_DESCRIPTIONS.md`: 128 -> 224 where the input size is mentioned.
- `thesis-system/models/colab_run/README.md`: marked as a superseded 128 x 128 record.

Left as they were on purpose:
- `thesis-system/webapp_backup_*` folders: old snapshots, not used by the app.
- `thesis-system/models/colab_run/` and the two `pure_empirical_benchmark.json` files: records of the old 128 x 128 run.
- `thesis-system/preprocessing/ela.py`'s other numbers containing 128 (filter counts, colors) are unrelated to input size.

## What the manuscript needs

- The approved manuscript already says 224 x 224, so its methodology needs no change.
- The current manuscript is the proposal (Chapters 1-2) and has no results tables yet. When the results chapter is written, use the 224 numbers above, not the old 128 numbers (91.82% for Basic CNN, 82.22% for MobileNetV2, 53.42% for ResNet50).
- Anything else that quotes the old numbers (slides, the defense guide, a poster) must be updated to the new ones.
- Report Basic CNN as about 11.2M parameters at 224 x 224, not 2.1M or 3.3M.

## Checked after the change

- The Streamlit app was run locally with the new models. All three models loaded at input shape 224 x 224 with no errors.
- Authentic benchmark sample (`authentic_0001.jpg`): Basic CNN Authentic (100.0%), MobileNetV2 Authentic (88.3%), ResNet50 Authentic (53.4%).
- Edited benchmark sample (`forged_amount_0001.jpg`): Basic CNN Forged (100.0%), MobileNetV2 Forged (74.2%), ResNet50 Authentic (53.2%).
