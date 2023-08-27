function previewImage(imgId, input) {
  var imgElement = document.getElementById(imgId);
  if (input.files && input.files[0]) {
    var reader = new FileReader();
    reader.onload = function (e) {
      imgElement.src = e.target.result;
    };
    reader.readAsDataURL(input.files[0]);
  } else {
    imgElement.src = "#"; // Clear the image source if no file selected
  }
}
