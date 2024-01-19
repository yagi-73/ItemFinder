function previewImage(input) {
  var preview = document.getElementById('preview');
  var file = input.files[0];
  var reader = new FileReader();

  reader.onloadend = function () {
    preview.src = reader.result;
    preview.style.display = 'block';
  }

  if (file) {
    reader.readAsDataURL(file);
  } else {
    preview.src = '';
    preview.style.display = 'none';
  }
}

document.addEventListener('DOMContentLoaded', function () {
  // フォームがサブミットされたときに呼び出される関数
  document.getElementById('captureForm').addEventListener('submit', function () {
    // ローダーを表示
    document.getElementById('loader').style.display = 'block';
    // 背景色を設定
  });
});