
import os
import shutil
import tempfile
from uuid import uuid4

from django import forms
from django.core.files.storage import default_storage

from libs.mosaic import MosaicFaceImage


class UploadForm(forms.Form):
    file = forms.ImageField(label='画像ファイル')

    def save(self):
        upload_file = self.cleaned_data['file']
        file_name = self.mosaic(upload_file.name, upload_file)

        return default_storage.url(file_name)

    def save_uploaded_file(self, file_name, content):
        with open(file_name, 'wb') as destination:
            for chunk in content.chunks():
                destination.write(chunk)

    def mosaic(self, file_name, src):
        """ tmpdir に出力してからモザイクをかける """

        with tempfile.TemporaryDirectory() as tmpdname:
            src_image_file = os.path.join(tmpdname, file_name)
            # 拡張子取得
            ext = file_name.split('.')[-1]
            dst_image_file = os.path.join(tmpdname, "mosaic_{}.{}".format(uuid4().hex, ext))
            # ローカルに一度保存
            self.save_uploaded_file(src_image_file, src)
            # モザイクがけ
            MosaicFaceImage().mosaic(src_image_file, dst_image_file)
            # ファイル保存
            with open(dst_image_file, 'rb') as f:
                file_name = default_storage.save(os.path.basename(dst_image_file), f)
            return file_name
