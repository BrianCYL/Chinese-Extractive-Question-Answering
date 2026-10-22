## Preparing
Install the dependencies listed by running:
```
pip install -r requirement.txt
```

Download the dataset and checkpoints (if needed) from following command:
```bash
bash download.sh
```
Then, the folder structure should be similar to the one below:

```
|- checkpoints_roberta-chinese_qa
|- checkpoints_roberta-chinese_squad
|- dataset
    |- train.json
    |- valid.json
    |- test.json
    |- context.json
```

## Preprocessing
Please run the following command to transform the data format to adapt to the QA Training session.
```
python preprocessing.py
```
Finally, under the `dataset` folder, there will be two new json files, called `train_qa.json` and `valid_qa.json`.

## Train the RoBERTa Model for Multiple Choice Porblem
Pleace run the following command:
```
bash train_mc.sh
```
After running the above bash script, the trained model will be stored in a folder called `checkpoints_roberta_chinese_squad`, which is shown below.
```
|- ...
|- dataset
|- train_mc.sh
|- checkpoints_roberta_chinese_squad
    |- tokenizer
    |- vocab.txt
    |- model.safetensors
    |- ...
```

## Train the RoBERTa Model for Question Answering Porblem
Pleace run the following command:
```
bash train_qa.sh
```
After running the above bash script, the trained model will be stored in a folder called `checkpoints_roberta_chinese_qa`, which is shown below.
Also the figure of the training loss curve and the evaluation metric curve are also included in the checkpoint folder, which is shown below.
```
|- ...
|- dataset
|- train_mc.sh
|- train_qa.sh
|- checkpoints_roberta_chinese_qa
    |- tokenizer
    |- vocab.txt
    |- model.safetensors
    |- training_tracking.pdf
    |- metric_tracking.pdf
    |- ...
```

## Inference
Run the complete inference pipeline with the following command:
```
bash run.sh <context_file> <test_file> <output_dir>
```

- `<context_file>` is the JSON file containing the context paragraphs.
- `<test_file>` is the JSON file containing the multiple-choice test examples.
- `<output_dir>` is the directory where the final QA predictions will be saved.

The pipeline first predicts the relevant paragraph with the multiple-choice model, writes `choices.npy` and `test_qa.json` under `./dataset`, and then extracts the answer with the QA model. The final predictions are saved as `predictions.csv` under `<output_dir>`.

For example:
```
bash run.sh ./dataset/context.json ./dataset/test.json ./predictions
```