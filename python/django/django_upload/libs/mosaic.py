
import cv2
import face_recognition


class MosaicFaceImage:

    def _area_mosaic(self, img, scale=0.05):
        # 画像を scale (0 < scale <= 1) 倍にリサイズする。
        mosaiced = cv2.resize(img, dsize=None, fx=scale, fy=scale,
                              interpolation=cv2.INTER_NEAREST)
        # 元の大きさにリサイズする。
        h, w = img.shape[:2]
        mosaiced = cv2.resize(mosaiced, dsize=(w, h),
                              interpolation=cv2.INTER_NEAREST)
        return mosaiced

    def mosaic(self, src_image_file, dst_image_file):
        """ 顔画像モザイク """
        src = cv2.imread(src_image_file)

        # 顔検出する。
        locations = face_recognition.face_locations(src)

        # 検出された顔領域に対して、モザイク処理を行う。
        for top, right, bottom, left in locations:
            src[top:bottom, left:right] = self._area_mosaic(
                src[top:bottom, left:right])

        cv2.imwrite(dst_image_file, src)
