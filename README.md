# self-supervised-activate-learning-disfluency

Combining Self-Supervised Learning and Activate-Learning for Disfluency Detection

This repo contains the code and model used for Combining Self-Training and Self-Supervised Learning for Combining Self-Supervised Learning and Activate Learning for Disfluency Detection.

This repo is still being improved. All the code is uploaded and we are working on uploading model. 

Since the model have not been uploaded, you can't run this repo directly. But you can follow the instruction in the paper to train a self-supervised disfluency model and then you can run the repo by putting your model in "self_supervised_model" folder.

Thank you for your patience, and the model is coming soon.

## How to use

```
conda create -n sa_disfluency
conda activate sa_disfluency
conda install pytorch torchvision torchaudio cudatoolkit=10.1 -c pytorch
python transformers/setup.py install
nohup sh auto_self_supervise_activate_learning.sh 0 _self_supervise_mnlp 0 > log_self_supervise_mnlp 2>&1 &
```


## Contact
zywang@ir.hit.edu.cn and slwang@ir.hit.edu.cn
