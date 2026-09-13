# Assignment 3 – Continuous MLOps with Azure DevOps

This folder is the **student starting point** for Assignment 3.

Your task is to implement and run a continuous MLOps workflow for the supplied
machine-learning application using Azure DevOps Pipelines.

The intended lifecycle is:

    Train → Evaluate → Quality Gate → Deploy
                              ↓
                           Monitor
                         ↙         ↘
                    No degradation  Degradation
                         ↓              ↓
                     Keep model      Retrain
                                       ↓
                                  Evaluate again
                                       ↓
                                  Quality Gate
                                       ↓
                                    Deploy

## Repository contents

### `app/`

Contains the supplied machine-learning application.

- `train.py` trains a model and writes the trained model plus training metrics.
- `predict.py` loads a model, evaluates it on a dataset, and writes evaluation metrics.
- `__init__.py` marks the directory as a Python package.

You normally do **not** need to modify the application code.

### `data/`

Contains the supplied data-generation script.

- `generate_data.py` creates the training and test datasets used in the assignment.
- The generated datasets represent the different situations required to demonstrate
  normal and changed production data.

You normally do **not** need to modify this script.

### `tests/`

Contains tests for the ML application and pipeline functionality.

Run them locally with:

    python -m pytest -v tests/test_pipeline.py

Your Azure DevOps pipelines should also execute the tests.

### `scripts/quality_gate.py`

Checks whether a trained model satisfies the required minimum quality.

The quality gate evaluates:

- Accuracy
- F1 score

A model that does not satisfy the thresholds must cause the pipeline to fail
and must not be approved for deployment.

This script is supplied as part of the assignment.

### `scripts/check_drift.py`

This is one of your implementation tasks.

Complete the TODOs so that the script:

1. Reads the monitoring metrics.
2. Reads the configured baseline accuracy.
3. Reads the allowed accuracy drop.
4. Calculates the drift threshold.
5. Compares the current accuracy with the threshold.
6. Reports either `NO DRIFT` or `DRIFT DETECTED`.
7. Returns exit code `0` when there is no drift.
8. Returns exit code `10` when drift is detected.
9. Returns a different non-zero code if the check itself fails.

The exit code is important because the Azure DevOps monitoring pipeline
uses it to decide whether retraining is required.

### `pipelines/`

Contains the Azure DevOps YAML pipeline templates you must complete and run.

#### `train-deploy-a.yml`

Creates the initial model lifecycle.

It should:

- prepare the environment,
- install dependencies,
- generate data,
- run tests,
- train the initial model,
- evaluate it,
- apply the quality gate,
- and publish the approved model as a pipeline artifact.

The artifact represents the currently deployed model in this teaching setup.

#### `monitor-normal.yml`

Checks whether the deployed model still performs well under normal
production conditions.

It should:

- obtain the currently deployed model artifact,
- generate/prepare the production data,
- evaluate the model on normal data,
- calculate its performance,
- run the drift check,
- and finish successfully without triggering retraining when performance
  remains within the accepted range.

#### `monitor-drift.yml`

This is the central orchestration task.

It should:

- obtain the currently deployed model,
- evaluate it on changed production data,
- run the drift detection logic,
- correctly distinguish `NO DRIFT` from `DRIFT DETECTED`,
- and automatically trigger the retraining workflow when drift is detected.

Pay particular attention to handling the drift detector's exit code.
`DRIFT DETECTED` is an expected condition in this assignment and should
not simply make the monitoring pipeline fail.

#### `retrain-deploy-b.yml`

Creates the adapted model after degradation has been detected.

It should:

- prepare the updated training data,
- train the new model,
- evaluate it on independent test data,
- apply the quality gate,
- and publish the new model only if it passes the quality requirements.

## Important concepts

### Pipeline artifacts

A pipeline artifact is used to pass the trained model from one stage of the
MLOps lifecycle to another.

In this assignment, the artifact represents the deployed model. This is a
teaching simulation; you are not required to create a real Azure ML endpoint.

### Quality gate

Automatic retraining does not automatically mean automatic deployment.

The newly trained model must first pass the quality gate. This prevents a
new model with worse performance from replacing an existing model simply
because retraining was triggered.

### Drift detection

For this assignment, drift is simplified to **performance degradation on
new labelled production data**.

The initial baseline accuracy is approximately:

    0.892

The maximum allowed accuracy drop is:

    0.10

Therefore:

    drift threshold = 0.892 - 0.10 = 0.792

If current accuracy is below `0.792`, the system should report:

    DRIFT DETECTED

and initiate retraining.

## Your goal

The final result should demonstrate a complete closed-loop MLOps workflow:

    Train → Deploy → Monitor → Detect → Retrain → Evaluate → Deploy

Do not treat the pipelines as independent tasks. The important part of this
assignment is that they work together as one automated ML lifecycle.
