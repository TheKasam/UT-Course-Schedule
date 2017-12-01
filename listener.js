
var admin = require("firebase-admin");

var serviceAccount = require("./courseschedule-8a816-firebase-adminsdk-jgy6n-2f35d9eaad.json");

admin.initializeApp({
  credential: admin.credential.cert(serviceAccount),
  databaseURL: "https://courseschedule-8a816.firebaseio.com/"
});

// Import Admin SDK
var admin = require("firebase-admin");

// Get a database reference to our posts
var db = admin.database();
var ref = db.ref("validate");

// Attach an asynchronous callback to read the data at our posts reference
/* ref.on("value", function(snapshot) {
  console.log(snapshot.val());
}, function (errorObject) {
  console.log("The read failed: " + errorObject.code);
}); */

console.log("bob the builder")

ref.on("child_added", function(snapshot, prevChildKey) {
  var value = snapshot.val();
  var key = Object.keys(snapshot.val());
  console.log(snapshot.key);


});

var spawn = require("child_process").spawn;
var process = spawn('python',["./script1.py"]);


process.stdout.on('data', function (data){

    console.log(data.toString());
});
