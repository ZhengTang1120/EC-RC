#!/bin/sh

for iter in {1..5}
do
    # train
	python train.py --lr 1e-5 --pooling avg --batch_size 32 --num_epoch 20 --seed 43 --id $iter --device 0 --warmup_prop 0.3 --data_dir dataset/tacred --info "TACRED EC+RC" 
	# generate model output
	python eval.py saved_models/$iter --device 0 --dataset train --iter $iter
	# generate rules
	python collect_rules.py $iter
	python generate_rules.py $iter
	# excute rules
	sbt -J-Xmx4G "runMain shell /data/dev.json /grammars_$iter/ dev_output_$iter.txt"
	# eval rules
	python eval_per_rule.py
	# filter rules
	TODO
	# generate new taggings
	python create_tagging.py
done
	


