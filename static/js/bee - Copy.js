//----------------------------------------------------
// Settings
var countB = 0; // initialize the bee counts
var threshold = 0.90;
var targetClass = "Bee";
//---------------------------------------------------


// More API functions here:
// https://github.com/googlecreativelab/teachablemachine-community/tree/master/libraries/image

// the link to your model provided by Teachable Machine export panel
const URL = "https://teachablemachine.withgoogle.com/models/xwhfd4kp/";

let model, webcam, labelContainer, maxPredictions;

// Load the image model and setup the webcam
async function init() {
    const modelURL = URL + "model.json";
    const metadataURL = URL + "metadata.json";

    // load the model and metadata
    // Refer to tmImage.loadFromFiles() in the API to support files from a file picker
    // or files from your local hard drive
    // Note: the pose library adds "tmImage" object to your window (window.tmImage)
    model = await tmImage.load(modelURL, metadataURL);
    maxPredictions = model.getTotalClasses();

    // Convenience function to setup a webcam
    const flip = true; // whether to flip the webcam
    webcam = new tmImage.Webcam(200, 200, flip); // width, height, flip
    await webcam.setup(); // request access to the webcam
    await webcam.play();
    window.requestAnimationFrame(loop);

    // append elements to the DOM
    document.getElementById("webcam-container").appendChild(webcam.canvas);
    labelContainer = document.getElementById("label-container");
    for (let i = 0; i < maxPredictions; i++) { // and class labels
        labelContainer.appendChild(document.createElement("div"));
    }
}

async function loop() {
    webcam.update(); // update the webcam frame
    await predict();
    window.requestAnimationFrame(loop);
}

// run the webcam image through the image model
async function predict() {
    // predict can take in an image, video or canvas html element
    const prediction = await model.predict(webcam.canvas);
    for (let i = 0; i < maxPredictions; i++) {
        var p_Bee = prediction[i].probability.toFixed(2);
        var spacies = prediction[i].className;
        if (p_Bee>=threshold && spacies ==targetClass) {
            
            // Run the code below once the probability of a specific spacy (i.e., bee) reaches the threshold
            
            //send the json data back to the server, using ajax
            $.getJSON($SCRIPT_ROOT + "/cameradatatransfer/",//receiving url
                      {p_Bee: p_Bee}//data that are sent back to server
            )
            
            
            
            
            $("#Beee").html("<img src='statics/img/ArtificialFlowerBee.png' style='max-width: 250px;'>"); // color the bee
            setTimeout(function(){ 
                $("#Beee").html("<img src='statics/img/ArtificialFlower.png' style='max-width: 250px;'>");
            }, 3000); // gray out the bee after 3000ms (3 seconds)
            countB++; // counting bees

        };
        const classPrediction =
            prediction[i].className + ": " + prediction[i].probability.toFixed(2);
            labelContainer.childNodes[i].innerHTML = classPrediction; // display probabilities

        // display bee counts
        const countDisplay =
            "Count Bees: " + countB;
        console.log(classPrediction);
        labelContainer.childNodes[1].innerHTML = countDisplay;
    }

}

jQuery(function(){
   jQuery('#modal').click();
}); // automativally click the button when the page is loaded