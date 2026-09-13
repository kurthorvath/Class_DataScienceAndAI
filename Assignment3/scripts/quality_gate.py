import json
import os
import sys
from pathlib import Path

metrics_file = Path(
    os.environ.get(
        "MODEL_METRICS_FILE",
        "artifacts/model_v2_test_C.json"
    )
)
accuracy_threshold = float(os.environ.get("ACCURACY_THRESHOLD", "0.80"))
f1_threshold = float(os.environ.get("F1_THRESHOLD", "0.80"))

if not metrics_file.exists():
    print(f"ERROR: Metrics file not found: {metrics_file}")
    sys.exit(1)

metrics = json.loads(metrics_file.read_text())
accuracy = float(metrics["accuracy"])
f1 = float(metrics["f1"])

print("Quality Gate")
print("------------")
print(f"Metrics file:       {metrics_file}")
print(f"Accuracy:           {accuracy:.4f}")
print(f"Accuracy threshold: {accuracy_threshold:.4f}")
print(f"F1:                 {f1:.4f}")
print(f"F1 threshold:       {f1_threshold:.4f}")

accuracy_ok = accuracy >= accuracy_threshold
f1_ok = f1 >= f1_threshold

if accuracy_ok and f1_ok:
    print("")
    print("QUALITY GATE PASSED")
    print("Model is approved.")
    sys.exit(0)

print("")
print("QUALITY GATE FAILED")
if not accuracy_ok:
    print(f"Accuracy {accuracy:.4f} is below threshold {accuracy_threshold:.4f}")
if not f1_ok:
    print(f"F1 {f1:.4f} is below threshold {f1_threshold:.4f}")
sys.exit(1)
