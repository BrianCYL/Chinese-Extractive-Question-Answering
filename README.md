## Preparing
- Download the codes from this [Google Drive](https://drive.google.com/drive/folders/1yqt7SSi-CxQ3KAH8VbSePmbPf3KUD37a?usp=sharing).
- Then, the folder structure should be similar to the one below, where the `dataset` folder is same as the one provided from TAs.

```
|- dataset
    |- train.json
    |- valid.json
    |- test.json
    |- context.json
    
|- preprocessing.py
```

## Preprocessing
- Please run the following command to transform the data format to adapt to the QA Training session.
```
python preprocessing.py
```
- Finally, under the `dataset` folder, there will be two new json files, called `train_qa.json` and `valid_qa.json`.

## Train the RoBERTa Model for Multiple Choice Porblem
- Pleace run the following command:
```
bash train_mc.sh
```
- After running the above bash script, the trained model will be stored in a folder called `checkpoints_roberta_chinese_squad`, which is shown below.
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
- Pleace run the following command:
```
bash train_qa.sh
```
- After running the above bash script, the trained model will be stored in a folder called `checkpoints_roberta_chinese_qa`, which is shown below.
- Also the figure of the training loss curve and the evaluation metric curve are also included in the checkpoint folder, which is shown below.
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