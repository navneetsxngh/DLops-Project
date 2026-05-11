## DVC -> Data Version Control

This is a tool that is used to version control for large files, datasets and machine learning models.
Something that traditional verison control systems struggle with.

DVC tracks datasets, manage data pipelines and reproduce experiments. 
So instead of storing files directly in git, DVC stores metadata `.dvc` files in git and stores actual data in remote storage like S3, Google Drive or local database.

While git is used tracking the code changes, collabarations and version history of files.

### Difference Between **DVC** v/s **GIT**

### Difference Between DVC and Git

| Feature                  | Git                                  | DVC                                      |
|---------------------------|--------------------------------------|------------------------------------------|
| Purpose                   | Version control for code and projects | Version control for datasets, ML models, and pipelines |
| Handling Large Files      | Limited efficiency                   | Optimized for large data files           |
| Data Storage              | Stored directly in repository        | Stored in external storage               |
| Change Tracking           | Tracks code changes                  | Tracks data, models, and code            |
| Pipeline Management       | Not supported                        | Built-in pipeline support                |
| Reproducibility           | Basic support                        | Strong reproducibility features          |
| Machine Learning Focus    | General-purpose VCS                  | Specifically designed for ML workflows   |

### Commands:-

1. Initialize DVC in your project and it creates .dvc folder, adds config files
It must be run after `git init`

```bash
dvc init
```

2. It creates data.dvc, adds original file to .gitignore and Stores files in DVC cache
```bash
dvc add <file>
```

3. Using this command git tracks metadata not the actual data
```bash
git add data.dvc .gitignore
git commit -m "Track Dataset"
```

4. It connects the storage from S3, GDrive and local file, Here `-d` means defaukt remote
```bash
dvc remote add -d <path>
```

5. It will upload the to remote storage
```bash
dvc push
```

6. It will download the data from remote
```bash
dvc pull
```

7. It restores data version based on `git commit` and it's syncs workspace with `.dvc` files
```bash
dvc checkout
```

8. Stops tracking a file
```bash
dvc remove
```

### Run Pipeline Stage

```bash
dvc stage add -n preprocess -d preprocess.py -d data.csv -o clean.csv python preprocess.py
```

`-n` --> Stage Name
`-d` --> Dependencies
`-o` --> outputs

```bash
dvc repro
```
Re-run Pipeline when the data and code changes


```bash
dvc dag
```
It is used for visualization of pipeline


### INTERVIEW QUESTIONS
1. Why do we need DVC if we already have git?
2. What files does dvc create?
3. What is DVC cache?