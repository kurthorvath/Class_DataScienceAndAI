import json
import os
import sys
from pathlib import Path

# TODO 1:
# Read the metrics file path from the METRICS_FILE environment variable.
# Use "artifacts/monitor_metrics.json" as the default path.
metrics_file = Path("TODO")

# TODO 2:
# Read BASELINE_ACCURACY from the environment.
# Use 0.892 as the default.
baseline_accuracy = float("TODO")

# TODO 3:
# Read ALLOWED_ACCURACY_DROP from the environment.
# Use 0.10 as the default.
allowed_drop = float("TODO")

if not metrics_file.exists():
    print(f"ERROR: Metrics file not found: {metrics_file}")
    sys.exit(2)

metrics = json.loads(metrics_file.read_text())

# TODO 4:
# Read the current accuracy from the metrics dictionary.
current_accuracy = float("TODO")

# TODO 5:
# Calculate the drift threshold.
# threshold = baseline_accuracy - allowed_drop
threshold = 0.0

print(f"Baseline accuracy: {baseline_accuracy:.4f}")
print(f"Current accuracy:  {current_accuracy:.4f}")
print(f"Allowed drop:     {allowed_drop:.4f}")
print(f"Drift threshold:   {threshold:.4f}")

# TODO 6:
# If current accuracy is below the threshold:
#   print "DRIFT DETECTED"
#   print "Retraining is required."
#   exit with code 10
#
# Otherwise:
#   print "NO DRIFT"
#   print "Model remains within the accepted performance range."
#   exit with code 0
