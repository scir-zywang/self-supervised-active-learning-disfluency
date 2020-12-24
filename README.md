# self-supervised-activate-learning-disfluency

Combining Self-Supervised Learning and Activate-Learning for Disfluency Detection

This repo contains the code and model used for Combining Self-Training and Self-Supervised Learning for Combining Self-Supervised Learning and Activate Learning for Disfluency Detection.

Now all the code and model are released. Thank you for your patience!



## About Dataset

Since the *switchboard* dataset was bought from LDC(linguistic Data Consortium), so we have no right to release the data in this repo.

But we give the sample of the data.

If you want to run this repo, you need to collect the *switchboard* dataset or other disfluency dataset by yourself. Remember to organize the data as the format of the sample data.

It worth noting that the train dataset need to be split into *train.tsv* and *unused.tsv*. There should be 100 sentence annotated data in *train.tsv*. And the other annotated train data should be in *unused.tsv*.

What we did in the paper was to simulate the activate learning process. So all the train data we used were annotated before. If you want to use our solution in real scene, you need to modify the automatic script to deal with the unannotated data. That will be easy!

## About Model
We also release our self-supervised model trained by pseudo data. Please download it in the following link, and put the "pytorch_model.bin" in the "self_supervised_model" folder.

[download_model][model_link]

[model_link]: https://drive.google.com/file/d/1WXuTC5ygmiilfVOoW9Iwi94bbvk6dS3t/view?usp=sharing

## How to Use

```
conda create -n sa_disfluency python=3.7
conda activate sa_disfluency
conda install pytorch torchvision torchaudio cudatoolkit=10.1 -c pytorch
python transformers/setup.py install
nohup sh auto_self_supervise_activate_learning.sh 0 _self_supervise_mnlp 0 > log_self_supervise_mnlp 2>&1 &
```

## About GPU

This repo need to be run on GPU, and it will cost 3~4 GPU RAM.


## Contact

zywang@ir.hit.edu.cn and slwang@ir.hit.edu.cn

