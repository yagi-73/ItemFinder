#? This is moore's AI test file.
##! Check!!! install this library.##? pip3 install matplotlib opencv-python tensorflow tensorflow-hub
###   https://stackoverflow.com/questions/50236117/scraping-ssl-certificate-verify-failed-error-for-http-en-wikipedia-org/53310545#53310545   ###


import numpy as np
import tensorflow as tf
import tensorflow_hub as hub
from PIL import Image

class RecommendedFeature:
    def __init__(self, shirts, jacket, pants):
        self.shirts = shirts
        self.jacket = jacket
        self.pants = pants

img_path = '/Users/moore/git/ItemFinder/moore_AI_test/sanple_image/61obz82MvTL._AC_UF894,1000_QL80_.jpg'

def scoreFinder(score):
    ans = []
    sample = [[0.1,0.2,0.25,0.3],[0.35,0.38,0.4,0.45,0.48],[0.3,0.5,0.55,0.6,0.7]]
    for i in range(3):
        if float(score[i]) <= sample[i][0]:
            ans.append('A')
        elif sample[i][1] < float(score[i]) <= sample[i][2]:
            ans.append('B')
        elif sample[i][2] < float(score[i]) <= sample[i][3]:
            ans.append('C')
        elif sample[i][3] < int(score[i]) <= sample[i][4]:
            ans.append('D')
        else:
            ans.append('E')
    return ans

class PoseEstimator:
    
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


def st_search(file):
    # import argparse

    import cv2

    # # 引数の設定
    # parser = argparse.ArgumentParser()

    # parser.add_argument("image_path", help="実験対象の画像へのパス")

    # args = parser.parse_args()

    # img = cv2.imread(img_path)
    image = Image.open(file)
    image_np = np.array(image)

    # モデルの初期化
    print('model clearing now.')
    pe = PoseEstimator()
    # 画像のキーポイントを取得
    keypoints = pe.predict(image_np)
    
    shoulder_width = np.sqrt((keypoints[0,0,5,0]-keypoints[0,0,6,0])**2 + (keypoints[0,0,5,1]-keypoints[0,0,6,1])**2 + ((keypoints[0,0,5,2]-keypoints[0,0,6,2])**2))
    
    l_arm_len = np.sqrt((keypoints[0,0,5,0]-keypoints[0,0,7,0])**2 + (keypoints[0,0,5,1]-keypoints[0,0,7,1])**2 + ((keypoints[0,0,5,2]-keypoints[0,0,7,2])**2)) + np.sqrt((keypoints[0,0,9,0]-keypoints[0,0,7,0])**2 + (keypoints[0,0,9,1]-keypoints[0,0,7,1])**2 + ((keypoints[0,0,9,2]-keypoints[0,0,7,2])**2))
    r_arm_len = np.sqrt((keypoints[0,0,8,0]-keypoints[0,0,6,0])**2 + (keypoints[0,0,8,1]-keypoints[0,0,6,1])**2 + ((keypoints[0,0,8,2]-keypoints[0,0,10,2])**2)) + np.sqrt((keypoints[0,0,8,0]-keypoints[0,0,10,0])**2 + (keypoints[0,0,8,1]-keypoints[0,0,10,1])**2 + ((keypoints[0,0,8,2]-keypoints[0,0,10,2])**2))
    arm_ave = (l_arm_len + r_arm_len)/2
    
    l_leg_len = np.sqrt((keypoints[0,0,11,0]-keypoints[0,0,13,0])**2 + (keypoints[0,0,11,1]-keypoints[0,0,13,1])**2 + ((keypoints[0,0,11,2]-keypoints[0,0,13,2])**2)) + np.sqrt((keypoints[0,0,13,0]-keypoints[0,0,15,0])**2 + (keypoints[0,0,13,1]-keypoints[0,0,15,1])**2 + ((keypoints[0,0,13,2]-keypoints[0,0,15,2])**2))
    r_leg_len = np.sqrt((keypoints[0,0,12,0]-keypoints[0,0,14,0])**2 + (keypoints[0,0,12,1]-keypoints[0,0,14,1])**2 + ((keypoints[0,0,12,2]-keypoints[0,0,14,2])**2)) + np.sqrt((keypoints[0,0,14,0]-keypoints[0,0,16,0])**2 + (keypoints[0,0,14,1]-keypoints[0,0,16,1])**2 + ((keypoints[0,0,14,2]-keypoints[0,0,16,2])**2))
    leg_ave = (l_leg_len + r_leg_len)/2
    
    # print(keypoints[0,0,0])
    shirts, jacket, pants = scoreFinder([shoulder_width, arm_ave, leg_ave])
    recommended_feature = RecommendedFeature(shirts, jacket, pants)
    return(recommended_feature)

    # 実行結果を保存
    # drwaed_img = pe.draw_prediction_on_image(img, keypoints=keypoints)
    # # cv2.imwrite(f"{args.image_path.split('.')[0]}_results.png", drwaed_img)     #?画像パス
    # cv2.imwrite(f"{img_path.split('.')[0]}_results.png", drwaed_img)     #?画像パス

    # # 出力
    # h, w, _ = drwaed_img.shape
    # concat_img = cv2.hconcat([cv2.resize(img, (w, h)), drwaed_img])
    # cv2.imshow("smaple", concat_img)

    # # キーが押されるまで待ち続ける。
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()

if __name__ == "__main__":
    ans = st_search(img_path=img_path)
    print(' inner : ', ans[0],'\n outer :',ans[1],'\n pants :',ans[2])