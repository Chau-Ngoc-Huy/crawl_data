gen_cf: download
	python ./crawl/create_config.py 


down_img: gen_cf
	python ./crawl/google-images-download/google_images_download/google_images_download.py -cf ./crawl/config.json -n
down_video:
	python download_video/main.py


detect_img:
	python detect_face_image/detect_face.py
detect_video:
	python detect_face_video/main.py

	
update_env:
	pip freeze > requirements.txt
