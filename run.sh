accelerate launch inference_mc.py \
  --model_name_or_path ./checkpoints_roberta-chinese_squad/ \
  --context_file ${1} \
  --test_file ${2} \
  --output_dir ./dataset \
  --per_device_test_batch_size 8 \
  --max_seq_length 512 \
  --pad_to_max_length

python extract_qa_context.py \
    --context_file ${1} \
    --test_file ${2} \
    --choice_file choices.npy \
    --folder_path ./dataset

accelerate launch inference_qa.py \
    --model_name_or_path ./checkpoints_roberta-chinese_qa/ \
    --test_file ./dataset/test_qa.json \
    --context_file ${1} \
    --output_dir ${3} \
    --per_device_test_batch_size 8 \
    --max_seq_length 512 \
    --pad_to_max_length