#? This is moore's AI test file.
#! Check!!! install this library.
#? pip3 install matplotlib opencv-python tensorflow tensorflow-hub
#!! CERTIFICATE_VERIFY_FAILED ↓
###   https://stackoverflow.com/questions/50236117/scraping-ssl-certificate-verify-failed-error-for-http-en-wikipedia-org/53310545#53310545   ###


import numpy as np
import tensorflow as tf
import tensorflow_hub as hub

img_path = '/Users/sasakimoore/Documents/GitHub/ItemFinder/moore_AI_test/sanple_image/dfed1914c383418be6bd1544234f36b6_1.jpg'

class PoseEstimator:
    """入力画像から骨格のキーポイントを返す。"""

    def __init__(self) -> None:
        # Download the model from TF Hub.
        model = hub.load("https://www.kaggle.com/models/google/movenet/frameworks/TensorFlow2/variations/singlepose-lightning/versions/4")
        self.movenet = model.signatures["serving_default"]

    def predict(self, target_image: np.ndarray) -> np.ndarray:
        """RGB画像の入力から、その画像に映る1人の骨格のキーポイントを返す。

        Args:
            target_image (np.ndarray): 処理対象の画像

        Returns:
            np.ndarray: 検出されたキーポイント
        """
        # 推論できるように画像の整形
        image = tf.expand_dims(target_image, axis=0)
        image = tf.cast(tf.image.resize_with_pad(image, 192, 192), dtype=tf.int32)
        # Run model inference.
        outputs = self.movenet(image)
        # Output is a [1, 1, 17, 3] tensor.
        keypoints = outputs["output_0"]

        del outputs, image, target_image
        return keypoints.numpy()

    def draw_prediction_on_image(self, target_image: np.ndarray, keypoints: np.ndarray):

        from util import draw_prediction_on_image

        return draw_prediction_on_image(target_image, keypoints)


if __name__ == "__main__":
    import argparse

    import cv2

    # # 引数の設定
    # parser = argparse.ArgumentParser()

    # parser.add_argument("image_path", help="実験対象の画像へのパス")

    # args = parser.parse_args()

    # img = cv2.imread(args.image_path)                                           #?画像パス
    img = cv2.imread(img_path)                                                      

    # モデルの初期化
    pe = PoseEstimator()
    # 画像のキーポイントを取得
    keypoints = pe.predict(img)
    print(keypoints)

    # 実行結果を保存
    drwaed_img = pe.draw_prediction_on_image(img, keypoints=keypoints)
    # cv2.imwrite(f"{args.image_path.split('.')[0]}_results.png", drwaed_img)     #?画像パス
    cv2.imwrite(f"{img_path.split('.')[0]}_results.png", drwaed_img)     #?画像パス

    # 出力
    h, w, _ = drwaed_img.shape
    concat_img = cv2.hconcat([cv2.resize(img, (w, h)), drwaed_img])
    cv2.imshow("smaple", concat_img)

    # キーが押されるまで待ち続ける。
    cv2.waitKey(0)
    cv2.destroyAllWindows()

