
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


console.log("bob the builder")

ref.on("child_added", function(snapshot, prevChildKey) {
  var value = String(snapshot.val().input);
  var key = snapshot.key
  //console.log(snapshot.val().input);



  var spawn = require("child_process").spawn;
  var process = spawn('python3',["./script1.py",value]);


  process.stdout.on('data', function (data){

      console.log(data.toString());
      dataString = data.toString().trim();
      //var postsRef = ref.child(key);
      var ref = db.ref("validate").child(key);

       ref.set(dataString);

  });

  // var ref2 = db.ref('/courses_subscribers');
  // ref.on("child_removed", function(snapshot) {
  //
  //   var deletedClass = String(snapshot.getPriority());
  //   var refCourse = db.ref('/courses');
  //   refCourse.child(deletedClass).remove();
  //
  // console.log("The class '" + deletedClass + "' has been deleted");
  // });



});
