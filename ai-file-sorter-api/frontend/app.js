function uploadFile() {
    let fileInput = document.getElementById("fileInput").files[0];
    if (!fileInput) {
        document.getElementById("status").innerText = "Please select a file.";
        return;
    }

    let formData = new FormData();
    formData.append("file", fileInput);

    fetch("http://127.0.0.1:5005/api/upload", { // Make sure port matches your Flask server
        method: "POST",
        body: formData
    })
    .then(response => response.json())
    .then(data => {
        if (data.message) {
            document.getElementById("status").innerText = "✅ " + data.message;
        } else {
            document.getElementById("status").innerText = "❌ Upload failed: " + data.error;
        }
    })
    .catch(error => {
        document.getElementById("status").innerText = "❌ Error: " + error;
    });
}
