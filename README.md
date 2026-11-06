# PS 2 Exercise 2 · Smoking is bad

This exercise reproduces the crude association between smoking and recorded
survival in the supplied sample. It then uses visualizations, age stratification,
and sensitivity analysis to examine how age composition affects that comparison.
Start with the [main notebook](smoking_is_bad.ipynb) for the full exercise.

[Course instructions](https://jewel-scowl-daa.notion.site/Ex-2-Smoking-is-bad-7f8a2a09d1068262b9510109161b64e1)

## Install and run

Install [Git](https://git-scm.com/install/) and [Pixi](https://pixi.sh/latest/installation/).
Then clone the repository and run these commands from the repository root.

```bash
git clone https://github.com/starries-creator/ps_2_ex2_smoking_is_bad.git
cd ps_2_ex2_smoking_is_bad
pixi install --locked -e smoke
pixi run -e smoke jupyter
```

Pixi installs the dependencies for the Python 3.12 `smoke` environment from
[pixi.lock](pixi.lock). In JupyterLab, open `smoking_is_bad.ipynb`, choose the
Python kernel from the `smoke` environment if prompted, and select **Run All**
to regenerate the tables. The figures linked from the main notebook are included
in the repository. Run the companion notebooks from the same directory.

The locked installation, JupyterLab launch, and all four notebooks were
verified on Apple Silicon macOS. The lock file also includes macOS Intel,
Linux x86-64, and Windows x86-64.

## Results and supporting files

- **[Main notebook](smoking_is_bad.ipynb)** covers data preparation, the crude
  comparison, and the combined analysis. In 1,314 records, the crude recorded
  survival proportions were **68.6%** for non-smokers and **76.1%** for smokers.
- **[Sample distributions](member_a_distributions.ipynb)** describes age,
  observed salary, smoking status, outcome, and gender. See the
  [numeric figure](figures/member_a_numeric_distributions.png) and
  [categorical figure](figures/member_a_categorical_distributions.png).
- **[Baseline age-stratified analysis](member_e_age_stratified_survival.ipynb)**
  compares the two smoking groups within ages 18–29, 30–49, 50–64, and 65+.
  The recorded survival proportion was lower for smokers in each baseline
  band. See the [baseline figure](figures/member_e_age_stratified_survival.png).
- **[Age-group sensitivity analysis](member_c_age_sensitivity.ipynb)** compares
  the baseline with coarser and finer bands. The age-standardized difference
  changes sign across the three schemes. See the
  [sensitivity figure](figures/member_c_age_sensitivity.png).
- **[Source data](data/smoking_data.csv)** contains the dataset supplied for the exercise.

The observed differences depend on the age distribution and the chosen bands.
The results describe the recorded outcomes in this sample.

## Contributor setup

Install the [notebook cleanup hook](.pre-commit-config.yaml) once per clone.
It clears cell outputs before commits. Use the second command to check all files.

```bash
pixi run -e smoke pre-commit install
pixi run -e smoke pre-commit run --all-files
```
