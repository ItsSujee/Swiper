cd tensorflow
source bin/activate
cd tensorflow-for-poets-2

while True
do
	python -m scripts.tinder_next_image
	python -m scripts.label_image_for_tinder \
	--graph=tf_files/retrained_graph.pb  \
	--image=tf_files/Run_Retrain_Models/test.png
done