function RunSentimentAnalysis() {

    let text = document.getElementById("textToAnalyze").value;

    fetch("/emotionDetector?textToAnalyze=" + text)
    .then(response => response.text())
    .then(data => {
        document.getElementById("system_response").innerHTML = data;
    });

}