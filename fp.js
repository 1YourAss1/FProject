const xhr = new XMLHttpRequest();
const fpPromise = import('https://openfpcdn.io/fingerprintjs/v3')
            .then(FingerprintJS => FingerprintJS.load())

function collectData() {
    fpPromise
    .then(fp => fp.get())
    .then(result => {
        console.log(result.components)            
        // download(JSON.stringify(result.components), 'FingerprintJS.json', 'text/plain');
        sendDataToServer(JSON.stringify(result.components));

        // This is the visitor identifier:
        const visitorId = result.visitorId
        console.log("FingerprintJS: " + visitorId)
    })
}

function sendDataToServer(data) {
    xhr.open("POST", "/");
    xhr.setRequestHeader("Content-Type", "application/json");
    xhr.send(data);
}

function test() {
    console.log("testik");
}
