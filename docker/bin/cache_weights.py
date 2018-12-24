"""Cache weights for trained models during docker build so that they will be available without download at runtime."""

from detectron.core.config import cfg
from detectron.utils.io import cache_url

weights_2_cache = [
    'https://s3-us-west-2.amazonaws.com/detectron/35861858/12_2017_baselines/e2e_mask_rcnn_R-101-FPN_2x.yaml.02_32_51.SgT4y1cO/output/train/coco_2014_train:coco_2014_valminusminival/generalized_rcnn/model_final.pkl'
]

for w in weights_2_cache:
    cache_url(w, cfg.DOWNLOAD_CACHE)