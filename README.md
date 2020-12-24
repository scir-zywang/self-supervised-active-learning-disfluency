# self-supervised-activate-learning-disfluency

Combining Self-Supervised Learning and Activate-Learning for Disfluency Detection

This repo contains the code and model used for Combining Self-Training and Self-Supervised Learning for Combining Self-Supervised Learning and Activate Learning for Disfluency Detection.

Now all the code and model are released. Thank you for your patience!


## About Model
We release our self-supervised model trained by pseudo data. Please download it in the following link, and put the "pytorch_model.bin" in the "self_supervised_model" folder.

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

