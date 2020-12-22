
gpu=$1
run=$2
seed=$3

for ((i=100;i<54000;i+=100));
# for ((i=500;i<3500;i+=1000));
do 
CUDA_VISIBLE_DEVICES=${gpu} nohup python run_disfluency_activate_learning_bert.py --task_name disfluency --do_train --do_eval --do_lower_case --data_dir data/run${run}/${i}/ --bert_model bert_model/empty_english_small/ --max_seq_length 128 --train_batch_size 32 --eval_batch_size 32 --learning_rate 2e-5 --num_train_epochs 30.0 --output_dir run${run}/${i}/ --do_tagging --pretrain_model_dir self_supervised_model --pretrain_model_name pytorch_model.bin --use_new_model --model_name_or_path bert_model/empty_english_small/ --seed ${seed} > log/run${run}_${i}
wait

CUDA_VISIBLE_DEVICES=${gpu} nohup python run_disfluency_activate_learning_bert.py --task_name disfluency --do_unused_predict --do_lower_case --data_dir data/run${run}/${i}/ --bert_model bert_model/empty_english_small/ --max_seq_length 128 --train_batch_size 32 --eval_batch_size 128 --learning_rate 2e-5 --num_train_epochs 30.0 --output_dir run${run}/${i}_predict/ --do_tagging --pretrain_model_dir run${run}/${i}/ --pretrain_model_name pytorch_model.bin --use_new_model --model_name_or_path bert_model/empty_english_small/ --seed ${seed} > log/run${run}_${i}_predict
wait

python select_by_mnlp.py run${run}/${i}_predict/unused_results.txt run${run}/${i}_predict/sorted_mnlp.txt
wait

python data_prepare.py ${i} 100 run${run} sorted_mnlp
wait

cp data/run${run}/${i}/dev.tsv data/run${run}/$(($i+100))/.
wait
cp data/run${run}/${i}/test.tsv data/run${run}/$(($i+100))/.
wait
done
