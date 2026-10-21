accelerate launch train_mc.py \
  --model_name_or_path hfl/chinese-roberta-wwm-ext-large \
  --train_file ./dataset/train.json \
  --validation_file ./dataset/valid.json \
  --max_seq_length 512 \
  --per_device_train_batch_size 4 \
  --per_device_eval_batch_size 8 \
  --learning_rate 3e-5 \
  --weight_decay 0.01 \
  --num_train_epochs 5 \
  --gradient_accumulation_steps 16 \
  --output_dir ./checkpoints_roberta_chinese_squad/ \
  --pad_to_max_length

