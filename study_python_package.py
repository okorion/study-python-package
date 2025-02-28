"""
Python Advanced - 패키지 만들기
png(jpg) to gif, pil, image

"""

import glob
from PIL import Image

# 이미지, 결과 생성 경로
path_in = "./images/*.png"
path_out = "./image_out/result.gif"

# 첫 번째 이미지 & 모든 이미지 리스트 팩킹
img, *imgs = [Image.open(f) for f in sorted(glob.glob(path_in))]

# 이미지 저장
img.save(
    fp=path_out, format="GIF", append_images=imgs, save_all=True, duration=500, loop=0
)
