function goToCaptureScreen() {
    document.getElementById("topScreen").style.display = "none";
    document.getElementById("captureScreen").style.display = "block";
    document.getElementById("imageConfirmationScreen").style.display = "none";
    document.getElementById("recommendationScreen").style.display = "none";
}

function showImageConfirmationScreen() {
    // ここでユーザーの画像を表示するロジックを実装
    // 仮の画像URLをセットしています。実際の実装ではカメラからの画像を取得するなどが必要です。
    var imageUrl = "user_captured_image.jpg";
    document.getElementById("userImage").src = imageUrl;

    document.getElementById("topScreen").style.display = "none";
    document.getElementById("captureScreen").style.display = "none";
    document.getElementById("imageConfirmationScreen").style.display = "block";
    document.getElementById("recommendationScreen").style.display = "none";
}

function showRecommendationScreen() {
    // ここで骨格診断などの処理を行い、おすすめの衣服を取得するロジックを実装
    // おすすめの衣服データを recommendationText に表示
    var recommendationData = { clothing: "デニムジャケット(黒)" };
    document.getElementById("recommendationText").innerText = "おすすめの衣服: " + recommendationData.clothing;

    document.getElementById("topScreen").style.display = "none";
    document.getElementById("captureScreen").style.display = "none";
    document.getElementById("imageConfirmationScreen").style.display = "none";
    document.getElementById("recommendationScreen").style.display = "block";
}

function goToTopScreen() {
    document.getElementById("topScreen").style.display = "block";
    document.getElementById("captureScreen").style.display = "none";
    document.getElementById("imageConfirmationScreen").style.display = "none";
    document.getElementById("recommendationScreen").style.display = "none";
}

function toggleDetails() {
    var details = document.getElementById("productDetails");
    var productDetailsBtn = document.getElementById("productDetailsBtn");

    if (details.style.display === "none") {
        details.style.display = "block";
        productDetailsBtn.innerText = "閉じる";
    } else {
        details.style.display = "none";
        productDetailsBtn.innerText = "商品詳細";
    }
}
